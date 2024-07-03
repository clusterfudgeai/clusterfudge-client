from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TunnelRequest(_message.Message):
    __slots__ = ("initialise", "data")
    INITIALISE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    initialise: InitialiseRequest
    data: Data
    def __init__(self, initialise: _Optional[_Union[InitialiseRequest, _Mapping]] = ..., data: _Optional[_Union[Data, _Mapping]] = ...) -> None: ...

class InitialiseRequest(_message.Message):
    __slots__ = ("exec_command_id",)
    EXEC_COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    exec_command_id: str
    def __init__(self, exec_command_id: _Optional[str] = ...) -> None: ...

class Data(_message.Message):
    __slots__ = ("data", "close")
    DATA_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    close: bool
    def __init__(self, data: _Optional[bytes] = ..., close: bool = ...) -> None: ...
