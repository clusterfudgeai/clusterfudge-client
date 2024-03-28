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
    __slots__ = ["available_resources", "cordoned_resources", "gpu_a100_40gb", "gpu_a100_80gb", "gpu_h100", "gpu_rtx3090", "gpu_t4", "name", "offline_resources", "shard_resources", "total_resources", "used_non_clusterfudge", "used_resources"]
    AVAILABLE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CORDONED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    GPU_A100_40GB_FIELD_NUMBER: _ClassVar[int]
    GPU_A100_80GB_FIELD_NUMBER: _ClassVar[int]
    GPU_H100_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX3090_FIELD_NUMBER: _ClassVar[int]
    GPU_T4_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SHARD_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    USED_NON_CLUSTERFUDGE_FIELD_NUMBER: _ClassVar[int]
    USED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    available_resources: _resources_pb2.Resources
    cordoned_resources: _resources_pb2.Resources
    gpu_a100_40gb: ResourceStatuses
    gpu_a100_80gb: ResourceStatuses
    gpu_h100: ResourceStatuses
    gpu_rtx3090: ResourceStatuses
    gpu_t4: ResourceStatuses
    name: str
    offline_resources: _resources_pb2.Resources
    shard_resources: _containers.RepeatedCompositeFieldContainer[ShardResources]
    total_resources: _resources_pb2.Resources
    used_non_clusterfudge: _resources_pb2.Resources
    used_resources: _resources_pb2.Resources
    def __init__(self, name: _Optional[str] = ..., total_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., used_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., used_non_clusterfudge: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., available_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., cordoned_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., offline_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., shard_resources: _Optional[_Iterable[_Union[ShardResources, _Mapping]]] = ..., gpu_rtx3090: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_a100_40gb: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_a100_80gb: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_h100: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_t4: _Optional[_Union[ResourceStatuses, _Mapping]] = ...) -> None: ...

class CreateLaunchRequest(_message.Message):
    __slots__ = ["cluster", "command", "command_to_run", "description", "git_branch", "git_repo", "hostnames", "jobs", "launch_script_body", "launched_by", "replica_resources", "replicas", "shard", "title", "zip_file_contents"]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TO_RUN_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GIT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    GIT_REPO_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    LAUNCHED_BY_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_SCRIPT_BODY_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    REPLICA_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ZIP_FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    cluster: str
    command: _containers.RepeatedScalarFieldContainer[str]
    command_to_run: str
    description: str
    git_branch: str
    git_repo: str
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    jobs: _containers.RepeatedCompositeFieldContainer[Job]
    launch_script_body: str
    launched_by: str
    replica_resources: _resources_pb2.Resources
    replicas: int
    shard: str
    title: str
    zip_file_contents: bytes
    def __init__(self, launched_by: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., command_to_run: _Optional[str] = ..., hostnames: _Optional[_Iterable[str]] = ..., replicas: _Optional[int] = ..., replica_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., launch_script_body: _Optional[str] = ..., zip_file_contents: _Optional[bytes] = ..., git_repo: _Optional[str] = ..., git_branch: _Optional[str] = ..., shard: _Optional[str] = ..., cluster: _Optional[str] = ..., jobs: _Optional[_Iterable[_Union[Job, _Mapping]]] = ...) -> None: ...

class DownloadZipRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DownloadZipResponse(_message.Message):
    __slots__ = ["zip"]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    zip: Zip
    def __init__(self, zip: _Optional[_Union[Zip, _Mapping]] = ...) -> None: ...

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

class ImportantLog(_message.Message):
    __slots__ = ["exec_command_id", "hostname", "id", "launch_id", "occurred_at", "text_payload"]
    EXEC_COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    TEXT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    exec_command_id: str
    hostname: str
    id: str
    launch_id: str
    occurred_at: _timestamp_pb2.Timestamp
    text_payload: str
    def __init__(self, id: _Optional[str] = ..., hostname: _Optional[str] = ..., occurred_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., launch_id: _Optional[str] = ..., exec_command_id: _Optional[str] = ..., text_payload: _Optional[str] = ...) -> None: ...

class Job(_message.Message):
    __slots__ = ["processes", "replicas", "short_name"]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    processes: _containers.RepeatedCompositeFieldContainer[Process]
    replicas: int
    short_name: str
    def __init__(self, short_name: _Optional[str] = ..., replicas: _Optional[int] = ..., processes: _Optional[_Iterable[_Union[Process, _Mapping]]] = ...) -> None: ...

class Launch(_message.Message):
    __slots__ = ["cluster", "command", "command_to_run", "description", "git_branch", "git_repo", "hostnames", "id", "jobs", "launch_id", "launch_script_body", "launched_by", "replica_resources", "replicas", "scheduling_log", "shard", "status", "submitted_at", "title", "zip_id"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TO_RUN_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GIT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    GIT_REPO_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
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
    SHARD_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ZIP_ID_FIELD_NUMBER: _ClassVar[int]
    cluster: str
    command: _containers.RepeatedScalarFieldContainer[str]
    command_to_run: str
    description: str
    git_branch: str
    git_repo: str
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    id: str
    jobs: _containers.RepeatedCompositeFieldContainer[Job]
    launch_id: int
    launch_script_body: str
    launched_by: str
    replica_resources: _resources_pb2.Resources
    replicas: int
    scheduling_log: _containers.RepeatedScalarFieldContainer[str]
    shard: str
    status: Launch.Status
    submitted_at: _timestamp_pb2.Timestamp
    title: str
    zip_id: str
    def __init__(self, launch_id: _Optional[int] = ..., launched_by: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., command_to_run: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., hostnames: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[Launch.Status, str]] = ..., id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., replicas: _Optional[int] = ..., replica_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., launch_script_body: _Optional[str] = ..., scheduling_log: _Optional[_Iterable[str]] = ..., zip_id: _Optional[str] = ..., git_repo: _Optional[str] = ..., git_branch: _Optional[str] = ..., shard: _Optional[str] = ..., cluster: _Optional[str] = ..., jobs: _Optional[_Iterable[_Union[Job, _Mapping]]] = ...) -> None: ...

class LaunchDetails(_message.Message):
    __slots__ = ["commands", "important_logs", "launch", "logs", "xids"]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    IMPORTANT_LOGS_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    XIDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[_exec_pb2.Command]
    important_logs: _containers.RepeatedCompositeFieldContainer[ImportantLog]
    launch: Launch
    logs: _containers.RepeatedCompositeFieldContainer[_logs_pb2.Log]
    xids: _containers.RepeatedCompositeFieldContainer[Xid]
    def __init__(self, launch: _Optional[_Union[Launch, _Mapping]] = ..., commands: _Optional[_Iterable[_Union[_exec_pb2.Command, _Mapping]]] = ..., xids: _Optional[_Iterable[_Union[Xid, _Mapping]]] = ..., logs: _Optional[_Iterable[_Union[_logs_pb2.Log, _Mapping]]] = ..., important_logs: _Optional[_Iterable[_Union[ImportantLog, _Mapping]]] = ...) -> None: ...

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

class Process(_message.Message):
    __slots__ = ["command", "resource_requirements"]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    command: _containers.RepeatedScalarFieldContainer[str]
    resource_requirements: _resources_pb2.Resources
    def __init__(self, command: _Optional[_Iterable[str]] = ..., resource_requirements: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ...) -> None: ...

class RerunLaunchRequest(_message.Message):
    __slots__ = ["launch_id"]
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    launch_id: str
    def __init__(self, launch_id: _Optional[str] = ...) -> None: ...

class RerunLaunchResponse(_message.Message):
    __slots__ = ["launch"]
    LAUNCH_FIELD_NUMBER: _ClassVar[int]
    launch: Launch
    def __init__(self, launch: _Optional[_Union[Launch, _Mapping]] = ...) -> None: ...

class ResourceCountWithHostnames(_message.Message):
    __slots__ = ["count", "hostnames"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    count: int
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, count: _Optional[int] = ..., hostnames: _Optional[_Iterable[str]] = ...) -> None: ...

class ResourceStatuses(_message.Message):
    __slots__ = ["available", "cordoned", "offline", "total", "used", "used_non_clusterfudge"]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    CORDONED_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    USED_NON_CLUSTERFUDGE_FIELD_NUMBER: _ClassVar[int]
    available: ResourceCountWithHostnames
    cordoned: ResourceCountWithHostnames
    offline: ResourceCountWithHostnames
    total: ResourceCountWithHostnames
    used: ResourceCountWithHostnames
    used_non_clusterfudge: ResourceCountWithHostnames
    def __init__(self, total: _Optional[_Union[ResourceCountWithHostnames, _Mapping]] = ..., used: _Optional[_Union[ResourceCountWithHostnames, _Mapping]] = ..., used_non_clusterfudge: _Optional[_Union[ResourceCountWithHostnames, _Mapping]] = ..., available: _Optional[_Union[ResourceCountWithHostnames, _Mapping]] = ..., cordoned: _Optional[_Union[ResourceCountWithHostnames, _Mapping]] = ..., offline: _Optional[_Union[ResourceCountWithHostnames, _Mapping]] = ...) -> None: ...

class ShardResources(_message.Message):
    __slots__ = ["available_resources", "cordoned_resources", "gpu_a100_40gb", "gpu_a100_80gb", "gpu_h100", "gpu_rtx3090", "gpu_t4", "name", "offline_resources", "total_resources", "used_non_clusterfudge", "used_resources"]
    AVAILABLE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CORDONED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    GPU_A100_40GB_FIELD_NUMBER: _ClassVar[int]
    GPU_A100_80GB_FIELD_NUMBER: _ClassVar[int]
    GPU_H100_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX3090_FIELD_NUMBER: _ClassVar[int]
    GPU_T4_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    USED_NON_CLUSTERFUDGE_FIELD_NUMBER: _ClassVar[int]
    USED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    available_resources: _resources_pb2.Resources
    cordoned_resources: _resources_pb2.Resources
    gpu_a100_40gb: ResourceStatuses
    gpu_a100_80gb: ResourceStatuses
    gpu_h100: ResourceStatuses
    gpu_rtx3090: ResourceStatuses
    gpu_t4: ResourceStatuses
    name: str
    offline_resources: _resources_pb2.Resources
    total_resources: _resources_pb2.Resources
    used_non_clusterfudge: _resources_pb2.Resources
    used_resources: _resources_pb2.Resources
    def __init__(self, name: _Optional[str] = ..., total_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., used_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., used_non_clusterfudge: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., available_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., cordoned_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., offline_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., gpu_rtx3090: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_a100_40gb: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_a100_80gb: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_h100: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_t4: _Optional[_Union[ResourceStatuses, _Mapping]] = ...) -> None: ...

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

class Zip(_message.Message):
    __slots__ = ["contents", "id", "launch_id", "tenant_id"]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    contents: bytes
    id: str
    launch_id: str
    tenant_id: str
    def __init__(self, tenant_id: _Optional[str] = ..., launch_id: _Optional[str] = ..., id: _Optional[str] = ..., contents: _Optional[bytes] = ...) -> None: ...
