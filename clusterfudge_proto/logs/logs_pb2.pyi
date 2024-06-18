from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Log(_message.Message):
    __slots__ = ("hostname", "source", "contents", "logged_at", "seen_at", "tenant_id", "launch_id", "exec_command_id")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    LOGGED_AT_FIELD_NUMBER: _ClassVar[int]
    SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    source: str
    contents: str
    logged_at: _timestamp_pb2.Timestamp
    seen_at: _timestamp_pb2.Timestamp
    tenant_id: str
    launch_id: str
    exec_command_id: str
    def __init__(self, hostname: _Optional[str] = ..., source: _Optional[str] = ..., contents: _Optional[str] = ..., logged_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., seen_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tenant_id: _Optional[str] = ..., launch_id: _Optional[str] = ..., exec_command_id: _Optional[str] = ...) -> None: ...
