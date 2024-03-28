from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Resources(_message.Message):
    __slots__ = ["cpus", "gpu_a100_40gb", "gpu_a100_80gb", "gpu_h100", "gpu_rtx3090", "gpu_t4", "memory_mb"]
    CPUS_FIELD_NUMBER: _ClassVar[int]
    GPU_A100_40GB_FIELD_NUMBER: _ClassVar[int]
    GPU_A100_80GB_FIELD_NUMBER: _ClassVar[int]
    GPU_H100_FIELD_NUMBER: _ClassVar[int]
    GPU_RTX3090_FIELD_NUMBER: _ClassVar[int]
    GPU_T4_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    cpus: int
    gpu_a100_40gb: int
    gpu_a100_80gb: int
    gpu_h100: int
    gpu_rtx3090: int
    gpu_t4: int
    memory_mb: int
    def __init__(self, cpus: _Optional[int] = ..., memory_mb: _Optional[int] = ..., gpu_a100_40gb: _Optional[int] = ..., gpu_a100_80gb: _Optional[int] = ..., gpu_h100: _Optional[int] = ..., gpu_rtx3090: _Optional[int] = ..., gpu_t4: _Optional[int] = ...) -> None: ...
