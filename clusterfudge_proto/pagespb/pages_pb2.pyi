from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Page(_message.Message):
    __slots__ = ("page_number", "limit")
    PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    page_number: _wrappers_pb2.Int32Value
    limit: _wrappers_pb2.Int32Value
    def __init__(self, page_number: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., limit: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class PageDetails(_message.Message):
    __slots__ = ("total_pages",)
    TOTAL_PAGES_FIELD_NUMBER: _ClassVar[int]
    total_pages: int
    def __init__(self, total_pages: _Optional[int] = ...) -> None: ...
