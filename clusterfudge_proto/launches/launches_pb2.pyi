from google.protobuf import timestamp_pb2 as _timestamp_pb2
from resources import resources_pb2 as _resources_pb2
from exec import exec_pb2 as _exec_pb2
from logs import logs_pb2 as _logs_pb2
from pagespb import pages_pb2 as _pages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LaunchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LAUNCH_TYPE_UNKNOWN: _ClassVar[LaunchType]
    LAUNCH_TYPE_COMMAND: _ClassVar[LaunchType]
    LAUNCH_TYPE_JUPYTER_NOTEBOOK: _ClassVar[LaunchType]
    LAUNCH_TYPE_WORKSTATION: _ClassVar[LaunchType]
LAUNCH_TYPE_UNKNOWN: LaunchType
LAUNCH_TYPE_COMMAND: LaunchType
LAUNCH_TYPE_JUPYTER_NOTEBOOK: LaunchType
LAUNCH_TYPE_WORKSTATION: LaunchType

class LaunchWorkstationRequest(_message.Message):
    __slots__ = ("port", "resource_requirements", "shard", "cluster")
    PORT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    port: int
    resource_requirements: _resources_pb2.Resources
    shard: str
    cluster: str
    def __init__(self, port: _Optional[int] = ..., resource_requirements: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., shard: _Optional[str] = ..., cluster: _Optional[str] = ...) -> None: ...

class LaunchWorkstationResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListResourcesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListResourcesResponse(_message.Message):
    __slots__ = ("clusters", "resource_consumers", "total", "available")
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[_resources_pb2.ClusterResources]
    resource_consumers: _containers.RepeatedCompositeFieldContainer[_exec_pb2.Command]
    total: _resources_pb2.Resources
    available: _resources_pb2.Resources
    def __init__(self, clusters: _Optional[_Iterable[_Union[_resources_pb2.ClusterResources, _Mapping]]] = ..., resource_consumers: _Optional[_Iterable[_Union[_exec_pb2.Command, _Mapping]]] = ..., total: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., available: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("page",)
    PAGE_FIELD_NUMBER: _ClassVar[int]
    page: _pages_pb2.Page
    def __init__(self, page: _Optional[_Union[_pages_pb2.Page, _Mapping]] = ...) -> None: ...

class ListLaunchesResponse(_message.Message):
    __slots__ = ("launches", "launch_status_counts", "page_details")
    LAUNCHES_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_STATUS_COUNTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    launches: _containers.RepeatedCompositeFieldContainer[Launch]
    launch_status_counts: _containers.RepeatedCompositeFieldContainer[LaunchStatusCounts]
    page_details: _pages_pb2.PageDetails
    def __init__(self, launches: _Optional[_Iterable[_Union[Launch, _Mapping]]] = ..., launch_status_counts: _Optional[_Iterable[_Union[LaunchStatusCounts, _Mapping]]] = ..., page_details: _Optional[_Union[_pages_pb2.PageDetails, _Mapping]] = ...) -> None: ...

class StopLaunchRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class StopLaunchResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Launch(_message.Message):
    __slots__ = ("launch_id", "launched_by", "submitted_at", "command_to_run", "command", "launch_type", "hostnames", "status", "id", "title", "description", "replicas", "replica_resources", "launch_script_body", "scheduling_log", "zip_id", "git_repo", "git_branch", "shard", "cluster", "jobs", "git_commit", "node_exclusivity", "queueing_behaviour")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LAUNCH_STATUS_UNKNOWN: _ClassVar[Launch.Status]
        LAUNCH_STATUS_PENDING: _ClassVar[Launch.Status]
        LAUNCH_STATUS_RUNNING: _ClassVar[Launch.Status]
        LAUNCH_STATUS_COMPLETED: _ClassVar[Launch.Status]
        LAUNCH_STATUS_FAILED: _ClassVar[Launch.Status]
        LAUNCH_STATUS_UNMANAGED: _ClassVar[Launch.Status]
        LAUNCH_STATUS_STOPPED: _ClassVar[Launch.Status]
        LAUNCH_STATUS_QUEUED: _ClassVar[Launch.Status]
    LAUNCH_STATUS_UNKNOWN: Launch.Status
    LAUNCH_STATUS_PENDING: Launch.Status
    LAUNCH_STATUS_RUNNING: Launch.Status
    LAUNCH_STATUS_COMPLETED: Launch.Status
    LAUNCH_STATUS_FAILED: Launch.Status
    LAUNCH_STATUS_UNMANAGED: Launch.Status
    LAUNCH_STATUS_STOPPED: Launch.Status
    LAUNCH_STATUS_QUEUED: Launch.Status
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCHED_BY_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TO_RUN_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    REPLICA_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_SCRIPT_BODY_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_LOG_FIELD_NUMBER: _ClassVar[int]
    ZIP_ID_FIELD_NUMBER: _ClassVar[int]
    GIT_REPO_FIELD_NUMBER: _ClassVar[int]
    GIT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    GIT_COMMIT_FIELD_NUMBER: _ClassVar[int]
    NODE_EXCLUSIVITY_FIELD_NUMBER: _ClassVar[int]
    QUEUEING_BEHAVIOUR_FIELD_NUMBER: _ClassVar[int]
    launch_id: int
    launched_by: str
    submitted_at: _timestamp_pb2.Timestamp
    command_to_run: str
    command: _containers.RepeatedScalarFieldContainer[str]
    launch_type: LaunchType
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    status: Launch.Status
    id: str
    title: str
    description: str
    replicas: int
    replica_resources: _resources_pb2.Resources
    launch_script_body: str
    scheduling_log: _containers.RepeatedScalarFieldContainer[str]
    zip_id: str
    git_repo: str
    git_branch: str
    shard: str
    cluster: str
    jobs: _containers.RepeatedCompositeFieldContainer[Job]
    git_commit: str
    node_exclusivity: _exec_pb2.NodeExclusivity
    queueing_behaviour: QueueingBehaviour
    def __init__(self, launch_id: _Optional[int] = ..., launched_by: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., command_to_run: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., launch_type: _Optional[_Union[LaunchType, str]] = ..., hostnames: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[Launch.Status, str]] = ..., id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., replicas: _Optional[int] = ..., replica_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., launch_script_body: _Optional[str] = ..., scheduling_log: _Optional[_Iterable[str]] = ..., zip_id: _Optional[str] = ..., git_repo: _Optional[str] = ..., git_branch: _Optional[str] = ..., shard: _Optional[str] = ..., cluster: _Optional[str] = ..., jobs: _Optional[_Iterable[_Union[Job, _Mapping]]] = ..., git_commit: _Optional[str] = ..., node_exclusivity: _Optional[_Union[_exec_pb2.NodeExclusivity, str]] = ..., queueing_behaviour: _Optional[_Union[QueueingBehaviour, _Mapping]] = ...) -> None: ...

class QueueingBehaviour(_message.Message):
    __slots__ = ("queue_launch",)
    QUEUE_LAUNCH_FIELD_NUMBER: _ClassVar[int]
    queue_launch: bool
    def __init__(self, queue_launch: bool = ...) -> None: ...

class RerunLaunchRequest(_message.Message):
    __slots__ = ("launch_id",)
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    launch_id: str
    def __init__(self, launch_id: _Optional[str] = ...) -> None: ...

class RerunLaunchResponse(_message.Message):
    __slots__ = ("launch",)
    LAUNCH_FIELD_NUMBER: _ClassVar[int]
    launch: Launch
    def __init__(self, launch: _Optional[_Union[Launch, _Mapping]] = ...) -> None: ...

class LaunchDetails(_message.Message):
    __slots__ = ("launch", "commands", "xids", "logs", "important_logs", "status_counts")
    LAUNCH_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    XIDS_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    IMPORTANT_LOGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_COUNTS_FIELD_NUMBER: _ClassVar[int]
    launch: Launch
    commands: _containers.RepeatedCompositeFieldContainer[_exec_pb2.Command]
    xids: _containers.RepeatedCompositeFieldContainer[Xid]
    logs: _containers.RepeatedCompositeFieldContainer[_logs_pb2.Log]
    important_logs: _containers.RepeatedCompositeFieldContainer[ImportantLog]
    status_counts: LaunchStatusCounts
    def __init__(self, launch: _Optional[_Union[Launch, _Mapping]] = ..., commands: _Optional[_Iterable[_Union[_exec_pb2.Command, _Mapping]]] = ..., xids: _Optional[_Iterable[_Union[Xid, _Mapping]]] = ..., logs: _Optional[_Iterable[_Union[_logs_pb2.Log, _Mapping]]] = ..., important_logs: _Optional[_Iterable[_Union[ImportantLog, _Mapping]]] = ..., status_counts: _Optional[_Union[LaunchStatusCounts, _Mapping]] = ...) -> None: ...

class ImportantLog(_message.Message):
    __slots__ = ("id", "hostname", "occurred_at", "launch_id", "exec_command_id", "text_payload")
    ID_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hostname: str
    occurred_at: _timestamp_pb2.Timestamp
    launch_id: str
    exec_command_id: str
    text_payload: str
    def __init__(self, id: _Optional[str] = ..., hostname: _Optional[str] = ..., occurred_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., launch_id: _Optional[str] = ..., exec_command_id: _Optional[str] = ..., text_payload: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("launched_by", "command", "command_to_run", "hostnames", "launch_type", "replicas", "replica_resources", "title", "description", "launch_script_body", "zip_file_contents", "git_repo", "git_branch", "shard", "cluster", "jobs", "zip_file_id", "git_commit", "node_exclusivity", "queueing_behaviour")
    LAUNCHED_BY_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TO_RUN_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    REPLICA_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_SCRIPT_BODY_FIELD_NUMBER: _ClassVar[int]
    ZIP_FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    GIT_REPO_FIELD_NUMBER: _ClassVar[int]
    GIT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    ZIP_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    GIT_COMMIT_FIELD_NUMBER: _ClassVar[int]
    NODE_EXCLUSIVITY_FIELD_NUMBER: _ClassVar[int]
    QUEUEING_BEHAVIOUR_FIELD_NUMBER: _ClassVar[int]
    launched_by: str
    command: _containers.RepeatedScalarFieldContainer[str]
    command_to_run: str
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    launch_type: LaunchType
    replicas: int
    replica_resources: _resources_pb2.Resources
    title: str
    description: str
    launch_script_body: str
    zip_file_contents: bytes
    git_repo: str
    git_branch: str
    shard: str
    cluster: str
    jobs: _containers.RepeatedCompositeFieldContainer[Job]
    zip_file_id: str
    git_commit: str
    node_exclusivity: _exec_pb2.NodeExclusivity
    queueing_behaviour: QueueingBehaviour
    def __init__(self, launched_by: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., command_to_run: _Optional[str] = ..., hostnames: _Optional[_Iterable[str]] = ..., launch_type: _Optional[_Union[LaunchType, str]] = ..., replicas: _Optional[int] = ..., replica_resources: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., launch_script_body: _Optional[str] = ..., zip_file_contents: _Optional[bytes] = ..., git_repo: _Optional[str] = ..., git_branch: _Optional[str] = ..., shard: _Optional[str] = ..., cluster: _Optional[str] = ..., jobs: _Optional[_Iterable[_Union[Job, _Mapping]]] = ..., zip_file_id: _Optional[str] = ..., git_commit: _Optional[str] = ..., node_exclusivity: _Optional[_Union[_exec_pb2.NodeExclusivity, str]] = ..., queueing_behaviour: _Optional[_Union[QueueingBehaviour, _Mapping]] = ...) -> None: ...

class Job(_message.Message):
    __slots__ = ("short_name", "replicas", "processes", "on_replica_failure_other_replicas_continue", "on_replica_failure_other_replicas_are_stopped")
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    ON_REPLICA_FAILURE_OTHER_REPLICAS_CONTINUE_FIELD_NUMBER: _ClassVar[int]
    ON_REPLICA_FAILURE_OTHER_REPLICAS_ARE_STOPPED_FIELD_NUMBER: _ClassVar[int]
    short_name: str
    replicas: int
    processes: _containers.RepeatedCompositeFieldContainer[Process]
    on_replica_failure_other_replicas_continue: OnReplicaFailureOtherReplicasContinue
    on_replica_failure_other_replicas_are_stopped: OnReplicaFailureOtherReplicasAreStopped
    def __init__(self, short_name: _Optional[str] = ..., replicas: _Optional[int] = ..., processes: _Optional[_Iterable[_Union[Process, _Mapping]]] = ..., on_replica_failure_other_replicas_continue: _Optional[_Union[OnReplicaFailureOtherReplicasContinue, _Mapping]] = ..., on_replica_failure_other_replicas_are_stopped: _Optional[_Union[OnReplicaFailureOtherReplicasAreStopped, _Mapping]] = ...) -> None: ...

class OnReplicaFailureOtherReplicasContinue(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnReplicaFailureOtherReplicasAreStopped(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Process(_message.Message):
    __slots__ = ("command", "resource_requirements")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    command: _containers.RepeatedScalarFieldContainer[str]
    resource_requirements: _resources_pb2.Resources
    def __init__(self, command: _Optional[_Iterable[str]] = ..., resource_requirements: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ...) -> None: ...

class DownloadZipRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DownloadZipResponse(_message.Message):
    __slots__ = ("zip",)
    ZIP_FIELD_NUMBER: _ClassVar[int]
    zip: Zip
    def __init__(self, zip: _Optional[_Union[Zip, _Mapping]] = ...) -> None: ...

class Zip(_message.Message):
    __slots__ = ("tenant_id", "launch_id", "id", "contents")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    launch_id: str
    id: str
    contents: bytes
    def __init__(self, tenant_id: _Optional[str] = ..., launch_id: _Optional[str] = ..., id: _Optional[str] = ..., contents: _Optional[bytes] = ...) -> None: ...

class LaunchStatusCounts(_message.Message):
    __slots__ = ("id", "jobs", "processes")
    ID_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    id: str
    jobs: _containers.RepeatedCompositeFieldContainer[JobStatusCounts]
    processes: StatusCounts
    def __init__(self, id: _Optional[str] = ..., jobs: _Optional[_Iterable[_Union[JobStatusCounts, _Mapping]]] = ..., processes: _Optional[_Union[StatusCounts, _Mapping]] = ...) -> None: ...

class JobStatusCounts(_message.Message):
    __slots__ = ("job_name", "replicas")
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    job_name: str
    replicas: StatusCounts
    def __init__(self, job_name: _Optional[str] = ..., replicas: _Optional[_Union[StatusCounts, _Mapping]] = ...) -> None: ...

class StatusCounts(_message.Message):
    __slots__ = ("pending", "running", "succeeded", "failed", "stopped", "total")
    PENDING_FIELD_NUMBER: _ClassVar[int]
    RUNNING_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    STOPPED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    pending: int
    running: int
    succeeded: int
    failed: int
    stopped: int
    total: int
    def __init__(self, pending: _Optional[int] = ..., running: _Optional[int] = ..., succeeded: _Optional[int] = ..., failed: _Optional[int] = ..., stopped: _Optional[int] = ..., total: _Optional[int] = ...) -> None: ...

class LaunchHelloWorldRequest(_message.Message):
    __slots__ = ("cluster", "shard", "hostnames")
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    cluster: str
    shard: str
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cluster: _Optional[str] = ..., shard: _Optional[str] = ..., hostnames: _Optional[_Iterable[str]] = ...) -> None: ...

class LaunchHelloWorldResponse(_message.Message):
    __slots__ = ("launch",)
    LAUNCH_FIELD_NUMBER: _ClassVar[int]
    launch: Launch
    def __init__(self, launch: _Optional[_Union[Launch, _Mapping]] = ...) -> None: ...

class LaunchGpuBurnRequest(_message.Message):
    __slots__ = ("cluster", "shard", "hostnames")
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    cluster: str
    shard: str
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cluster: _Optional[str] = ..., shard: _Optional[str] = ..., hostnames: _Optional[_Iterable[str]] = ...) -> None: ...

class LaunchGpuBurnResponse(_message.Message):
    __slots__ = ("launch",)
    LAUNCH_FIELD_NUMBER: _ClassVar[int]
    launch: Launch
    def __init__(self, launch: _Optional[_Union[Launch, _Mapping]] = ...) -> None: ...

class LaunchJupyterNotebookRequest(_message.Message):
    __slots__ = ("resource_requirements", "cluster", "shard")
    RESOURCE_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    resource_requirements: _resources_pb2.Resources
    cluster: str
    shard: str
    def __init__(self, resource_requirements: _Optional[_Union[_resources_pb2.Resources, _Mapping]] = ..., cluster: _Optional[str] = ..., shard: _Optional[str] = ...) -> None: ...

class LaunchJupyterNotebookResponse(_message.Message):
    __slots__ = ("launch",)
    LAUNCH_FIELD_NUMBER: _ClassVar[int]
    launch: Launch
    def __init__(self, launch: _Optional[_Union[Launch, _Mapping]] = ...) -> None: ...
