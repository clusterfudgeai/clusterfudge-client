from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListLogsRequest(_message.Message):
    __slots__ = ("hostnames", "start_time", "end_time", "limit", "sources", "launch_ids", "exec_command_ids")
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_IDS_FIELD_NUMBER: _ClassVar[int]
    EXEC_COMMAND_IDS_FIELD_NUMBER: _ClassVar[int]
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    limit: int
    sources: _containers.RepeatedScalarFieldContainer[str]
    launch_ids: _containers.RepeatedScalarFieldContainer[str]
    exec_command_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hostnames: _Optional[_Iterable[str]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ..., sources: _Optional[_Iterable[str]] = ..., launch_ids: _Optional[_Iterable[str]] = ..., exec_command_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListLogsResponse(_message.Message):
    __slots__ = ("logs",)
    LOGS_FIELD_NUMBER: _ClassVar[int]
    logs: _containers.RepeatedCompositeFieldContainer[Log]
    def __init__(self, logs: _Optional[_Iterable[_Union[Log, _Mapping]]] = ...) -> None: ...

class ListLogSourcesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLogSourcesResponse(_message.Message):
    __slots__ = ("sources",)
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sources: _Optional[_Iterable[str]] = ...) -> None: ...

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
