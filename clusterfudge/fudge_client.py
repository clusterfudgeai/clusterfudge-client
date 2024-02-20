
import dataclasses
from sys import stderr
import dataclasses_json
import grpc
from grpc import ssl_channel_credentials

from proto.launches import launches_pb2_grpc
from proto.launches import launches_pb2

import json


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


class FudgeClient:
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
        try:
            with open("/Users/george/.clusterfudge/config.json") as f:
                return ClusterfudgeConfig.from_json(f.read())
        except FileNotFoundError:
            print(
                "No config file found at ~/.clusterfudge/config.json",
                file=stderr,
            )
            return ClusterfudgeConfig(token="")

    def create_launch(
        self, create_launch_request: launches_pb2.CreateLaunchRequest
    ) -> launches_pb2.Launch:
        return self.launches_stub.CreateLaunch(create_launch_request)