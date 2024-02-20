from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetLaunchRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListLaunchesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLaunchesResponse(_message.Message):
    __slots__ = ("launches",)
    LAUNCHES_FIELD_NUMBER: _ClassVar[int]
    launches: _containers.RepeatedCompositeFieldContainer[Launch]
    def __init__(self, launches: _Optional[_Iterable[_Union[Launch, _Mapping]]] = ...) -> None: ...

class Launch(_message.Message):
    __slots__ = ("launch_id", "launched_by", "submitted_at", "command_to_run", "command", "hostnames", "status", "id")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LAUNCH_STATUS_UNKNOWN: _ClassVar[Launch.Status]
        LAUNCH_STATUS_PENDING: _ClassVar[Launch.Status]
        LAUNCH_STATUS_RUNNING: _ClassVar[Launch.Status]
        LAUNCH_STATUS_COMPLETED: _ClassVar[Launch.Status]
        LAUNCH_STATUS_FAILED: _ClassVar[Launch.Status]
        LAUNCH_STATUS_UNMANAGED: _ClassVar[Launch.Status]
    LAUNCH_STATUS_UNKNOWN: Launch.Status
    LAUNCH_STATUS_PENDING: Launch.Status
    LAUNCH_STATUS_RUNNING: Launch.Status
    LAUNCH_STATUS_COMPLETED: Launch.Status
    LAUNCH_STATUS_FAILED: Launch.Status
    LAUNCH_STATUS_UNMANAGED: Launch.Status
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCHED_BY_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TO_RUN_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    launch_id: int
    launched_by: str
    submitted_at: _timestamp_pb2.Timestamp
    command_to_run: str
    command: _containers.RepeatedScalarFieldContainer[str]
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    status: Launch.Status
    id: str
    def __init__(self, launch_id: _Optional[int] = ..., launched_by: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., command_to_run: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., hostnames: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[Launch.Status, str]] = ..., id: _Optional[str] = ...) -> None: ...

class ListLaunchesWithCommandStatusesResponse(_message.Message):
    __slots__ = ("launches",)
    LAUNCHES_FIELD_NUMBER: _ClassVar[int]
    launches: _containers.RepeatedCompositeFieldContainer[LaunchWithCommandStatuses]
    def __init__(self, launches: _Optional[_Iterable[_Union[LaunchWithCommandStatuses, _Mapping]]] = ...) -> None: ...

class LaunchWithCommandStatuses(_message.Message):
    __slots__ = ("launch", "commands_unknown_count", "commands_unacknowledged_count", "commands_acknowledged_count", "commands_running_count", "commands_succeeded_count", "commands_failed_count")
    LAUNCH_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_UNKNOWN_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_UNACKNOWLEDGED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_ACKNOWLEDGED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_RUNNING_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_SUCCEEDED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    launch: Launch
    commands_unknown_count: int
    commands_unacknowledged_count: int
    commands_acknowledged_count: int
    commands_running_count: int
    commands_succeeded_count: int
    commands_failed_count: int
    def __init__(self, launch: _Optional[_Union[Launch, _Mapping]] = ..., commands_unknown_count: _Optional[int] = ..., commands_unacknowledged_count: _Optional[int] = ..., commands_acknowledged_count: _Optional[int] = ..., commands_running_count: _Optional[int] = ..., commands_succeeded_count: _Optional[int] = ..., commands_failed_count: _Optional[int] = ...) -> None: ...

class CreateLaunchRequest(_message.Message):
    __slots__ = ("launched_by", "command_to_run", "command", "hostnames")
    LAUNCHED_BY_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TO_RUN_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    launched_by: str
    command_to_run: str
    command: _containers.RepeatedScalarFieldContainer[str]
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, launched_by: _Optional[str] = ..., command_to_run: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., hostnames: _Optional[_Iterable[str]] = ...) -> None: ...