from google.protobuf import timestamp_pb2 as _timestamp_pb2
from resources import resources_pb2 as _resources_pb2
from exec import exec_pb2 as _exec_pb2
from logs import logs_pb2 as _logs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterResources(_message.Message):
    __slots__ = ["available_resources", "name", "total_resources", "used_resources"]
    AVAILABLE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    USED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    available_resources: _resources_pb2.Resources
    name: str
    total_resources: _resources_pb2.Resources
    used_resources: _resources_pb2.Resources
    def __init__(self, name: _Optional[str] = ..., total_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., used_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., available_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ...) -> None: ...

class CreateLaunchRequest(_message.Message):
    __slots__ = ["command", "command_to_run", "description", "hostnames", "launch_script_body", "launched_by", "replica_resources", "replicas", "title"]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TO_RUN_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    LAUNCHED_BY_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_SCRIPT_BODY_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    REPLICA_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    command: _containers.RepeatedScalarFieldContainer[str]
    command_to_run: str
    description: str
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    launch_script_body: str
    launched_by: str
    replica_resources: _resources_pb2.Resources
    replicas: int
    title: str
    def __init__(self, launched_by: _Optional[str] = ..., command_to_run: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., hostnames: _Optional[_Iterable[str]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., replicas: _Optional[int] = ..., replica_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., launch_script_body: _Optional[str] = ...) -> None: ...

class GetLaunchDetailsRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetLaunchRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Launch(_message.Message):
    __slots__ = ["command", "command_to_run", "description", "hostnames", "id", "launch_id", "launch_script_body", "launched_by", "replica_resources", "replicas", "scheduling_log", "status", "submitted_at", "title"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TO_RUN_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCHED_BY_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_SCRIPT_BODY_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_STATUS_COMPLETED: Launch.Status
    LAUNCH_STATUS_FAILED: Launch.Status
    LAUNCH_STATUS_PENDING: Launch.Status
    LAUNCH_STATUS_RUNNING: Launch.Status
    LAUNCH_STATUS_STOPPED: Launch.Status
    LAUNCH_STATUS_UNKNOWN: Launch.Status
    LAUNCH_STATUS_UNMANAGED: Launch.Status
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    REPLICA_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_LOG_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    command: _containers.RepeatedScalarFieldContainer[str]
    command_to_run: str
    description: str
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    id: str
    launch_id: int
    launch_script_body: str
    launched_by: str
    replica_resources: _resources_pb2.Resources
    replicas: int
    scheduling_log: _containers.RepeatedScalarFieldContainer[str]
    status: Launch.Status
    submitted_at: _timestamp_pb2.Timestamp
    title: str
    def __init__(self, launch_id: _Optional[int] = ..., launched_by: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., command_to_run: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., hostnames: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[Launch.Status, str]] = ..., id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., replicas: _Optional[int] = ..., replica_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., launch_script_body: _Optional[str] = ..., scheduling_log: _Optional[_Iterable[str]] = ...) -> None: ...

class LaunchDetails(_message.Message):
    __slots__ = ["commands", "launch", "logs", "xids"]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    XIDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[_exec_pb2.Command]
    launch: Launch
    logs: _containers.RepeatedCompositeFieldContainer[_logs_pb2.Log]
    xids: _containers.RepeatedCompositeFieldContainer[Xid]
    def __init__(self, launch: _Optional[_Union[Launch, _Mapping]] = ..., commands: _Optional[_Iterable[_Union[_exec_pb2.Command, _Mapping]]] = ..., xids: _Optional[_Iterable[_Union[Xid, _Mapping]]] = ..., logs: _Optional[_Iterable[_Union[_logs_pb2.Log, _Mapping]]] = ...) -> None: ...

class LaunchWithCommandStatuses(_message.Message):
    __slots__ = ["commands_acknowledged_count", "commands_cancelled_count", "commands_failed_count", "commands_killed_count", "commands_running_count", "commands_succeeded_count", "commands_total_count", "commands_unacknowledged_count", "commands_unknown_count", "launch"]
    COMMANDS_ACKNOWLEDGED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_CANCELLED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_KILLED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_RUNNING_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_SUCCEEDED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_UNACKNOWLEDGED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_UNKNOWN_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_FIELD_NUMBER: _ClassVar[int]
    commands_acknowledged_count: int
    commands_cancelled_count: int
    commands_failed_count: int
    commands_killed_count: int
    commands_running_count: int
    commands_succeeded_count: int
    commands_total_count: int
    commands_unacknowledged_count: int
    commands_unknown_count: int
    launch: Launch
    def __init__(self, launch: _Optional[_Union[Launch, _Mapping]] = ..., commands_unknown_count: _Optional[int] = ..., commands_unacknowledged_count: _Optional[int] = ..., commands_acknowledged_count: _Optional[int] = ..., commands_running_count: _Optional[int] = ..., commands_succeeded_count: _Optional[int] = ..., commands_failed_count: _Optional[int] = ..., commands_killed_count: _Optional[int] = ..., commands_cancelled_count: _Optional[int] = ..., commands_total_count: _Optional[int] = ...) -> None: ...

class ListLaunchesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListLaunchesResponse(_message.Message):
    __slots__ = ["launches"]
    LAUNCHES_FIELD_NUMBER: _ClassVar[int]
    launches: _containers.RepeatedCompositeFieldContainer[Launch]
    def __init__(self, launches: _Optional[_Iterable[_Union[Launch, _Mapping]]] = ...) -> None: ...

class ListLaunchesWithCommandStatusesResponse(_message.Message):
    __slots__ = ["launches"]
    LAUNCHES_FIELD_NUMBER: _ClassVar[int]
    launches: _containers.RepeatedCompositeFieldContainer[LaunchWithCommandStatuses]
    def __init__(self, launches: _Optional[_Iterable[_Union[LaunchWithCommandStatuses, _Mapping]]] = ...) -> None: ...

class ListResourcesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListResourcesResponse(_message.Message):
    __slots__ = ["clusters", "resource_consumers"]
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[ClusterResources]
    resource_consumers: _containers.RepeatedCompositeFieldContainer[_exec_pb2.Command]
    def __init__(self, clusters: _Optional[_Iterable[_Union[ClusterResources, _Mapping]]] = ..., resource_consumers: _Optional[_Iterable[_Union[_exec_pb2.Command, _Mapping]]] = ...) -> None: ...

class StopLaunchRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class StopLaunchResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Xid(_message.Message):
    __slots__ = ["gpu_uuid", "hostname", "occurred_at", "pci_id", "xid"]
    GPU_UUID_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    PCI_ID_FIELD_NUMBER: _ClassVar[int]
    XID_FIELD_NUMBER: _ClassVar[int]
    gpu_uuid: str
    hostname: str
    occurred_at: _timestamp_pb2.Timestamp
    pci_id: str
    xid: int
    def __init__(self, hostname: _Optional[str] = ..., gpu_uuid: _Optional[str] = ..., pci_id: _Optional[str] = ..., xid: _Optional[int] = ..., occurred_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
