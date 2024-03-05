from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Resources(_message.Message):
    __slots__ = ("cpus", "memory_mb", "gpu_a100_40gb", "gpu_a100_80gb", "gpu_h100")
    CPUS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    GPU_A100_40GB_FIELD_NUMBER: _ClassVar[int]
    GPU_A100_80GB_FIELD_NUMBER: _ClassVar[int]
    GPU_H100_FIELD_NUMBER: _ClassVar[int]
    cpus: int
    memory_mb: int
    gpu_a100_40gb: int
    gpu_a100_80gb: int
    gpu_h100: int
    def __init__(self, cpus: _Optional[int] = ..., memory_mb: _Optional[int] = ..., gpu_a100_40gb: _Optional[int] = ..., gpu_a100_80gb: _Optional[int] = ..., gpu_h100: _Optional[int] = ...) -> None: ...
