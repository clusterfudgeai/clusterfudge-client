from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSandboxRequest(_message.Message):
    __slots__ = ("image_tag", "sidecar_pod_definitions", "display_name")
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    SIDECAR_POD_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    image_tag: str
    sidecar_pod_definitions: _containers.RepeatedScalarFieldContainer[str]
    display_name: str
    def __init__(self, image_tag: _Optional[str] = ..., sidecar_pod_definitions: _Optional[_Iterable[str]] = ..., display_name: _Optional[str] = ...) -> None: ...

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

class GetSandboxRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    def __init__(self, machine_id: _Optional[str] = ...) -> None: ...

class GetSandboxResponse(_message.Message):
    __slots__ = ("sandbox",)
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    sandbox: Sandbox
    def __init__(self, sandbox: _Optional[_Union[Sandbox, _Mapping]] = ...) -> None: ...

class Sandbox(_message.Message):
    __slots__ = ("id", "created_at", "state", "display_name", "created_by")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Sandbox.State]
        STATE_PENDING: _ClassVar[Sandbox.State]
        STATE_RUNNING_HAPPILY: _ClassVar[Sandbox.State]
        STATE_RUNNING_SADLY: _ClassVar[Sandbox.State]
        STATE_DELETED: _ClassVar[Sandbox.State]
    STATE_UNSPECIFIED: Sandbox.State
    STATE_PENDING: Sandbox.State
    STATE_RUNNING_HAPPILY: Sandbox.State
    STATE_RUNNING_SADLY: Sandbox.State
    STATE_DELETED: Sandbox.State
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    state: Sandbox.State
    display_name: str
    created_by: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[Sandbox.State, str]] = ..., display_name: _Optional[str] = ..., created_by: _Optional[str] = ...) -> None: ...

class ComputerUseRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    def __init__(self, machine_id: _Optional[str] = ...) -> None: ...

class ComputerUseResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

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

class ComputerUseRequestResponse(_message.Message):
    __slots__ = ("tenant_id", "user_id", "machine_id", "request_timestamp", "raw_request_contents", "response_timestamp", "raw_response_contents")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RAW_REQUEST_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RAW_RESPONSE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    user_id: str
    machine_id: str
    request_timestamp: _timestamp_pb2.Timestamp
    raw_request_contents: bytes
    response_timestamp: _timestamp_pb2.Timestamp
    raw_response_contents: bytes
    def __init__(self, tenant_id: _Optional[str] = ..., user_id: _Optional[str] = ..., machine_id: _Optional[str] = ..., request_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., raw_request_contents: _Optional[bytes] = ..., response_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., raw_response_contents: _Optional[bytes] = ...) -> None: ...

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

class GetComputerUseRequestLogsRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    def __init__(self, machine_id: _Optional[str] = ...) -> None: ...

class GetComputerUseRequestLogsResponse(_message.Message):
    __slots__ = ("logs",)
    LOGS_FIELD_NUMBER: _ClassVar[int]
    logs: _containers.RepeatedCompositeFieldContainer[ComputerUseRequestLog]
    def __init__(self, logs: _Optional[_Iterable[_Union[ComputerUseRequestLog, _Mapping]]] = ...) -> None: ...

class ComputerUseRequestLog(_message.Message):
    __slots__ = ("request_timestamp", "raw_request_contents", "response_timestamp", "raw_response_contents")
    REQUEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RAW_REQUEST_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RAW_RESPONSE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    request_timestamp: _timestamp_pb2.Timestamp
    raw_request_contents: bytes
    response_timestamp: _timestamp_pb2.Timestamp
    raw_response_contents: bytes
    def __init__(self, request_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., raw_request_contents: _Optional[bytes] = ..., response_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., raw_response_contents: _Optional[bytes] = ...) -> None: ...

class WriteToTerminalRequest(_message.Message):
    __slots__ = ("machine_id", "terminal_id", "input", "wait_for_response_ms")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_RESPONSE_MS_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    terminal_id: str
    input: bytes
    wait_for_response_ms: int
    def __init__(self, machine_id: _Optional[str] = ..., terminal_id: _Optional[str] = ..., input: _Optional[bytes] = ..., wait_for_response_ms: _Optional[int] = ...) -> None: ...

class WriteToTerminalResponse(_message.Message):
    __slots__ = ("stdout", "stderr", "exec_error")
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    EXEC_ERROR_FIELD_NUMBER: _ClassVar[int]
    stdout: bytes
    stderr: bytes
    exec_error: str
    def __init__(self, stdout: _Optional[bytes] = ..., stderr: _Optional[bytes] = ..., exec_error: _Optional[str] = ...) -> None: ...

class KillTerminalRequest(_message.Message):
    __slots__ = ("machine_id", "terminal_id")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    terminal_id: str
    def __init__(self, machine_id: _Optional[str] = ..., terminal_id: _Optional[str] = ...) -> None: ...

class KillTerminalResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str
    def __init__(self, success: bool = ..., error: _Optional[str] = ...) -> None: ...

class ResetTerminalRequest(_message.Message):
    __slots__ = ("machine_id", "terminal_id")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    terminal_id: str
    def __init__(self, machine_id: _Optional[str] = ..., terminal_id: _Optional[str] = ...) -> None: ...

class ResetTerminalResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str
    def __init__(self, success: bool = ..., error: _Optional[str] = ...) -> None: ...

class ResetAllTerminalsRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    def __init__(self, machine_id: _Optional[str] = ...) -> None: ...

class ResetAllTerminalsResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str
    def __init__(self, success: bool = ..., error: _Optional[str] = ...) -> None: ...

class GetTerminalHistoryRequest(_message.Message):
    __slots__ = ("machine_id", "terminal_id")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    terminal_id: str
    def __init__(self, machine_id: _Optional[str] = ..., terminal_id: _Optional[str] = ...) -> None: ...

class GetTerminalHistoryResponse(_message.Message):
    __slots__ = ("commands", "error")
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedScalarFieldContainer[str]
    error: str
    def __init__(self, commands: _Optional[_Iterable[str]] = ..., error: _Optional[str] = ...) -> None: ...
