from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from resources import resources_pb2 as _resources_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommandType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMAND_TYPE_UNKNOWN: _ClassVar[CommandType]
    COMMAND_TYPE_AGENT_UPDATE: _ClassVar[CommandType]
    COMMAND_TYPE_NVIDIA_BUG_REPORT: _ClassVar[CommandType]
    COMMAND_TYPE_LAUNCH: _ClassVar[CommandType]
    COMMAND_TYPE_KILL: _ClassVar[CommandType]
    COMMAND_TYPE_STREAM_LOGS: _ClassVar[CommandType]
    COMMAND_TYPE_STREAM_TCP: _ClassVar[CommandType]
    COMMAND_TYPE_SCANCEL: _ClassVar[CommandType]
    COMMAND_TYPE_JUPYTER_LAUNCH: _ClassVar[CommandType]
    COMMAND_TYPE_SBATCH: _ClassVar[CommandType]

class CommandState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMAND_STATE_UNKNOWN: _ClassVar[CommandState]
    COMMAND_STATE_UNACKNOWLEDGED: _ClassVar[CommandState]
    COMMAND_STATE_ACKNOWLEDGED: _ClassVar[CommandState]
    COMMAND_STATE_RUNNING: _ClassVar[CommandState]
    COMMAND_STATE_SUCCEEDED: _ClassVar[CommandState]
    COMMAND_STATE_FAILED: _ClassVar[CommandState]
    COMMAND_STATE_KILLED: _ClassVar[CommandState]
    COMMAND_STATE_CANCELLED: _ClassVar[CommandState]
    COMMAND_STATE_TIMED_OUT: _ClassVar[CommandState]

class NodeExclusivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_EXCLUSIVITY_UNKNOWN: _ClassVar[NodeExclusivity]
    NODE_EXCLUSIVITY_SHARE_NODE: _ClassVar[NodeExclusivity]
    NODE_EXCLUSIVITY_REQUIRE_ENTIRE_NODE: _ClassVar[NodeExclusivity]
COMMAND_TYPE_UNKNOWN: CommandType
COMMAND_TYPE_AGENT_UPDATE: CommandType
COMMAND_TYPE_NVIDIA_BUG_REPORT: CommandType
COMMAND_TYPE_LAUNCH: CommandType
COMMAND_TYPE_KILL: CommandType
COMMAND_TYPE_STREAM_LOGS: CommandType
COMMAND_TYPE_STREAM_TCP: CommandType
COMMAND_TYPE_SCANCEL: CommandType
COMMAND_TYPE_JUPYTER_LAUNCH: CommandType
COMMAND_TYPE_SBATCH: CommandType
COMMAND_STATE_UNKNOWN: CommandState
COMMAND_STATE_UNACKNOWLEDGED: CommandState
COMMAND_STATE_ACKNOWLEDGED: CommandState
COMMAND_STATE_RUNNING: CommandState
COMMAND_STATE_SUCCEEDED: CommandState
COMMAND_STATE_FAILED: CommandState
COMMAND_STATE_KILLED: CommandState
COMMAND_STATE_CANCELLED: CommandState
COMMAND_STATE_TIMED_OUT: CommandState
NODE_EXCLUSIVITY_UNKNOWN: NodeExclusivity
NODE_EXCLUSIVITY_SHARE_NODE: NodeExclusivity
NODE_EXCLUSIVITY_REQUIRE_ENTIRE_NODE: NodeExclusivity

class CommandResponse(_message.Message):
    __slots__ = ("id", "requested_at", "command", "reference_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    requested_at: _timestamp_pb2.Timestamp
    command: CommandType
    reference_id: str
    def __init__(self, id: _Optional[str] = ..., requested_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., command: _Optional[_Union[CommandType, str]] = ..., reference_id: _Optional[str] = ...) -> None: ...

class GetCommandRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CreateCommandRequest(_message.Message):
    __slots__ = ("hostname", "command", "reference_id")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    command: CommandType
    reference_id: str
    def __init__(self, hostname: _Optional[str] = ..., command: _Optional[_Union[CommandType, str]] = ..., reference_id: _Optional[str] = ...) -> None: ...

class CreateCommandResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkCreateCommandRequest(_message.Message):
    __slots__ = ("hostnames", "command")
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    command: CommandType
    def __init__(self, hostnames: _Optional[_Iterable[str]] = ..., command: _Optional[_Union[CommandType, str]] = ...) -> None: ...

class BulkCreateCommandResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCommandsRequest(_message.Message):
    __slots__ = ("hostname", "state", "hostnames", "states", "types", "reference_ids", "requested_by")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_IDS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    state: CommandState
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    states: _containers.RepeatedScalarFieldContainer[CommandState]
    types: _containers.RepeatedScalarFieldContainer[CommandType]
    reference_ids: _containers.RepeatedScalarFieldContainer[str]
    requested_by: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hostname: _Optional[str] = ..., state: _Optional[_Union[CommandState, str]] = ..., hostnames: _Optional[_Iterable[str]] = ..., states: _Optional[_Iterable[_Union[CommandState, str]]] = ..., types: _Optional[_Iterable[_Union[CommandType, str]]] = ..., reference_ids: _Optional[_Iterable[str]] = ..., requested_by: _Optional[_Iterable[str]] = ...) -> None: ...

class ListCommandsResponse(_message.Message):
    __slots__ = ("commands",)
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[Command]
    def __init__(self, commands: _Optional[_Iterable[_Union[Command, _Mapping]]] = ...) -> None: ...

class UpdateCommandRequest(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: Command
    def __init__(self, command: _Optional[_Union[Command, _Mapping]] = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ("tenant_id", "hostname", "id", "requested_by", "requested_at", "acknowledged_at", "command", "reference_id", "execution_started_at", "execution_completed_at", "exec_err", "exit_code", "state", "env", "pid", "cmd_line", "resource_request", "zip_id", "git_repo", "git_branch", "job_name", "server_state", "git_commit", "node_exclusivity", "command_options")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGED_AT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    EXEC_ERR_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    CMD_LINE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ZIP_ID_FIELD_NUMBER: _ClassVar[int]
    GIT_REPO_FIELD_NUMBER: _ClassVar[int]
    GIT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_STATE_FIELD_NUMBER: _ClassVar[int]
    GIT_COMMIT_FIELD_NUMBER: _ClassVar[int]
    NODE_EXCLUSIVITY_FIELD_NUMBER: _ClassVar[int]
    COMMAND_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    hostname: str
    id: str
    requested_by: str
    requested_at: _timestamp_pb2.Timestamp
    acknowledged_at: _timestamp_pb2.Timestamp
    command: CommandType
    reference_id: str
    execution_started_at: _timestamp_pb2.Timestamp
    execution_completed_at: _timestamp_pb2.Timestamp
    exec_err: str
    exit_code: _wrappers_pb2.Int32Value
    state: CommandState
    env: _containers.RepeatedScalarFieldContainer[str]
    pid: _wrappers_pb2.Int32Value
    cmd_line: _containers.RepeatedScalarFieldContainer[str]
    resource_request: _resources_pb2.Resources
    zip_id: str
    git_repo: str
    git_branch: str
    job_name: str
    server_state: CommandState
    git_commit: str
    node_exclusivity: NodeExclusivity
    command_options: CommandOptions
    def __init__(self, tenant_id: _Optional[str] = ..., hostname: _Optional[str] = ..., id: _Optional[str] = ..., requested_by: _Optional[str] = ..., requested_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., acknowledged_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., command: _Optional[_Union[CommandType, str]] = ..., reference_id: _Optional[str] = ..., execution_started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., execution_completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., exec_err: _Optional[str] = ..., exit_code: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., state: _Optional[_Union[CommandState, str]] = ..., env: _Optional[_Iterable[str]] = ..., pid: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., cmd_line: _Optional[_Iterable[str]] = ..., resource_request: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., zip_id: _Optional[str] = ..., git_repo: _Optional[str] = ..., git_branch: _Optional[str] = ..., job_name: _Optional[str] = ..., server_state: _Optional[_Union[CommandState, str]] = ..., git_commit: _Optional[str] = ..., node_exclusivity: _Optional[_Union[NodeExclusivity, str]] = ..., command_options: _Optional[_Union[CommandOptions, _Mapping]] = ...) -> None: ...

class CommandOptions(_message.Message):
    __slots__ = ("scancel", "jupyter_launch", "sbatch")
    SCANCEL_FIELD_NUMBER: _ClassVar[int]
    JUPYTER_LAUNCH_FIELD_NUMBER: _ClassVar[int]
    SBATCH_FIELD_NUMBER: _ClassVar[int]
    scancel: ScancelOptions
    jupyter_launch: JupyterLaunchOptions
    sbatch: SbatchOptions
    def __init__(self, scancel: _Optional[_Union[ScancelOptions, _Mapping]] = ..., jupyter_launch: _Optional[_Union[JupyterLaunchOptions, _Mapping]] = ..., sbatch: _Optional[_Union[SbatchOptions, _Mapping]] = ...) -> None: ...

class ScancelOptions(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class JupyterLaunchOptions(_message.Message):
    __slots__ = ("virtual_env_path", "gpu_per_node", "output_file", "nvidia_config")
    VIRTUAL_ENV_PATH_FIELD_NUMBER: _ClassVar[int]
    GPU_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FILE_FIELD_NUMBER: _ClassVar[int]
    NVIDIA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    virtual_env_path: str
    gpu_per_node: int
    output_file: str
    nvidia_config: NvidiaConfig
    def __init__(self, virtual_env_path: _Optional[str] = ..., gpu_per_node: _Optional[int] = ..., output_file: _Optional[str] = ..., nvidia_config: _Optional[_Union[NvidiaConfig, _Mapping]] = ...) -> None: ...

class SbatchOptions(_message.Message):
    __slots__ = ("script_path", "unix_user", "env_vars", "args", "sbatch_content")
    SCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    UNIX_USER_FIELD_NUMBER: _ClassVar[int]
    ENV_VARS_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    SBATCH_CONTENT_FIELD_NUMBER: _ClassVar[int]
    script_path: str
    unix_user: str
    env_vars: _containers.RepeatedCompositeFieldContainer[EnvironmentVariable]
    args: _containers.RepeatedScalarFieldContainer[str]
    sbatch_content: str
    def __init__(self, script_path: _Optional[str] = ..., unix_user: _Optional[str] = ..., env_vars: _Optional[_Iterable[_Union[EnvironmentVariable, _Mapping]]] = ..., args: _Optional[_Iterable[str]] = ..., sbatch_content: _Optional[str] = ...) -> None: ...

class EnvironmentVariable(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class NvidiaConfig(_message.Message):
    __slots__ = ("nccl_socket_if_name", "nccl_ib_hca", "ucx_net_devices", "sharp_coll_enable_pci_relaxed_ordering", "nccl_collnet_enable", "ld_library_path")
    NCCL_SOCKET_IF_NAME_FIELD_NUMBER: _ClassVar[int]
    NCCL_IB_HCA_FIELD_NUMBER: _ClassVar[int]
    UCX_NET_DEVICES_FIELD_NUMBER: _ClassVar[int]
    SHARP_COLL_ENABLE_PCI_RELAXED_ORDERING_FIELD_NUMBER: _ClassVar[int]
    NCCL_COLLNET_ENABLE_FIELD_NUMBER: _ClassVar[int]
    LD_LIBRARY_PATH_FIELD_NUMBER: _ClassVar[int]
    nccl_socket_if_name: str
    nccl_ib_hca: str
    ucx_net_devices: str
    sharp_coll_enable_pci_relaxed_ordering: int
    nccl_collnet_enable: int
    ld_library_path: str
    def __init__(self, nccl_socket_if_name: _Optional[str] = ..., nccl_ib_hca: _Optional[str] = ..., ucx_net_devices: _Optional[str] = ..., sharp_coll_enable_pci_relaxed_ordering: _Optional[int] = ..., nccl_collnet_enable: _Optional[int] = ..., ld_library_path: _Optional[str] = ...) -> None: ...
