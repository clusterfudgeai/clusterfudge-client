import dataclasses
import inspect
import json
import os
from collections.abc import Sequence

import dataclasses_json
import grpc
from grpc import ssl_channel_credentials

from clusterfudge_proto.launches import launches_pb2, launches_pb2_grpc
from clusterfudge_proto.resources import resources_pb2


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


@dataclasses.dataclass(kw_only=True)
class CreateLaunchRequest:
    command: Sequence[str]
    replicas: int
    name: str | None = None
    description: str | None = None
    replica_resources: Resources | None = None


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

        launch_script_contents: str = ""
        stack = inspect.stack()
        caller_frame = stack[1]
        caller_file_path = caller_frame.filename
        try:
            with open(caller_file_path, "r") as file:
                launch_script_contents = file.read()
        except FileNotFoundError:
            pass

        return self.launches_stub.CreateLaunch(
            launches_pb2.CreateLaunchRequest(
                # name=create_launch_request.name,
                # description=create_launch_request.description,
                command=create_launch_request.command,
                replicas=create_launch_request.replicas,
                replica_resources=_resources_to_proto(
                    create_launch_request.replica_resources
                ),
                # launch_script_contents=launch_script_contents,
            )
        )


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
    )
