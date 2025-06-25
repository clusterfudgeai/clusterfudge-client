from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from pagespb import pages_pb2 as _pages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClickAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLICK_ACTION_UNSPECIFIED: _ClassVar[ClickAction]
    CLICK_ACTION_LEFT_CLICK: _ClassVar[ClickAction]
    CLICK_ACTION_RIGHT_CLICK: _ClassVar[ClickAction]
    CLICK_ACTION_MIDDLE_CLICK: _ClassVar[ClickAction]
    CLICK_ACTION_DOUBLE_CLICK: _ClassVar[ClickAction]
    CLICK_ACTION_TRIPLE_CLICK: _ClassVar[ClickAction]

class ScrollDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCROLL_DIRECTION_UNSPECIFIED: _ClassVar[ScrollDirection]
    SCROLL_DIRECTION_UP: _ClassVar[ScrollDirection]
    SCROLL_DIRECTION_DOWN: _ClassVar[ScrollDirection]
    SCROLL_DIRECTION_LEFT: _ClassVar[ScrollDirection]
    SCROLL_DIRECTION_RIGHT: _ClassVar[ScrollDirection]

class SecurityRiskLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECURITY_RISK_LEVEL_UNSPECIFIED: _ClassVar[SecurityRiskLevel]
    SECURITY_RISK_LEVEL_NONE: _ClassVar[SecurityRiskLevel]
    SECURITY_RISK_LEVEL_LOW: _ClassVar[SecurityRiskLevel]
    SECURITY_RISK_LEVEL_MEDIUM: _ClassVar[SecurityRiskLevel]
    SECURITY_RISK_LEVEL_HIGH: _ClassVar[SecurityRiskLevel]
    SECURITY_RISK_LEVEL_CRITICAL: _ClassVar[SecurityRiskLevel]
CLICK_ACTION_UNSPECIFIED: ClickAction
CLICK_ACTION_LEFT_CLICK: ClickAction
CLICK_ACTION_RIGHT_CLICK: ClickAction
CLICK_ACTION_MIDDLE_CLICK: ClickAction
CLICK_ACTION_DOUBLE_CLICK: ClickAction
CLICK_ACTION_TRIPLE_CLICK: ClickAction
SCROLL_DIRECTION_UNSPECIFIED: ScrollDirection
SCROLL_DIRECTION_UP: ScrollDirection
SCROLL_DIRECTION_DOWN: ScrollDirection
SCROLL_DIRECTION_LEFT: ScrollDirection
SCROLL_DIRECTION_RIGHT: ScrollDirection
SECURITY_RISK_LEVEL_UNSPECIFIED: SecurityRiskLevel
SECURITY_RISK_LEVEL_NONE: SecurityRiskLevel
SECURITY_RISK_LEVEL_LOW: SecurityRiskLevel
SECURITY_RISK_LEVEL_MEDIUM: SecurityRiskLevel
SECURITY_RISK_LEVEL_HIGH: SecurityRiskLevel
SECURITY_RISK_LEVEL_CRITICAL: SecurityRiskLevel

class MintAuthTokenRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    def __init__(self, machine_id: _Optional[str] = ...) -> None: ...

class MintAuthTokenResponse(_message.Message):
    __slots__ = ("auth_token",)
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    auth_token: str
    def __init__(self, auth_token: _Optional[str] = ...) -> None: ...

class CreateSandboxRequest(_message.Message):
    __slots__ = ("image_tag", "sidecar_pod_definitions", "display_name", "config")
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    SIDECAR_POD_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    image_tag: str
    sidecar_pod_definitions: _containers.RepeatedScalarFieldContainer[str]
    display_name: str
    config: SandboxConfig
    def __init__(self, image_tag: _Optional[str] = ..., sidecar_pod_definitions: _Optional[_Iterable[str]] = ..., display_name: _Optional[str] = ..., config: _Optional[_Union[SandboxConfig, _Mapping]] = ...) -> None: ...

class SandboxConfig(_message.Message):
    __slots__ = ("sandboxlet",)
    SANDBOXLET_FIELD_NUMBER: _ClassVar[int]
    sandboxlet: SandboxletConfig
    def __init__(self, sandboxlet: _Optional[_Union[SandboxletConfig, _Mapping]] = ...) -> None: ...

class SandboxletConfig(_message.Message):
    __slots__ = ("proxied_paths", "screen_resolution")
    PROXIED_PATHS_FIELD_NUMBER: _ClassVar[int]
    SCREEN_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    proxied_paths: _containers.RepeatedCompositeFieldContainer[ProxiedPath]
    screen_resolution: ScreenResolution
    def __init__(self, proxied_paths: _Optional[_Iterable[_Union[ProxiedPath, _Mapping]]] = ..., screen_resolution: _Optional[_Union[ScreenResolution, _Mapping]] = ...) -> None: ...

class ScreenResolution(_message.Message):
    __slots__ = ("width", "height")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class ProxiedPath(_message.Message):
    __slots__ = ("incoming_path", "outgoing_port")
    INCOMING_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTGOING_PORT_FIELD_NUMBER: _ClassVar[int]
    incoming_path: str
    outgoing_port: int
    def __init__(self, incoming_path: _Optional[str] = ..., outgoing_port: _Optional[int] = ...) -> None: ...

class CreateSandboxResponse(_message.Message):
    __slots__ = ("sandbox",)
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    sandbox: Sandbox
    def __init__(self, sandbox: _Optional[_Union[Sandbox, _Mapping]] = ...) -> None: ...

class ListSandboxesRequest(_message.Message):
    __slots__ = ("page", "statuses")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    page: _pages_pb2.Page
    statuses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, page: _Optional[_Union[_pages_pb2.Page, _Mapping]] = ..., statuses: _Optional[_Iterable[str]] = ...) -> None: ...

class ListSandboxesResponse(_message.Message):
    __slots__ = ("sandboxes", "aggregates", "page_details")
    SANDBOXES_FIELD_NUMBER: _ClassVar[int]
    AGGREGATES_FIELD_NUMBER: _ClassVar[int]
    PAGE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    sandboxes: _containers.RepeatedCompositeFieldContainer[Sandbox]
    aggregates: SandboxAggregates
    page_details: _pages_pb2.PageDetails
    def __init__(self, sandboxes: _Optional[_Iterable[_Union[Sandbox, _Mapping]]] = ..., aggregates: _Optional[_Union[SandboxAggregates, _Mapping]] = ..., page_details: _Optional[_Union[_pages_pb2.PageDetails, _Mapping]] = ...) -> None: ...

class SandboxAggregates(_message.Message):
    __slots__ = ("total_sandboxes", "total_running_sandboxes", "total_sandbox_seconds")
    TOTAL_SANDBOXES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RUNNING_SANDBOXES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SANDBOX_SECONDS_FIELD_NUMBER: _ClassVar[int]
    total_sandboxes: int
    total_running_sandboxes: int
    total_sandbox_seconds: int
    def __init__(self, total_sandboxes: _Optional[int] = ..., total_running_sandboxes: _Optional[int] = ..., total_sandbox_seconds: _Optional[int] = ...) -> None: ...

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
    __slots__ = ("id", "created_at", "state", "display_name", "created_by", "image_tag", "ready_at", "updated_at", "deleted_at", "desired_state", "metadata_json", "summary", "short_summary", "security_summary")
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
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    READY_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DESIRED_STATE_FIELD_NUMBER: _ClassVar[int]
    METADATA_JSON_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SHORT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SECURITY_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    state: Sandbox.State
    display_name: str
    created_by: str
    image_tag: str
    ready_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    desired_state: str
    metadata_json: str
    summary: str
    short_summary: str
    security_summary: SecuritySummary
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[Sandbox.State, str]] = ..., display_name: _Optional[str] = ..., created_by: _Optional[str] = ..., image_tag: _Optional[str] = ..., ready_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., desired_state: _Optional[str] = ..., metadata_json: _Optional[str] = ..., summary: _Optional[str] = ..., short_summary: _Optional[str] = ..., security_summary: _Optional[_Union[SecuritySummary, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("tenant_id", "user_id", "machine_id", "request_timestamp", "raw_request_contents", "response_timestamp", "raw_response_contents", "method", "http_status_code")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RAW_REQUEST_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RAW_RESPONSE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    HTTP_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    user_id: str
    machine_id: str
    request_timestamp: _timestamp_pb2.Timestamp
    raw_request_contents: bytes
    response_timestamp: _timestamp_pb2.Timestamp
    raw_response_contents: bytes
    method: str
    http_status_code: int
    def __init__(self, tenant_id: _Optional[str] = ..., user_id: _Optional[str] = ..., machine_id: _Optional[str] = ..., request_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., raw_request_contents: _Optional[bytes] = ..., response_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., raw_response_contents: _Optional[bytes] = ..., method: _Optional[str] = ..., http_status_code: _Optional[int] = ...) -> None: ...

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
    __slots__ = ("request_timestamp", "raw_request_contents", "response_timestamp", "raw_response_contents", "method", "http_status_code")
    REQUEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RAW_REQUEST_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RAW_RESPONSE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    HTTP_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    request_timestamp: _timestamp_pb2.Timestamp
    raw_request_contents: bytes
    response_timestamp: _timestamp_pb2.Timestamp
    raw_response_contents: bytes
    method: str
    http_status_code: int
    def __init__(self, request_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., raw_request_contents: _Optional[bytes] = ..., response_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., raw_response_contents: _Optional[bytes] = ..., method: _Optional[str] = ..., http_status_code: _Optional[int] = ...) -> None: ...

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

class DownloadFileRequest(_message.Message):
    __slots__ = ("machine_id", "absolute_file_path")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    absolute_file_path: str
    def __init__(self, machine_id: _Optional[str] = ..., absolute_file_path: _Optional[str] = ...) -> None: ...

class DownloadFileResponse(_message.Message):
    __slots__ = ("contents", "sandbox_error")
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_ERROR_FIELD_NUMBER: _ClassVar[int]
    contents: bytes
    sandbox_error: str
    def __init__(self, contents: _Optional[bytes] = ..., sandbox_error: _Optional[str] = ...) -> None: ...

class DownloadFolderRequest(_message.Message):
    __slots__ = ("machine_id", "absolute_folder_path")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    absolute_folder_path: str
    def __init__(self, machine_id: _Optional[str] = ..., absolute_folder_path: _Optional[str] = ...) -> None: ...

class DownloadFolderResponse(_message.Message):
    __slots__ = ("zipped_contents", "sandbox_error")
    ZIPPED_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_ERROR_FIELD_NUMBER: _ClassVar[int]
    zipped_contents: bytes
    sandbox_error: str
    def __init__(self, zipped_contents: _Optional[bytes] = ..., sandbox_error: _Optional[str] = ...) -> None: ...

class CreateFileRequest(_message.Message):
    __slots__ = ("machine_id", "absolute_file_path", "contents", "overwrite_existing")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    absolute_file_path: str
    contents: bytes
    overwrite_existing: bool
    def __init__(self, machine_id: _Optional[str] = ..., absolute_file_path: _Optional[str] = ..., contents: _Optional[bytes] = ..., overwrite_existing: bool = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("sandbox_error",)
    SANDBOX_ERROR_FIELD_NUMBER: _ClassVar[int]
    sandbox_error: str
    def __init__(self, sandbox_error: _Optional[str] = ...) -> None: ...

class WriteToProcessRequest(_message.Message):
    __slots__ = ("machine_id", "process_id", "input", "wait_for_response_ms")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_RESPONSE_MS_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    process_id: str
    input: bytes
    wait_for_response_ms: int
    def __init__(self, machine_id: _Optional[str] = ..., process_id: _Optional[str] = ..., input: _Optional[bytes] = ..., wait_for_response_ms: _Optional[int] = ...) -> None: ...

class WriteToProcessResponse(_message.Message):
    __slots__ = ("stdin", "stdout", "stderr", "terminal_output", "process_error", "exit_code", "sandbox_error")
    STDIN_FIELD_NUMBER: _ClassVar[int]
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ERROR_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_ERROR_FIELD_NUMBER: _ClassVar[int]
    stdin: _containers.RepeatedScalarFieldContainer[bytes]
    stdout: bytes
    stderr: bytes
    terminal_output: bytes
    process_error: str
    exit_code: _wrappers_pb2.Int32Value
    sandbox_error: str
    def __init__(self, stdin: _Optional[_Iterable[bytes]] = ..., stdout: _Optional[bytes] = ..., stderr: _Optional[bytes] = ..., terminal_output: _Optional[bytes] = ..., process_error: _Optional[str] = ..., exit_code: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., sandbox_error: _Optional[str] = ...) -> None: ...

class KillProcessRequest(_message.Message):
    __slots__ = ("machine_id", "process_id")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    process_id: str
    def __init__(self, machine_id: _Optional[str] = ..., process_id: _Optional[str] = ...) -> None: ...

class KillProcessResponse(_message.Message):
    __slots__ = ("success", "sandbox_error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    sandbox_error: str
    def __init__(self, success: bool = ..., sandbox_error: _Optional[str] = ...) -> None: ...

class GetProcessRequest(_message.Message):
    __slots__ = ("machine_id", "process_id")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    process_id: str
    def __init__(self, machine_id: _Optional[str] = ..., process_id: _Optional[str] = ...) -> None: ...

class GetProcessResponse(_message.Message):
    __slots__ = ("stdin", "stdout", "stderr", "terminal_output", "process_error", "exit_code", "sandbox_error")
    STDIN_FIELD_NUMBER: _ClassVar[int]
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ERROR_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_ERROR_FIELD_NUMBER: _ClassVar[int]
    stdin: _containers.RepeatedScalarFieldContainer[bytes]
    stdout: bytes
    stderr: bytes
    terminal_output: bytes
    process_error: str
    exit_code: _wrappers_pb2.Int32Value
    sandbox_error: str
    def __init__(self, stdin: _Optional[_Iterable[bytes]] = ..., stdout: _Optional[bytes] = ..., stderr: _Optional[bytes] = ..., terminal_output: _Optional[bytes] = ..., process_error: _Optional[str] = ..., exit_code: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., sandbox_error: _Optional[str] = ...) -> None: ...

class ScreenshotRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    def __init__(self, machine_id: _Optional[str] = ...) -> None: ...

class ScreenshotResponse(_message.Message):
    __slots__ = ("image_data_base64", "error")
    IMAGE_DATA_BASE64_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    image_data_base64: bytes
    error: str
    def __init__(self, image_data_base64: _Optional[bytes] = ..., error: _Optional[str] = ...) -> None: ...

class KeyRequest(_message.Message):
    __slots__ = ("machine_id", "text")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    text: str
    def __init__(self, machine_id: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class KeyResponse(_message.Message):
    __slots__ = ("output", "error")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    output: str
    error: str
    def __init__(self, output: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class TypeRequest(_message.Message):
    __slots__ = ("machine_id", "text")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    text: str
    def __init__(self, machine_id: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class TypeResponse(_message.Message):
    __slots__ = ("output", "error")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    output: str
    error: str
    def __init__(self, output: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class MouseMoveRequest(_message.Message):
    __slots__ = ("machine_id", "x", "y")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    x: int
    y: int
    def __init__(self, machine_id: _Optional[str] = ..., x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class MouseMoveResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class LeftClickDragRequest(_message.Message):
    __slots__ = ("machine_id", "x", "y")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    x: int
    y: int
    def __init__(self, machine_id: _Optional[str] = ..., x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class LeftClickDragResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class CursorPositionRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    def __init__(self, machine_id: _Optional[str] = ...) -> None: ...

class CursorPositionResponse(_message.Message):
    __slots__ = ("x", "y", "error")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    error: str
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...

class ClickRequest(_message.Message):
    __slots__ = ("machine_id", "action", "x", "y", "key")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    action: ClickAction
    x: _wrappers_pb2.Int32Value
    y: _wrappers_pb2.Int32Value
    key: _wrappers_pb2.StringValue
    def __init__(self, machine_id: _Optional[str] = ..., action: _Optional[_Union[ClickAction, str]] = ..., x: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., y: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., key: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ClickResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class LeftMouseDownRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    def __init__(self, machine_id: _Optional[str] = ...) -> None: ...

class LeftMouseDownResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class LeftMouseUpRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    def __init__(self, machine_id: _Optional[str] = ...) -> None: ...

class LeftMouseUpResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class ScrollRequest(_message.Message):
    __slots__ = ("machine_id", "direction", "amount", "x", "y", "key")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    direction: ScrollDirection
    amount: int
    x: _wrappers_pb2.Int32Value
    y: _wrappers_pb2.Int32Value
    key: _wrappers_pb2.StringValue
    def __init__(self, machine_id: _Optional[str] = ..., direction: _Optional[_Union[ScrollDirection, str]] = ..., amount: _Optional[int] = ..., x: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., y: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., key: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ScrollResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class HoldKeyRequest(_message.Message):
    __slots__ = ("machine_id", "text", "duration_ms")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    text: str
    duration_ms: int
    def __init__(self, machine_id: _Optional[str] = ..., text: _Optional[str] = ..., duration_ms: _Optional[int] = ...) -> None: ...

class HoldKeyResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class WaitRequest(_message.Message):
    __slots__ = ("machine_id", "duration_ms")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    machine_id: str
    duration_ms: int
    def __init__(self, machine_id: _Optional[str] = ..., duration_ms: _Optional[int] = ...) -> None: ...

class WaitResponse(_message.Message):
    __slots__ = ("image_data_base64", "error")
    IMAGE_DATA_BASE64_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    image_data_base64: bytes
    error: str
    def __init__(self, image_data_base64: _Optional[bytes] = ..., error: _Optional[str] = ...) -> None: ...

class SecurityConcern(_message.Message):
    __slots__ = ("category", "risk_level", "description", "evidence", "recommendation", "technical_details")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    RISK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    TECHNICAL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    category: str
    risk_level: SecurityRiskLevel
    description: str
    evidence: _containers.RepeatedScalarFieldContainer[str]
    recommendation: str
    technical_details: str
    def __init__(self, category: _Optional[str] = ..., risk_level: _Optional[_Union[SecurityRiskLevel, str]] = ..., description: _Optional[str] = ..., evidence: _Optional[_Iterable[str]] = ..., recommendation: _Optional[str] = ..., technical_details: _Optional[str] = ...) -> None: ...

class SecuritySummaryMetadata(_message.Message):
    __slots__ = ("model_used", "processing_time_ms", "threat_categories_checked", "novel_threats_detected")
    MODEL_USED_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    THREAT_CATEGORIES_CHECKED_FIELD_NUMBER: _ClassVar[int]
    NOVEL_THREATS_DETECTED_FIELD_NUMBER: _ClassVar[int]
    model_used: str
    processing_time_ms: int
    threat_categories_checked: _containers.RepeatedScalarFieldContainer[str]
    novel_threats_detected: bool
    def __init__(self, model_used: _Optional[str] = ..., processing_time_ms: _Optional[int] = ..., threat_categories_checked: _Optional[_Iterable[str]] = ..., novel_threats_detected: bool = ...) -> None: ...

class SecuritySummary(_message.Message):
    __slots__ = ("overall_risk_level", "security_concerns", "summary", "generated_at", "interactions_count", "metadata")
    OVERALL_RISK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CONCERNS_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    INTERACTIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    overall_risk_level: SecurityRiskLevel
    security_concerns: _containers.RepeatedCompositeFieldContainer[SecurityConcern]
    summary: str
    generated_at: _timestamp_pb2.Timestamp
    interactions_count: int
    metadata: SecuritySummaryMetadata
    def __init__(self, overall_risk_level: _Optional[_Union[SecurityRiskLevel, str]] = ..., security_concerns: _Optional[_Iterable[_Union[SecurityConcern, _Mapping]]] = ..., summary: _Optional[str] = ..., generated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., interactions_count: _Optional[int] = ..., metadata: _Optional[_Union[SecuritySummaryMetadata, _Mapping]] = ...) -> None: ...
