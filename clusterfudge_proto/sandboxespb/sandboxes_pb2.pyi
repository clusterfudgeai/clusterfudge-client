from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSandboxRequest(_message.Message):
    __slots__ = ("image_tag", "sidecar_pod_definitions")
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    SIDECAR_POD_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    image_tag: str
    sidecar_pod_definitions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, image_tag: _Optional[str] = ..., sidecar_pod_definitions: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateSandboxResponse(_message.Message):
    __slots__ = ("sandbox",)
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    sandbox: Sandbox
    def __init__(self, sandbox: _Optional[_Union[Sandbox, _Mapping]] = ...) -> None: ...

class ListSandboxesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSandboxesResponse(_message.Message):
    __slots__ = ("sandboxes",)
    SANDBOXES_FIELD_NUMBER: _ClassVar[int]
    sandboxes: _containers.RepeatedCompositeFieldContainer[Sandbox]
    def __init__(self, sandboxes: _Optional[_Iterable[_Union[Sandbox, _Mapping]]] = ...) -> None: ...

class DeleteSandboxRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    def __init__(self, machine_id: _Optional[str] = ...) -> None: ...

class DeleteSandboxResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Sandbox(_message.Message):
    __slots__ = ("id", "created_at", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Sandbox.State]
        STATE_PENDING: _ClassVar[Sandbox.State]
        STATE_RUNNING_HAPPILY: _ClassVar[Sandbox.State]
        STATE_RUNNING_SADLY: _ClassVar[Sandbox.State]
    STATE_UNSPECIFIED: Sandbox.State
    STATE_PENDING: Sandbox.State
    STATE_RUNNING_HAPPILY: Sandbox.State
    STATE_RUNNING_SADLY: Sandbox.State
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    state: Sandbox.State
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[Sandbox.State, str]] = ...) -> None: ...

class ClaudeComputerUseRequest(_message.Message):
    __slots__ = ("machine_id", "raw_anthropic_beta_content_block")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    RAW_ANTHROPIC_BETA_CONTENT_BLOCK_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    raw_anthropic_beta_content_block: bytes
    def __init__(self, machine_id: _Optional[str] = ..., raw_anthropic_beta_content_block: _Optional[bytes] = ...) -> None: ...

class ClaudeComputerUseResponse(_message.Message):
    __slots__ = ("raw_anthropic_beta_tool_result_block",)
    RAW_ANTHROPIC_BETA_TOOL_RESULT_BLOCK_FIELD_NUMBER: _ClassVar[int]
    raw_anthropic_beta_tool_result_block: bytes
    def __init__(self, raw_anthropic_beta_tool_result_block: _Optional[bytes] = ...) -> None: ...

class ClaudeComputerUseRequestResponse(_message.Message):
    __slots__ = ("tenant_id", "user_id", "machine_id", "request_timestamp", "raw_anthropic_beta_content_block", "response_timestamp", "raw_anthropic_beta_tool_result_block")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RAW_ANTHROPIC_BETA_CONTENT_BLOCK_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RAW_ANTHROPIC_BETA_TOOL_RESULT_BLOCK_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    user_id: str
    machine_id: str
    request_timestamp: _timestamp_pb2.Timestamp
    raw_anthropic_beta_content_block: bytes
    response_timestamp: _timestamp_pb2.Timestamp
    raw_anthropic_beta_tool_result_block: bytes
    def __init__(self, tenant_id: _Optional[str] = ..., user_id: _Optional[str] = ..., machine_id: _Optional[str] = ..., request_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., raw_anthropic_beta_content_block: _Optional[bytes] = ..., response_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., raw_anthropic_beta_tool_result_block: _Optional[bytes] = ...) -> None: ...
