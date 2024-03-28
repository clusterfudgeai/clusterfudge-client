import dataclasses
import inspect
import io
import json
import os
import zipfile
from collections.abc import Sequence
from typing import Optional

import dataclasses_json
import grpc
from clusterfudge_proto.launches import launches_pb2, launches_pb2_grpc
from clusterfudge_proto.resources import resources_pb2
from grpc import ssl_channel_credentials


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
    rtx3090: int = 0
    t4: int = 0


@dataclasses.dataclass(kw_only=True)
class LocalDir:
    pass


@dataclasses.dataclass(kw_only=True)
class GitRepo:
    repo: str
    branch: str


@dataclasses.dataclass(kw_only=True)
class Process:
    command: Sequence[str]
    resource_requirements: Optional[Resources] = None


@dataclasses.dataclass(kw_only=True)
class Job:
    short_name: str
    replicas: int
    processes: Sequence[Process]


@dataclasses.dataclass(kw_only=True)
class CreateLaunchRequest:
    name: Optional[str] = None
    description: Optional[str] = None
    deployment: Optional[LocalDir | GitRepo] = None
    jobs: Sequence[Job]


def _validate_create_launch_request_v2(
    create_launch_request: CreateLaunchRequest,
) -> None:
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

        jobs.append(
            launches_pb2.Job(
                short_name=job.short_name,
                replicas=job.replicas,
                processes=processes,
            )
        )

    return launches_pb2.CreateLaunchRequest(
        title=create_launch_request.name,
        description=create_launch_request.description,
        jobs=jobs,
    )


class Client:
    def __init__(self, base_url: str | None = None, api_key: str | None = None):
        self.base_url = base_url or "api.clusterfudge.com:443"
        self.api_key = api_key or self._load_config_from_file().token

        self.credentials = grpc.composite_channel_credentials(
            ssl_channel_credentials(),
            grpc.metadata_call_credentials(APIKeyCallCredentials(self.api_key)),
        )
        self.channel = grpc.secure_channel(self.base_url, self.credentials)
        self.launches_stub = launches_pb2_grpc.LaunchesStub(self.channel)

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
                protoReq.zip_file_contents = zipped_directory.getvalue()
            elif isinstance(create_launch_request.deployment, GitRepo):
                protoReq.git_repo = create_launch_request.deployment.repo
                protoReq.git_branch = create_launch_request.deployment.branch
            else:
                raise ValueError(
                    f"Unknown deployment type: {create_launch_request.deployment}"
                )

        return self.launches_stub.CreateLaunch(protoReq)


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
        gpu_rtx3090=r.rtx3090,
        gpu_t4=r.t4,
    )
