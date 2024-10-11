from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Resources(_message.Message):
    __slots__ = ("cpus", "memory_mb", "gpu_a100_40gb", "gpu_a100_80gb", "gpu_h100", "gpu_rtx3090", "gpu_t4", "gpu_rtx6000", "gpu_l4", "gpu_p4", "gpu_p100", "gpu_v100", "gpu_rtx3080", "gpu_rtx4090", "gpu_rtx4080", "gpu_rtx3070", "gpu_rtx3060", "gpu_rtx3050", "gpu_rtx4070", "gpu_rtx4060", "gpu_gtx1050", "gpu_h200")
    CPUS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    GPU_A100_40GB_FIELD_NUMBER: _ClassVar[int]
    GPU_A100_80GB_FIELD_NUMBER: _ClassVar[int]
    GPU_H100_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX3090_FIELD_NUMBER: _ClassVar[int]
    GPU_T4_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX6000_FIELD_NUMBER: _ClassVar[int]
    GPU_L4_FIELD_NUMBER: _ClassVar[int]
    GPU_P4_FIELD_NUMBER: _ClassVar[int]
    GPU_P100_FIELD_NUMBER: _ClassVar[int]
    GPU_V100_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX3080_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX4090_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX4080_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX3070_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX3060_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX3050_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX4070_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX4060_FIELD_NUMBER: _ClassVar[int]
    GPU_GTX1050_FIELD_NUMBER: _ClassVar[int]
    GPU_H200_FIELD_NUMBER: _ClassVar[int]
    cpus: int
    memory_mb: int
    gpu_a100_40gb: int
    gpu_a100_80gb: int
    gpu_h100: int
    gpu_rtx3090: int
    gpu_t4: int
    gpu_rtx6000: int
    gpu_l4: int
    gpu_p4: int
    gpu_p100: int
    gpu_v100: int
    gpu_rtx3080: int
    gpu_rtx4090: int
    gpu_rtx4080: int
    gpu_rtx3070: int
    gpu_rtx3060: int
    gpu_rtx3050: int
    gpu_rtx4070: int
    gpu_rtx4060: int
    gpu_gtx1050: int
    gpu_h200: int
    def __init__(self, cpus: _Optional[int] = ..., memory_mb: _Optional[int] = ..., gpu_a100_40gb: _Optional[int] = ..., gpu_a100_80gb: _Optional[int] = ..., gpu_h100: _Optional[int] = ..., gpu_rtx3090: _Optional[int] = ..., gpu_t4: _Optional[int] = ..., gpu_rtx6000: _Optional[int] = ..., gpu_l4: _Optional[int] = ..., gpu_p4: _Optional[int] = ..., gpu_p100: _Optional[int] = ..., gpu_v100: _Optional[int] = ..., gpu_rtx3080: _Optional[int] = ..., gpu_rtx4090: _Optional[int] = ..., gpu_rtx4080: _Optional[int] = ..., gpu_rtx3070: _Optional[int] = ..., gpu_rtx3060: _Optional[int] = ..., gpu_rtx3050: _Optional[int] = ..., gpu_rtx4070: _Optional[int] = ..., gpu_rtx4060: _Optional[int] = ..., gpu_gtx1050: _Optional[int] = ..., gpu_h200: _Optional[int] = ...) -> None: ...

class ClusterResources(_message.Message):
    __slots__ = ("name", "total_resources", "used_resources", "used_non_clusterfudge", "available_resources", "cordoned_resources", "offline_resources", "shard_resources", "gpu_rtx3090", "gpu_a100_40gb", "gpu_a100_80gb", "gpu_h100", "gpu_t4", "gpu_rtx6000", "gpu_l4", "gpu_p4", "gpu_p100", "gpu_v100", "gpu_rtx3080", "gpu_rtx4090", "gpu_rtx4080", "gpu_rtx3070", "gpu_rtx3060", "gpu_rtx3050", "gpu_rtx4070", "gpu_rtx4060", "gpu_gtx1050", "gpu_h200")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    USED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    USED_NON_CLUSTERFUDGE_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CORDONED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SHARD_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX3090_FIELD_NUMBER: _ClassVar[int]
    GPU_A100_40GB_FIELD_NUMBER: _ClassVar[int]
    GPU_A100_80GB_FIELD_NUMBER: _ClassVar[int]
    GPU_H100_FIELD_NUMBER: _ClassVar[int]
    GPU_T4_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX6000_FIELD_NUMBER: _ClassVar[int]
    GPU_L4_FIELD_NUMBER: _ClassVar[int]
    GPU_P4_FIELD_NUMBER: _ClassVar[int]
    GPU_P100_FIELD_NUMBER: _ClassVar[int]
    GPU_V100_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX3080_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX4090_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX4080_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX3070_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX3060_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX3050_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX4070_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX4060_FIELD_NUMBER: _ClassVar[int]
    GPU_GTX1050_FIELD_NUMBER: _ClassVar[int]
    GPU_H200_FIELD_NUMBER: _ClassVar[int]
    name: str
    total_resources: Resources
    used_resources: Resources
    used_non_clusterfudge: Resources
    available_resources: Resources
    cordoned_resources: Resources
    offline_resources: Resources
    shard_resources: _containers.RepeatedCompositeFieldContainer[ClusterResources]
    gpu_rtx3090: ResourceStatuses
    gpu_a100_40gb: ResourceStatuses
    gpu_a100_80gb: ResourceStatuses
    gpu_h100: ResourceStatuses
    gpu_t4: ResourceStatuses
    gpu_rtx6000: ResourceStatuses
    gpu_l4: ResourceStatuses
    gpu_p4: ResourceStatuses
    gpu_p100: ResourceStatuses
    gpu_v100: ResourceStatuses
    gpu_rtx3080: ResourceStatuses
    gpu_rtx4090: ResourceStatuses
    gpu_rtx4080: ResourceStatuses
    gpu_rtx3070: ResourceStatuses
    gpu_rtx3060: ResourceStatuses
    gpu_rtx3050: ResourceStatuses
    gpu_rtx4070: ResourceStatuses
    gpu_rtx4060: ResourceStatuses
    gpu_gtx1050: ResourceStatuses
    gpu_h200: ResourceStatuses
    def __init__(self, name: _Optional[str] = ..., total_resources: _Optional[_Union[Resources, _Mapping]] = ..., used_resources: _Optional[_Union[Resources, _Mapping]] = ..., used_non_clusterfudge: _Optional[_Union[Resources, _Mapping]] = ..., available_resources: _Optional[_Union[Resources, _Mapping]] = ..., cordoned_resources: _Optional[_Union[Resources, _Mapping]] = ..., offline_resources: _Optional[_Union[Resources, _Mapping]] = ..., shard_resources: _Optional[_Iterable[_Union[ClusterResources, _Mapping]]] = ..., gpu_rtx3090: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_a100_40gb: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_a100_80gb: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_h100: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_t4: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_rtx6000: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_l4: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_p4: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_p100: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_v100: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_rtx3080: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_rtx4090: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_rtx4080: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_rtx3070: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_rtx3060: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_rtx3050: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_rtx4070: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_rtx4060: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_gtx1050: _Optional[_Union[ResourceStatuses, _Mapping]] = ..., gpu_h200: _Optional[_Union[ResourceStatuses, _Mapping]] = ...) -> None: ...

class ResourceStatuses(_message.Message):
    __slots__ = ("total", "used", "used_non_clusterfudge", "available", "cordoned", "offline")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    USED_NON_CLUSTERFUDGE_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    CORDONED_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_FIELD_NUMBER: _ClassVar[int]
    total: ResourceCountWithHostnames
    used: ResourceCountWithHostnames
    used_non_clusterfudge: ResourceCountWithHostnames
    available: ResourceCountWithHostnames
    cordoned: ResourceCountWithHostnames
    offline: ResourceCountWithHostnames
    def __init__(self, total: _Optional[_Union[ResourceCountWithHostnames, _Mapping]] = ..., used: _Optional[_Union[ResourceCountWithHostnames, _Mapping]] = ..., used_non_clusterfudge: _Optional[_Union[ResourceCountWithHostnames, _Mapping]] = ..., available: _Optional[_Union[ResourceCountWithHostnames, _Mapping]] = ..., cordoned: _Optional[_Union[ResourceCountWithHostnames, _Mapping]] = ..., offline: _Optional[_Union[ResourceCountWithHostnames, _Mapping]] = ...) -> None: ...

class ResourceCountWithHostnames(_message.Message):
    __slots__ = ("count", "hostnames")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    count: int
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, count: _Optional[int] = ..., hostnames: _Optional[_Iterable[str]] = ...) -> None: ...
