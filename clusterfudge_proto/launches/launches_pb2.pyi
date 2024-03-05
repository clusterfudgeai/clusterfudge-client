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

class ListResourcesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListResourcesResponse(_message.Message):
    __slots__ = ("clusters", "resource_consumers")
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[ClusterResources]
    resource_consumers: _containers.RepeatedCompositeFieldContainer[_exec_pb2.Command]
    def __init__(self, clusters: _Optional[_Iterable[_Union[ClusterResources, _Mapping]]] = ..., resource_consumers: _Optional[_Iterable[_Union[_exec_pb2.Command, _Mapping]]] = ...) -> None: ...

class ClusterResources(_message.Message):
    __slots__ = ("name", "total_resources", "used_resources", "available_resources")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    USED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    total_resources: _resources_pb2.Resources
    used_resources: _resources_pb2.Resources
    available_resources: _resources_pb2.Resources
    def __init__(self, name: _Optional[str] = ..., total_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., used_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., available_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ...) -> None: ...

class GetLaunchRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetLaunchDetailsRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListLaunchesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLaunchesResponse(_message.Message):
    __slots__ = ("launches",)
    LAUNCHES_FIELD_NUMBER: _ClassVar[int]
    launches: _containers.RepeatedCompositeFieldContainer[Launch]
    def __init__(self, launches: _Optional[_Iterable[_Union[Launch, _Mapping]]] = ...) -> None: ...

class StopLaunchRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class StopLaunchResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Launch(_message.Message):
    __slots__ = ("launch_id", "launched_by", "submitted_at", "command_to_run", "command", "hostnames", "status", "id", "title", "description", "replicas", "replica_resources")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LAUNCH_STATUS_UNKNOWN: _ClassVar[Launch.Status]
        LAUNCH_STATUS_PENDING: _ClassVar[Launch.Status]
        LAUNCH_STATUS_RUNNING: _ClassVar[Launch.Status]
        LAUNCH_STATUS_COMPLETED: _ClassVar[Launch.Status]
        LAUNCH_STATUS_FAILED: _ClassVar[Launch.Status]
        LAUNCH_STATUS_UNMANAGED: _ClassVar[Launch.Status]
        LAUNCH_STATUS_STOPPED: _ClassVar[Launch.Status]
    LAUNCH_STATUS_UNKNOWN: Launch.Status
    LAUNCH_STATUS_PENDING: Launch.Status
    LAUNCH_STATUS_RUNNING: Launch.Status
    LAUNCH_STATUS_COMPLETED: Launch.Status
    LAUNCH_STATUS_FAILED: Launch.Status
    LAUNCH_STATUS_UNMANAGED: Launch.Status
    LAUNCH_STATUS_STOPPED: Launch.Status
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCHED_BY_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TO_RUN_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    REPLICA_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    launch_id: int
    launched_by: str
    submitted_at: _timestamp_pb2.Timestamp
    command_to_run: str
    command: _containers.RepeatedScalarFieldContainer[str]
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    status: Launch.Status
    id: str
    title: str
    description: str
    replicas: int
    replica_resources: _resources_pb2.Resources
    def __init__(self, launch_id: _Optional[int] = ..., launched_by: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., command_to_run: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., hostnames: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[Launch.Status, str]] = ..., id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., replicas: _Optional[int] = ..., replica_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ...) -> None: ...

class ListLaunchesWithCommandStatusesResponse(_message.Message):
    __slots__ = ("launches",)
    LAUNCHES_FIELD_NUMBER: _ClassVar[int]
    launches: _containers.RepeatedCompositeFieldContainer[LaunchWithCommandStatuses]
    def __init__(self, launches: _Optional[_Iterable[_Union[LaunchWithCommandStatuses, _Mapping]]] = ...) -> None: ...

class LaunchWithCommandStatuses(_message.Message):
    __slots__ = ("launch", "commands_unknown_count", "commands_unacknowledged_count", "commands_acknowledged_count", "commands_running_count", "commands_succeeded_count", "commands_failed_count", "commands_killed_count", "commands_cancelled_count", "commands_total_count")
    LAUNCH_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_UNKNOWN_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_UNACKNOWLEDGED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_ACKNOWLEDGED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_RUNNING_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_SUCCEEDED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_KILLED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_CANCELLED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    launch: Launch
    commands_unknown_count: int
    commands_unacknowledged_count: int
    commands_acknowledged_count: int
    commands_running_count: int
    commands_succeeded_count: int
    commands_failed_count: int
    commands_killed_count: int
    commands_cancelled_count: int
    commands_total_count: int
    def __init__(self, launch: _Optional[_Union[Launch, _Mapping]] = ..., commands_unknown_count: _Optional[int] = ..., commands_unacknowledged_count: _Optional[int] = ..., commands_acknowledged_count: _Optional[int] = ..., commands_running_count: _Optional[int] = ..., commands_succeeded_count: _Optional[int] = ..., commands_failed_count: _Optional[int] = ..., commands_killed_count: _Optional[int] = ..., commands_cancelled_count: _Optional[int] = ..., commands_total_count: _Optional[int] = ...) -> None: ...

class LaunchDetails(_message.Message):
    __slots__ = ("launch", "commands", "xids", "logs")
    LAUNCH_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    XIDS_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    launch: Launch
    commands: _containers.RepeatedCompositeFieldContainer[_exec_pb2.Command]
    xids: _containers.RepeatedCompositeFieldContainer[Xid]
    logs: _containers.RepeatedCompositeFieldContainer[_logs_pb2.Log]
    def __init__(self, launch: _Optional[_Union[Launch, _Mapping]] = ..., commands: _Optional[_Iterable[_Union[_exec_pb2.Command, _Mapping]]] = ..., xids: _Optional[_Iterable[_Union[Xid, _Mapping]]] = ..., logs: _Optional[_Iterable[_Union[_logs_pb2.Log, _Mapping]]] = ...) -> None: ...

class Xid(_message.Message):
    __slots__ = ("hostname", "gpu_uuid", "pci_id", "xid", "occurred_at")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    GPU_UUID_FIELD_NUMBER: _ClassVar[int]
    PCI_ID_FIELD_NUMBER: _ClassVar[int]
    XID_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    gpu_uuid: str
    pci_id: str
    xid: int
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, hostname: _Optional[str] = ..., gpu_uuid: _Optional[str] = ..., pci_id: _Optional[str] = ..., xid: _Optional[int] = ..., occurred_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateLaunchRequest(_message.Message):
    __slots__ = ("launched_by", "command_to_run", "command", "hostnames", "title", "description", "replicas", "replica_resources")
    LAUNCHED_BY_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TO_RUN_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    REPLICA_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    launched_by: str
    command_to_run: str
    command: _containers.RepeatedScalarFieldContainer[str]
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    title: str
    description: str
    replicas: int
    replica_resources: _resources_pb2.Resources
    def __init__(self, launched_by: _Optional[str] = ..., command_to_run: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., hostnames: _Optional[_Iterable[str]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., replicas: _Optional[int] = ..., replica_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ...) -> None: ...
