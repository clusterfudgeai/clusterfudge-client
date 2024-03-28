from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from resources import resources_pb2 as _resources_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

COMMAND_STATE_ACKNOWLEDGED: CommandState
COMMAND_STATE_CANCELLED: CommandState
COMMAND_STATE_FAILED: CommandState
COMMAND_STATE_KILLED: CommandState
COMMAND_STATE_RUNNING: CommandState
COMMAND_STATE_SUCCEEDED: CommandState
COMMAND_STATE_TIMED_OUT: CommandState
COMMAND_STATE_UNACKNOWLEDGED: CommandState
COMMAND_STATE_UNKNOWN: CommandState
COMMAND_TYPE_AGENT_UPDATE: CommandType
COMMAND_TYPE_KILL: CommandType
COMMAND_TYPE_LAUNCH: CommandType
COMMAND_TYPE_NVIDIA_BUG_REPORT: CommandType
COMMAND_TYPE_UNKNOWN: CommandType
DESCRIPTOR: _descriptor.FileDescriptor

class BulkCreateCommandRequest(_message.Message):
    __slots__ = ["command", "hostnames"]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    command: CommandType
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hostnames: _Optional[_Iterable[str]] = ..., command: _Optional[_Union[CommandType, str]] = ...) -> None: ...

class BulkCreateCommandResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Command(_message.Message):
    __slots__ = ["acknowledged_at", "cmd_line", "command", "env", "exec_err", "execution_completed_at", "execution_started_at", "exit_code", "git_branch", "git_repo", "hostname", "id", "job_name", "pid", "reference_id", "requested_at", "requested_by", "resource_request", "state", "tenant_id", "zip_id"]
    ACKNOWLEDGED_AT_FIELD_NUMBER: _ClassVar[int]
    CMD_LINE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    EXEC_ERR_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    GIT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    GIT_REPO_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ZIP_ID_FIELD_NUMBER: _ClassVar[int]
    acknowledged_at: _timestamp_pb2.Timestamp
    cmd_line: _containers.RepeatedScalarFieldContainer[str]
    command: CommandType
    env: _containers.RepeatedScalarFieldContainer[str]
    exec_err: str
    execution_completed_at: _timestamp_pb2.Timestamp
    execution_started_at: _timestamp_pb2.Timestamp
    exit_code: _wrappers_pb2.Int32Value
    git_branch: str
    git_repo: str
    hostname: str
    id: str
    job_name: str
    pid: _wrappers_pb2.Int32Value
    reference_id: str
    requested_at: _timestamp_pb2.Timestamp
    requested_by: str
    resource_request: _resources_pb2.Resources
    state: CommandState
    tenant_id: str
    zip_id: str
    def __init__(self, tenant_id: _Optional[str] = ..., hostname: _Optional[str] = ..., id: _Optional[str] = ..., requested_by: _Optional[str] = ..., requested_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledged_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., command: _Optional[_Union[CommandType, str]] = ..., env: _Optional[_Iterable[str]] = ..., reference_id: _Optional[str] = ..., execution_started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., execution_completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., exec_err: _Optional[str] = ..., exit_code: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., state: _Optional[_Union[CommandState, str]] = ..., pid: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., cmd_line: _Optional[_Iterable[str]] = ..., resource_request: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., zip_id: _Optional[str] = ..., git_repo: _Optional[str] = ..., git_branch: _Optional[str] = ..., job_name: _Optional[str] = ...) -> None: ...

class CommandResponse(_message.Message):
    __slots__ = ["command", "id", "reference_id", "requested_at"]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    command: CommandType
    id: str
    reference_id: str
    requested_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., requested_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., command: _Optional[_Union[CommandType, str]] = ..., reference_id: _Optional[str] = ...) -> None: ...

class CreateCommandRequest(_message.Message):
    __slots__ = ["command", "hostname", "reference_id"]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    command: CommandType
    hostname: str
    reference_id: str
    def __init__(self, hostname: _Optional[str] = ..., command: _Optional[_Union[CommandType, str]] = ..., reference_id: _Optional[str] = ...) -> None: ...

class CreateCommandResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetCommandRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListCommandsRequest(_message.Message):
    __slots__ = ["hostname", "hostnames", "reference_ids", "requested_by", "state", "states", "types"]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_IDS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    reference_ids: _containers.RepeatedScalarFieldContainer[str]
    requested_by: _containers.RepeatedScalarFieldContainer[str]
    state: CommandState
    states: _containers.RepeatedScalarFieldContainer[CommandState]
    types: _containers.RepeatedScalarFieldContainer[CommandType]
    def __init__(self, hostname: _Optional[str] = ..., state: _Optional[_Union[CommandState, str]] = ..., hostnames: _Optional[_Iterable[str]] = ..., states: _Optional[_Iterable[_Union[CommandState, str]]] = ..., types: _Optional[_Iterable[_Union[CommandType, str]]] = ..., reference_ids: _Optional[_Iterable[str]] = ..., requested_by: _Optional[_Iterable[str]] = ...) -> None: ...

class ListCommandsResponse(_message.Message):
    __slots__ = ["commands"]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[Command]
    def __init__(self, commands: _Optional[_Iterable[_Union[Command, _Mapping]]] = ...) -> None: ...

class UpdateCommandRequest(_message.Message):
    __slots__ = ["command"]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: Command
    def __init__(self, command: _Optional[_Union[Command, _Mapping]] = ...) -> None: ...

class CommandType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CommandState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
