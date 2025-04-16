from fudgelet import fudgelet_pb2 as _fudgelet_pb2
from pagespb import pages_pb2 as _pages_pb2
from exec import exec_pb2 as _exec_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSlurmJobRequest(_message.Message):
    __slots__ = ("job_id", "cluster")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    cluster: str
    def __init__(self, job_id: _Optional[str] = ..., cluster: _Optional[str] = ...) -> None: ...

class GetSlurmJobResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: _fudgelet_pb2.SlurmJob
    def __init__(self, job: _Optional[_Union[_fudgelet_pb2.SlurmJob, _Mapping]] = ...) -> None: ...

class GetSlurmArrayJobRequest(_message.Message):
    __slots__ = ("array_master_job_id", "cluster")
    ARRAY_MASTER_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    array_master_job_id: str
    cluster: str
    def __init__(self, array_master_job_id: _Optional[str] = ..., cluster: _Optional[str] = ...) -> None: ...

class GetSlurmArrayJobResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: _fudgelet_pb2.SlurmJob
    def __init__(self, job: _Optional[_Union[_fudgelet_pb2.SlurmJob, _Mapping]] = ...) -> None: ...

class GetSlurmArrayTasksForJobRequest(_message.Message):
    __slots__ = ("array_master_job_id", "cluster")
    ARRAY_MASTER_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    array_master_job_id: str
    cluster: str
    def __init__(self, array_master_job_id: _Optional[str] = ..., cluster: _Optional[str] = ...) -> None: ...

class GetSlurmArrayTasksForJobResponse(_message.Message):
    __slots__ = ("tasks",)
    TASKS_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[_fudgelet_pb2.SlurmJob]
    def __init__(self, tasks: _Optional[_Iterable[_Union[_fudgelet_pb2.SlurmJob, _Mapping]]] = ...) -> None: ...

class ListSlurmJobsRequest(_message.Message):
    __slots__ = ("page", "users", "statuses")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    page: _pages_pb2.Page
    users: _containers.RepeatedScalarFieldContainer[str]
    statuses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, page: _Optional[_Union[_pages_pb2.Page, _Mapping]] = ..., users: _Optional[_Iterable[str]] = ..., statuses: _Optional[_Iterable[str]] = ...) -> None: ...

class ListSlurmJobsResponse(_message.Message):
    __slots__ = ("jobs", "page_details", "aggregates", "all_users", "all_clusters")
    JOBS_FIELD_NUMBER: _ClassVar[int]
    PAGE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATES_FIELD_NUMBER: _ClassVar[int]
    ALL_USERS_FIELD_NUMBER: _ClassVar[int]
    ALL_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[_fudgelet_pb2.SlurmJob]
    page_details: _pages_pb2.PageDetails
    aggregates: SlurmJobAggregates
    all_users: _containers.RepeatedScalarFieldContainer[str]
    all_clusters: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, jobs: _Optional[_Iterable[_Union[_fudgelet_pb2.SlurmJob, _Mapping]]] = ..., page_details: _Optional[_Union[_pages_pb2.PageDetails, _Mapping]] = ..., aggregates: _Optional[_Union[SlurmJobAggregates, _Mapping]] = ..., all_users: _Optional[_Iterable[str]] = ..., all_clusters: _Optional[_Iterable[str]] = ...) -> None: ...

class ListSlurmNodesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSlurmNodesResponse(_message.Message):
    __slots__ = ("nodes",)
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[_fudgelet_pb2.SlurmNode]
    def __init__(self, nodes: _Optional[_Iterable[_Union[_fudgelet_pb2.SlurmNode, _Mapping]]] = ...) -> None: ...

class CancelSlurmJobRequest(_message.Message):
    __slots__ = ("job_id", "head_node")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    HEAD_NODE_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    head_node: str
    def __init__(self, job_id: _Optional[str] = ..., head_node: _Optional[str] = ...) -> None: ...

class CancelSlurmJobResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LaunchJupyterRequest(_message.Message):
    __slots__ = ("virtual_env_path", "gpu_per_node", "head_node")
    VIRTUAL_ENV_PATH_FIELD_NUMBER: _ClassVar[int]
    GPU_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    HEAD_NODE_FIELD_NUMBER: _ClassVar[int]
    virtual_env_path: str
    gpu_per_node: int
    head_node: str
    def __init__(self, virtual_env_path: _Optional[str] = ..., gpu_per_node: _Optional[int] = ..., head_node: _Optional[str] = ...) -> None: ...

class LaunchJupyterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DebugJobWithAIRequest(_message.Message):
    __slots__ = ("job_id", "cluster")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    cluster: str
    def __init__(self, job_id: _Optional[str] = ..., cluster: _Optional[str] = ...) -> None: ...

class DebugJobWithAIResponse(_message.Message):
    __slots__ = ("analysis", "created_at")
    ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    analysis: str
    created_at: str
    def __init__(self, analysis: _Optional[str] = ..., created_at: _Optional[str] = ...) -> None: ...

class UserStats(_message.Message):
    __slots__ = ("user", "job_count", "gpu_hours")
    USER_FIELD_NUMBER: _ClassVar[int]
    JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    GPU_HOURS_FIELD_NUMBER: _ClassVar[int]
    user: str
    job_count: int
    gpu_hours: float
    def __init__(self, user: _Optional[str] = ..., job_count: _Optional[int] = ..., gpu_hours: _Optional[float] = ...) -> None: ...

class SlurmJobAggregates(_message.Message):
    __slots__ = ("running_jobs_count", "pending_jobs_count", "user_stats_past_week", "user_stats_past_month", "user_stats_past_year")
    RUNNING_JOBS_COUNT_FIELD_NUMBER: _ClassVar[int]
    PENDING_JOBS_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_STATS_PAST_WEEK_FIELD_NUMBER: _ClassVar[int]
    USER_STATS_PAST_MONTH_FIELD_NUMBER: _ClassVar[int]
    USER_STATS_PAST_YEAR_FIELD_NUMBER: _ClassVar[int]
    running_jobs_count: int
    pending_jobs_count: int
    user_stats_past_week: _containers.RepeatedCompositeFieldContainer[UserStats]
    user_stats_past_month: _containers.RepeatedCompositeFieldContainer[UserStats]
    user_stats_past_year: _containers.RepeatedCompositeFieldContainer[UserStats]
    def __init__(self, running_jobs_count: _Optional[int] = ..., pending_jobs_count: _Optional[int] = ..., user_stats_past_week: _Optional[_Iterable[_Union[UserStats, _Mapping]]] = ..., user_stats_past_month: _Optional[_Iterable[_Union[UserStats, _Mapping]]] = ..., user_stats_past_year: _Optional[_Iterable[_Union[UserStats, _Mapping]]] = ...) -> None: ...

class LaunchSbatchRequest(_message.Message):
    __slots__ = ("head_node", "script_path", "reference_id", "unix_user", "env_vars", "args", "sbatch_content")
    HEAD_NODE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    UNIX_USER_FIELD_NUMBER: _ClassVar[int]
    ENV_VARS_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    SBATCH_CONTENT_FIELD_NUMBER: _ClassVar[int]
    head_node: str
    script_path: str
    reference_id: str
    unix_user: str
    env_vars: _containers.RepeatedCompositeFieldContainer[_exec_pb2.EnvironmentVariable]
    args: _containers.RepeatedScalarFieldContainer[str]
    sbatch_content: str
    def __init__(self, head_node: _Optional[str] = ..., script_path: _Optional[str] = ..., reference_id: _Optional[str] = ..., unix_user: _Optional[str] = ..., env_vars: _Optional[_Iterable[_Union[_exec_pb2.EnvironmentVariable, _Mapping]]] = ..., args: _Optional[_Iterable[str]] = ..., sbatch_content: _Optional[str] = ...) -> None: ...

class LaunchSbatchResponse(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: _exec_pb2.Command
    def __init__(self, command: _Optional[_Union[_exec_pb2.Command, _Mapping]] = ...) -> None: ...
