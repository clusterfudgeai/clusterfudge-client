from fudgelet import fudgelet_pb2 as _fudgelet_pb2
from pagespb import pages_pb2 as _pages_pb2
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
    __slots__ = ("jobs", "page_details", "aggregates", "all_users")
    JOBS_FIELD_NUMBER: _ClassVar[int]
    PAGE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATES_FIELD_NUMBER: _ClassVar[int]
    ALL_USERS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[_fudgelet_pb2.SlurmJob]
    page_details: _pages_pb2.PageDetails
    aggregates: SlurmJobAggregates
    all_users: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, jobs: _Optional[_Iterable[_Union[_fudgelet_pb2.SlurmJob, _Mapping]]] = ..., page_details: _Optional[_Union[_pages_pb2.PageDetails, _Mapping]] = ..., aggregates: _Optional[_Union[SlurmJobAggregates, _Mapping]] = ..., all_users: _Optional[_Iterable[str]] = ...) -> None: ...

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

class SlurmJobAggregates(_message.Message):
    __slots__ = ("running_jobs_count", "pending_jobs_count")
    RUNNING_JOBS_COUNT_FIELD_NUMBER: _ClassVar[int]
    PENDING_JOBS_COUNT_FIELD_NUMBER: _ClassVar[int]
    running_jobs_count: int
    pending_jobs_count: int
    def __init__(self, running_jobs_count: _Optional[int] = ..., pending_jobs_count: _Optional[int] = ...) -> None: ...
