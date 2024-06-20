from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Resources(_message.Message):
    __slots__ = ("cpus", "memory_mb", "gpu_a100_40gb", "gpu_a100_80gb", "gpu_h100", "gpu_rtx3090", "gpu_t4", "gpu_rtx6000", "gpu_l4", "gpu_p4", "gpu_p100", "gpu_v100", "gpu_rtx3080", "gpu_rtx4090", "gpu_rtx4080")
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
    def __init__(self, cpus: _Optional[int] = ..., memory_mb: _Optional[int] = ..., gpu_a100_40gb: _Optional[int] = ..., gpu_a100_80gb: _Optional[int] = ..., gpu_h100: _Optional[int] = ..., gpu_rtx3090: _Optional[int] = ..., gpu_t4: _Optional[int] = ..., gpu_rtx6000: _Optional[int] = ..., gpu_l4: _Optional[int] = ..., gpu_p4: _Optional[int] = ..., gpu_p100: _Optional[int] = ..., gpu_v100: _Optional[int] = ..., gpu_rtx3080: _Optional[int] = ..., gpu_rtx4090: _Optional[int] = ..., gpu_rtx4080: _Optional[int] = ...) -> None: ...
