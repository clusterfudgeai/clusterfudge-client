import asyncio
import dataclasses
import inspect
import io
import json
import os
import re
import time
import zipfile
from collections.abc import Sequence
from typing import Optional

import aiofiles
import dataclasses_json
import grpc
import grpc.aio
from anthropic.types.beta import (
    BetaMessageParam,
    BetaToolResultBlockParam,
    BetaToolUseBlockParam,
)
from clusterfudge_proto.launches import launches_pb2, launches_pb2_grpc
from clusterfudge_proto.resources import resources_pb2
from clusterfudge_proto.sandboxespb import sandboxes_pb2, sandboxes_pb2_grpc
from clusterfudge_proto.slurmpb import slurm_pb2, slurm_pb2_grpc
from clusterfudge_proto.tunnelpb import tunnel_pb2_grpc
from grpc import ssl_channel_credentials

LaunchStatus = launches_pb2.Launch.Status


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclasses.dataclass
class ClusterfudgeConfig:
    token: str


class APIKeyCallCredentials(grpc.AuthMetadataPlugin):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def __call__(self, context, callback):
        credentials = (("authorization", "Bearer " + self.api_key),)
        callback(credentials, None)


@dataclasses.dataclass
class Resources:
    cpus: int = 0
    memory_mb: int = 0
    a100_40gb: int = 0
    a100_80gb: int = 0
    h100: int = 0
    rtx3080: int = 0
    rtx3090: int = 0
    rtx6000: int = 0
    t4: int = 0
    l4: int = 0
    v100: int = 0
    p100: int = 0
    p4: int = 0
    rtx4090: int = 0
    rtx4080: int = 0
    rtx3070: int = 0
    rtx3060: int = 0
    rtx4070: int = 0
    rtx4060: int = 0
    rtx3050: int = 0
    gtx1050: int = 0
    h200: int = 0


@dataclasses.dataclass()
class LocalDir:
    pass


@dataclasses.dataclass()
class GitRepo:
    repo: str
    branch: str
    commit: Optional[str] = None


@dataclasses.dataclass()
class OnReplicaFailureOtherReplicasContinue:
    pass


@dataclasses.dataclass()
class OnReplicaFailureOtherReplicasAreStopped:
    pass


@dataclasses.dataclass()
class Process:
    command: Sequence[str]
    resource_requirements: Optional[Resources] = None


@dataclasses.dataclass()
class Job:
    short_name: str
    replicas: int
    processes: Sequence[Process]
    replica_failure_behaviour: Optional[
        OnReplicaFailureOtherReplicasContinue | OnReplicaFailureOtherReplicasAreStopped
    ] = None


@dataclasses.dataclass()
class QueueingBehaviour:
    enqueue_if_cluster_busy: Optional[bool] = True


@dataclasses.dataclass
class SandboxParams:
    sidecar_file_paths: Optional[list[str]] = None
    image_tag: Optional[str] = None


@dataclasses.dataclass()
class CreateLaunchRequest:
    jobs: Sequence[Job]
    name: Optional[str] = None
    description: Optional[str] = None
    deployment: Optional[LocalDir | GitRepo] = None
    cluster: Optional[str] = None
    shard: Optional[str] = None
    hostnames: Optional[Sequence[str]] = None
    queueing_behaviour: Optional[QueueingBehaviour] = None


def _validate_create_launch_request_v2(
    create_launch_request: CreateLaunchRequest,
) -> None:
    if create_launch_request.deployment is not None:
        if not isinstance(
            create_launch_request.deployment, LocalDir
        ) and not isinstance(create_launch_request.deployment, GitRepo):
            raise ValueError("deployment must be a LocalDir or GitRepo")

    if not create_launch_request.jobs:
        raise ValueError("jobs must be non-empty")

    for i, job in enumerate(create_launch_request.jobs):
        if not job.short_name:
            raise ValueError(f"short_name must be non-empty for job {i}")
        sn = job.short_name
        if not job.replicas:
            raise ValueError(f"replicas must be non-empty for job {sn}")
        if not job.processes:
            raise ValueError(f"processes must be non-empty for job {sn}")
        for process in job.processes:
            if not process.command:
                raise ValueError(f"command must be non-empty for job {sn}")


class SchedulingError(Exception):
    def __init__(self, message: str, scheduling_log: str):
        self.message = message
        self.scheduling_log = scheduling_log
        super().__init__(self.message)

    def prettyprint(self):
        print()
        print(self.message)
        print()
        print("Scheduling log:")
        print("---------------")
        print(self.scheduling_log)
        print("---------------")


def _is_scheduling_error(e: grpc.RpcError) -> bool:
    return e.details().startswith("failed to schedule launch:")


# TODO(geotho): return this structured from the backend.
def _grpc_error_to_clusterfudge_error(e: grpc.RpcError) -> SchedulingError:
    details = e.details() if hasattr(e, "details") else None
    detail_lines = details.splitlines() if details else []

    message = detail_lines[0] if detail_lines else ""

    for i, line in enumerate(detail_lines):
        if line.strip().startswith("Scheduling log:"):
            scheduling_log = "\n".join(detail_lines[i + 1 :])
            break

    return SchedulingError(message, scheduling_log)


def _proto_req_from_create_launch_request_v2(
    create_launch_request: CreateLaunchRequest,
) -> launches_pb2.CreateLaunchRequest:
    jobs = []
    for job in create_launch_request.jobs:
        processes = []
        for process in job.processes:
            processes.append(
                launches_pb2.Process(
                    command=process.command,
                    resource_requirements=_resources_to_proto(
                        process.resource_requirements
                    ),
                )
            )

        job_pb = launches_pb2.Job(
            short_name=job.short_name,
            replicas=job.replicas,
            processes=processes,
        )

        if job.replica_failure_behaviour is not None:
            if isinstance(
                job.replica_failure_behaviour, OnReplicaFailureOtherReplicasContinue
            ):
                job_pb.MergeFrom(
                    launches_pb2.Job(
                        on_replica_failure_other_replicas_continue=launches_pb2.OnReplicaFailureOtherReplicasContinue()
                    )
                )
            elif isinstance(
                job.replica_failure_behaviour, OnReplicaFailureOtherReplicasAreStopped
            ):
                job_pb.MergeFrom(
                    launches_pb2.Job(
                        on_replica_failure_other_replicas_are_stopped=launches_pb2.OnReplicaFailureOtherReplicasAreStopped()
                    )
                )
            else:
                raise ValueError(
                    f"Unknown replica failure behaviour: {job.replica_failure_behaviour}"
                )

        jobs.append(job_pb)

    proto_launch_request = launches_pb2.CreateLaunchRequest(
        title=create_launch_request.name,
        description=create_launch_request.description,
        cluster=create_launch_request.cluster,
        shard=create_launch_request.shard,
        hostnames=create_launch_request.hostnames,
        jobs=jobs,
    )

    if isinstance(create_launch_request.deployment, GitRepo):
        proto_launch_request.git_repo = create_launch_request.deployment.repo
        proto_launch_request.git_branch = create_launch_request.deployment.branch
        if create_launch_request.deployment.commit is not None:
            proto_launch_request.git_commit = create_launch_request.deployment.commit

    if create_launch_request.queueing_behaviour is not None:
        proto_launch_request.MergeFrom(
            launches_pb2.CreateLaunchRequest(
                queueing_behaviour=launches_pb2.QueueingBehaviour(
                    queue_launch=bool(
                        create_launch_request.queueing_behaviour.enqueue_if_cluster_busy
                    )
                )
            )
        )

    return proto_launch_request


class BetaClient:
    def __init__(self, channel: grpc.Channel):
        self.slurm_stub = slurm_pb2_grpc.SlurmStub(channel)

    def list_slurm_jobs(
        self, req: slurm_pb2.ListSlurmJobsRequest
    ) -> slurm_pb2.ListSlurmJobsResponse:
        return self.slurm_stub.ListSlurmJobs(req)


class Client:
    def __init__(self, base_url: str | None = None, api_key: str | None = None):
        self.base_url = base_url or "api.clusterfudge.com:443"
        self.api_key = api_key or self._load_config_from_file().token

        self.credentials = grpc.composite_channel_credentials(
            ssl_channel_credentials(),
            grpc.metadata_call_credentials(APIKeyCallCredentials(self.api_key)),
        )
        self.channel = grpc.secure_channel(self.base_url, self.credentials)
        self.async_channel = grpc.aio.secure_channel(self.base_url, self.credentials)
        self.launches_stub = launches_pb2_grpc.LaunchesStub(self.channel)
        self.tunnel_stub = tunnel_pb2_grpc.TunnelStub(self.async_channel)
        self.sandbox_stub = sandboxes_pb2_grpc.SandboxesStub(self.async_channel)
        self.beta = BetaClient(self.channel)

    def _load_config_from_file(self) -> ClusterfudgeConfig:
        config_path = os.path.join(
            os.path.expanduser("~"), ".clusterfudge", "config.json"
        )
        try:
            with open(config_path) as f:
                return ClusterfudgeConfig.from_json(f.read())
        except FileNotFoundError as e:
            raise RuntimeError(
                "Configuration file not found. Please run 'fudge login' to set up."
            ) from e
        except json.JSONDecodeError as e:
            raise RuntimeError(
                f"Configuration file {config_path} is not valid JSON. Please run 'fudge login' to set up."
            ) from e

    def create_launch(
        self, create_launch_request: CreateLaunchRequest
    ) -> launches_pb2.Launch:
        """Create a launch"""

        launch_script_body: str = ""
        stack = inspect.stack()
        caller_frame = stack[1]
        caller_file_path = caller_frame.filename
        try:
            with open(caller_file_path, "r") as file:
                launch_script_body = file.read()
        except FileNotFoundError:
            pass

        protoReq = None
        clr_v2 = create_launch_request

        _validate_create_launch_request_v2(clr_v2)
        protoReq = _proto_req_from_create_launch_request_v2(clr_v2)
        protoReq.launch_script_body = launch_script_body
        if create_launch_request.deployment is not None:
            if isinstance(create_launch_request.deployment, LocalDir):
                zipped_directory = _create_zip_file_of_project_contents_in_memory()
                zip_size = len(zipped_directory.getvalue())
                if zip_size > 50 * 1024 * 1024:
                    root = _project_root()
                    raise ValueError(
                        f"Launch specifies LocalDir deployment but project directory {root} is too large "
                        f"({zip_size / (1024 * 1024):.1f}MB). Maximum size is 50MB. "
                        "Ensure you have no large files (e.g. .venv, model weights, etc.) in your working directory. "
                        "You can also use a Git repository instead of a local directory."
                    )
                protoReq.zip_file_contents = zipped_directory.getvalue()

        try:
            return self.launches_stub.CreateLaunch(protoReq)
        except grpc.RpcError as e:
            status_code = e.code() if hasattr(e, "code") else None
            details = e.details() if hasattr(e, "details") else None
            if status_code == grpc.StatusCode.UNAUTHENTICATED:
                raise AuthenticationError(
                    e, details=details, status_code=status_code
                ) from None
            if _is_scheduling_error(e):
                raise _grpc_error_to_clusterfudge_error(e) from None
            raise e

    def launch_workstation(self) -> launches_pb2.LaunchWorkstationResponse:
        return self.launches_stub.LaunchWorkstation(
            launches_pb2.LaunchWorkstationRequest(
                port=22,
            )
        )

    def stop_launch(self, launch_id: str) -> None:
        self.launches_stub.StopLaunch(launches_pb2.StopLaunchRequest(id=launch_id))

    def get_launch_details(self, launch_id: str) -> launches_pb2.LaunchDetails:
        return self.launches_stub.GetLaunchDetails(
            launches_pb2.GetLaunchDetailsRequest(id=launch_id)
        )

    async def create_sandbox(self, params: Optional[SandboxParams] = None) -> str:
        """
        Create a new sandbox and wait for it to be ready.

        Args:
            sidecar_pod_definitions: Optional list of sidecar pod definitions
            image_tag: Optional custom image tag to use

        Returns:
            str: The ID of the created and ready-to-use sandbox

        Raises:
            TimeoutError: If the sandbox doesn't become ready within timeout
            Exception: If creation fails or sandbox enters failed state
        """

        sidecar_pod_definitions = []
        image_tag = ""
        if params:
            # Load the sidecar pod files if any are present
            sidecar_file_paths = params.sidecar_file_paths
            for sidecar_file_path in sidecar_file_paths or []:
                async with aiofiles.open(sidecar_file_path, "r") as f:
                    sidecar_pod_definitions.append(await f.read())
            image_tag = params.image_tag

        request = sandboxes_pb2.CreateSandboxRequest(
            sidecar_pod_definitions=sidecar_pod_definitions,
            image_tag=image_tag,
        )

        try:
            response = await self.sandbox_stub.CreateSandbox(request)
            if not response:
                raise Exception("failed to create sandbox - received empty response")

            sandbox_id = response.sandbox.id
            start_time = time.time()
            timeout = 360
            poll_interval = 1

            # Wait for the sandbox to be ready
            while True:
                if (time.time() - start_time) > timeout:
                    raise TimeoutError(
                        f"sandbox failed to start within {timeout} seconds"
                    )

                try:
                    response = await self.sandbox_stub.ListSandboxes(
                        sandboxes_pb2.ListSandboxesRequest()
                    )
                    for sandbox in response.sandboxes:
                        if sandbox.id == sandbox_id:
                            if (
                                sandbox.state
                                == sandboxes_pb2.Sandbox.STATE_RUNNING_HAPPILY
                            ):
                                return sandbox_id
                    await asyncio.sleep(poll_interval)
                except grpc.RpcError as e:
                    raise Exception(
                        f"failed to verify sandbox creation was successful: {e.details()}"
                    )

        except grpc.RpcError as e:
            raise Exception(f"failed to create sandbox: {e.details()}")

    async def claude_computer_use(
        self, sandbox_id: str, messages: list[BetaMessageParam]
    ) -> list[BetaMessageParam]:
        """
        Execute a Claude Computer Use operation.

        Args:
            sandbox_id: The ID of the Clusterfudge sandbox compute instance
            messages: All messages in the current Claude conversation

        Returns:
            list[BetaMessageParam]: All messages in the current Claude conversation, with any computer use actions performed appended

        Raises:
            Exception: If the operation fails
        """
        if not messages:
            return messages

        last_message = messages[-1]

        tool_use_requests: list[BetaToolUseBlockParam] = []
        for block in last_message.get("content"):
            if block["type"] == "tool_use":
                tool_use_requests.append(block)

        tool_use_results: list[BetaToolResultBlockParam] = []
        for block in tool_use_requests:
            try:
                response = await self.sandbox_stub.ClaudeComputerUse(
                    sandboxes_pb2.ClaudeComputerUseRequest(
                        machine_id=sandbox_id,
                        raw_anthropic_beta_content_block=json.dumps(block).encode(
                            "utf-8"
                        ),
                    )
                )
                computer_use_result = (
                    response.raw_anthropic_beta_tool_result_block.decode("utf-8")
                )
                tool_result = BetaToolResultBlockParam(
                    self._robust_json_decode(computer_use_result)
                )
                tool_use_results.append(tool_result)
            except grpc.RpcError as e:
                raise Exception(f"Failed to execute ClaudeComputerUse: {e.details()}")

        # If there are no tool_use blocks, return the original messages
        if not tool_use_results:
            return messages

        messages.append(BetaMessageParam(role="user", content=tool_use_results))

        return messages

    async def delete_sandbox(self, sandbox_id: str) -> None:
        """
        Delete a Clusterfudge sandbox instance.

        Args:
            sandbox_id: The ID of the Clusterfudge sandbox instance to delete

        Raises:
            Exception: If the deletion fails
        """

        try:
            await self.sandbox_stub.DeleteSandbox(
                sandboxes_pb2.DeleteSandboxRequest(machine_id=sandbox_id)
            )
        except grpc.RpcError as e:
            raise Exception(f"Failed to delete sandbox: {e.details()}")

    @staticmethod
    def _robust_json_decode(s: str) -> dict:
        """
        Robustly decode a JSON string that may contain invalid escape sequences.

        This function attempts multiple strategies:
        1. Direct JSON decoding
        2. Fixing common escape sequence issues
        3. Raw string interpretation
        4. Aggressive escape sequence cleaning

        Args:
            s: The string to decode

        Returns:
            The decoded JSON object

        Raises:
            JSONDecodeError: If all decoding attempts fail
        """
        # First try: direct decode
        try:
            return json.loads(s)
        except json.JSONDecodeError:
            pass

        # Second try: fix common escape sequence issues
        try:
            # Replace invalid escapes with proper ones
            fixed = re.sub(r'(?<!\\)\\(?!["\\/bfnrt])', r"\\\\", s)
            return json.loads(fixed)
        except json.JSONDecodeError:
            pass

        # Third try: treat as raw string
        try:
            # Convert to raw string representation
            raw_str = repr(s)[1:-1]
            return json.loads(raw_str)
        except json.JSONDecodeError:
            pass

        # Fourth try: aggressive cleanup
        try:
            # Remove all unescaped backslashes
            cleaned = re.sub(r'\\(?!["\\/bfnrt])', "", s)
            return json.loads(cleaned)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"All decoding attempts failed. Final error: {str(e)}", s, e.pos
            )


def _create_zip_file_of_project_contents_in_memory() -> io.BytesIO:
    folder = _project_root()
    if folder is None:
        raise ValueError("Could not find a project root")
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, folder))
    zip_buffer.seek(0)
    return zip_buffer


def _project_root() -> str | None:
    """Walk the directory tree to find the root of the project

    The root of the project is defined as the lowest folder that contains a
    .git, pyproject.toml, or requirements.txt."""
    current_dir = os.path.abspath(os.getcwd())
    while True:
        for f in [".git", "pyproject.toml", "requirements.txt"]:
            joined = os.path.join(current_dir, f)
            if os.path.exists(joined):
                print(f"Found {joined}")
                return current_dir
        current_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        if current_dir == os.path.abspath(os.sep):
            break

    return None


def _resources_to_proto(r: Resources | None) -> resources_pb2.Resources:
    if r is None:
        return resources_pb2.Resources()

    return resources_pb2.Resources(
        cpus=r.cpus,
        memory_mb=r.memory_mb,
        gpu_a100_40gb=r.a100_40gb,
        gpu_a100_80gb=r.a100_80gb,
        gpu_h100=r.h100,
        gpu_rtx3080=r.rtx3080,
        gpu_rtx3090=r.rtx3090,
        gpu_rtx6000=r.rtx6000,
        gpu_t4=r.t4,
        gpu_l4=r.l4,
        gpu_v100=r.v100,
        gpu_p4=r.p4,
        gpu_p100=r.p100,
        gpu_rtx4090=r.rtx4090,
        gpu_rtx4080=r.rtx4080,
        gpu_rtx3070=r.rtx3070,
        gpu_rtx3060=r.rtx3060,
        gpu_rtx4070=r.rtx4070,
        gpu_rtx4060=r.rtx4060,
        gpu_rtx3050=r.rtx3050,
        gpu_gtx1050=r.gtx1050,
        gpu_h200=r.h200,
    )


class AuthenticationError(Exception):
    """Exception raised for authentication failures"""

    def __init__(self, original_exception, details=None, status_code=None):
        self.original_exception = original_exception
        self.details = details
        self.status_code = status_code
        self.message = self.user_friendly_message()
        super().__init__(self.message)

    def user_friendly_message(self):
        base_message = "\n\nAuthentication failed. Please refresh your credentials with 'fudge login'."

        if self.details:
            base_message += f"\n\tDetails: {self.details}"

        if self.status_code:
            base_message += f"\n\tStatus code: {self.status_code}"

        return base_message
