from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LivenessRequest(_message.Message):
    __slots__ = ("hostname",)
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    def __init__(self, hostname: _Optional[str] = ...) -> None: ...

class LivenessResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClientReady(_message.Message):
    __slots__ = ("exec_command_id",)
    EXEC_COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    exec_command_id: str
    def __init__(self, exec_command_id: _Optional[str] = ...) -> None: ...

class NewConnection(_message.Message):
    __slots__ = ("connection_id", "exec_command_id")
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    exec_command_id: str
    def __init__(self, connection_id: _Optional[str] = ..., exec_command_id: _Optional[str] = ...) -> None: ...

class TCPDataPacket(_message.Message):
    __slots__ = ("connection_id", "data", "close")
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    data: bytes
    close: bool
    def __init__(self, connection_id: _Optional[str] = ..., data: _Optional[bytes] = ..., close: bool = ...) -> None: ...

class TCPPacket(_message.Message):
    __slots__ = ("init", "tcp_message")
    INIT_FIELD_NUMBER: _ClassVar[int]
    TCP_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    init: TCPInit
    tcp_message: TCPMessage
    def __init__(self, init: _Optional[_Union[TCPInit, _Mapping]] = ..., tcp_message: _Optional[_Union[TCPMessage, _Mapping]] = ...) -> None: ...

class TCPInit(_message.Message):
    __slots__ = ("connection_id",)
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    def __init__(self, connection_id: _Optional[str] = ...) -> None: ...

class TCPMessage(_message.Message):
    __slots__ = ("data", "close")
    DATA_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    close: bool
    def __init__(self, data: _Optional[bytes] = ..., close: bool = ...) -> None: ...

class ProxyInitialiseRequestOrResponse(_message.Message):
    __slots__ = ("registration", "http_response", "websocket_message")
    REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    HTTP_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    WEBSOCKET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    registration: ProxyRegistration
    http_response: HttpResponse
    websocket_message: WebsocketMessage
    def __init__(self, registration: _Optional[_Union[ProxyRegistration, _Mapping]] = ..., http_response: _Optional[_Union[HttpResponse, _Mapping]] = ..., websocket_message: _Optional[_Union[WebsocketMessage, _Mapping]] = ...) -> None: ...

class ProxyRegistration(_message.Message):
    __slots__ = ("launch_id", "exec_command_id")
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    launch_id: str
    exec_command_id: str
    def __init__(self, launch_id: _Optional[str] = ..., exec_command_id: _Optional[str] = ...) -> None: ...

class ProxiedRequest(_message.Message):
    __slots__ = ("http_request", "websocket_message")
    HTTP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    WEBSOCKET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    http_request: HttpRequest
    websocket_message: WebsocketMessage
    def __init__(self, http_request: _Optional[_Union[HttpRequest, _Mapping]] = ..., websocket_message: _Optional[_Union[WebsocketMessage, _Mapping]] = ...) -> None: ...

class HttpRequest(_message.Message):
    __slots__ = ("id", "http_request")
    ID_FIELD_NUMBER: _ClassVar[int]
    HTTP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    id: str
    http_request: bytes
    def __init__(self, id: _Optional[str] = ..., http_request: _Optional[bytes] = ...) -> None: ...

class HttpResponse(_message.Message):
    __slots__ = ("req_id", "status_code", "body", "headers")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Header
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Header, _Mapping]] = ...) -> None: ...
    REQ_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    req_id: str
    status_code: int
    body: bytes
    headers: _containers.MessageMap[str, Header]
    def __init__(self, req_id: _Optional[str] = ..., status_code: _Optional[int] = ..., body: _Optional[bytes] = ..., headers: _Optional[_Mapping[str, Header]] = ...) -> None: ...

class Header(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class WebsocketMessage(_message.Message):
    __slots__ = ("req_id", "message_type", "message")
    REQ_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    req_id: str
    message_type: int
    message: bytes
    def __init__(self, req_id: _Optional[str] = ..., message_type: _Optional[int] = ..., message: _Optional[bytes] = ...) -> None: ...

class IngestLogRequest(_message.Message):
    __slots__ = ("hostname", "source", "logs", "host_timezone_utc_offset_seconds", "launch_id", "exec_command_id")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    HOST_TIMEZONE_UTC_OFFSET_SECONDS_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    source: str
    logs: _containers.RepeatedCompositeFieldContainer[Log]
    host_timezone_utc_offset_seconds: int
    launch_id: str
    exec_command_id: str
    def __init__(self, hostname: _Optional[str] = ..., source: _Optional[str] = ..., logs: _Optional[_Iterable[_Union[Log, _Mapping]]] = ..., host_timezone_utc_offset_seconds: _Optional[int] = ..., launch_id: _Optional[str] = ..., exec_command_id: _Optional[str] = ...) -> None: ...

class Log(_message.Message):
    __slots__ = ("text_payload", "seen_at", "exec_command_id", "source")
    TEXT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    EXEC_COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    text_payload: str
    seen_at: _timestamp_pb2.Timestamp
    exec_command_id: str
    source: str
    def __init__(self, text_payload: _Optional[str] = ..., seen_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., exec_command_id: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class StreamLogsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IngestLogResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IngestNodeRequest(_message.Message):
    __slots__ = ("host_name", "ips", "architecture", "build", "agent_version", "family", "platform", "version", "boot_time", "cpu_throttled", "nvidia", "infiniband_devices", "devices_with_acs_enabled", "devices_with_acs_disabled", "partitions", "cpus_summary", "memory", "node", "fudgelet_version", "scraped_at", "fudgelet_config", "cluster", "shard", "slurm_cluster")
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    IPS_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BOOT_TIME_FIELD_NUMBER: _ClassVar[int]
    CPU_THROTTLED_FIELD_NUMBER: _ClassVar[int]
    NVIDIA_FIELD_NUMBER: _ClassVar[int]
    INFINIBAND_DEVICES_FIELD_NUMBER: _ClassVar[int]
    DEVICES_WITH_ACS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEVICES_WITH_ACS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    CPUS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    FUDGELET_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCRAPED_AT_FIELD_NUMBER: _ClassVar[int]
    FUDGELET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    SLURM_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    host_name: str
    ips: _containers.RepeatedScalarFieldContainer[str]
    architecture: str
    build: str
    agent_version: str
    family: str
    platform: str
    version: str
    boot_time: str
    cpu_throttled: bool
    nvidia: Nvidia
    infiniband_devices: _containers.RepeatedCompositeFieldContainer[InfinibandDevice]
    devices_with_acs_enabled: int
    devices_with_acs_disabled: int
    partitions: _containers.RepeatedCompositeFieldContainer[DiskPartition]
    cpus_summary: CpusSummary
    memory: Memory
    node: NodeV2
    fudgelet_version: str
    scraped_at: _timestamp_pb2.Timestamp
    fudgelet_config: FudgeletConfig
    cluster: str
    shard: str
    slurm_cluster: str
    def __init__(self, host_name: _Optional[str] = ..., ips: _Optional[_Iterable[str]] = ..., architecture: _Optional[str] = ..., build: _Optional[str] = ..., agent_version: _Optional[str] = ..., family: _Optional[str] = ..., platform: _Optional[str] = ..., version: _Optional[str] = ..., boot_time: _Optional[str] = ..., cpu_throttled: bool = ..., nvidia: _Optional[_Union[Nvidia, _Mapping]] = ..., infiniband_devices: _Optional[_Iterable[_Union[InfinibandDevice, _Mapping]]] = ..., devices_with_acs_enabled: _Optional[int] = ..., devices_with_acs_disabled: _Optional[int] = ..., partitions: _Optional[_Iterable[_Union[DiskPartition, _Mapping]]] = ..., cpus_summary: _Optional[_Union[CpusSummary, _Mapping]] = ..., memory: _Optional[_Union[Memory, _Mapping]] = ..., node: _Optional[_Union[NodeV2, _Mapping]] = ..., fudgelet_version: _Optional[str] = ..., scraped_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., fudgelet_config: _Optional[_Union[FudgeletConfig, _Mapping]] = ..., cluster: _Optional[str] = ..., shard: _Optional[str] = ..., slurm_cluster: _Optional[str] = ...) -> None: ...

class NodeV2(_message.Message):
    __slots__ = ("hostname", "ips", "architecture", "build", "agent_version", "family", "platform", "version", "boot_time", "scraped_at", "cpu_throttled", "nvidia", "infiniband_devices", "devices_with_acs_enabled", "devices_with_acs_disabled", "partitions", "cpus_summary", "memory", "aws_instance_metadata", "system_configuration")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    IPS_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BOOT_TIME_FIELD_NUMBER: _ClassVar[int]
    SCRAPED_AT_FIELD_NUMBER: _ClassVar[int]
    CPU_THROTTLED_FIELD_NUMBER: _ClassVar[int]
    NVIDIA_FIELD_NUMBER: _ClassVar[int]
    INFINIBAND_DEVICES_FIELD_NUMBER: _ClassVar[int]
    DEVICES_WITH_ACS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEVICES_WITH_ACS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    CPUS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    AWS_INSTANCE_METADATA_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    ips: _containers.RepeatedScalarFieldContainer[str]
    architecture: str
    build: str
    agent_version: str
    family: str
    platform: str
    version: str
    boot_time: _timestamp_pb2.Timestamp
    scraped_at: _timestamp_pb2.Timestamp
    cpu_throttled: bool
    nvidia: Nvidia
    infiniband_devices: _containers.RepeatedCompositeFieldContainer[InfinibandDevice]
    devices_with_acs_enabled: int
    devices_with_acs_disabled: int
    partitions: _containers.RepeatedCompositeFieldContainer[DiskPartition]
    cpus_summary: CpusSummary
    memory: Memory
    aws_instance_metadata: AWSInstanceMetadata
    system_configuration: SystemConfiguration
    def __init__(self, hostname: _Optional[str] = ..., ips: _Optional[_Iterable[str]] = ..., architecture: _Optional[str] = ..., build: _Optional[str] = ..., agent_version: _Optional[str] = ..., family: _Optional[str] = ..., platform: _Optional[str] = ..., version: _Optional[str] = ..., boot_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., scraped_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cpu_throttled: bool = ..., nvidia: _Optional[_Union[Nvidia, _Mapping]] = ..., infiniband_devices: _Optional[_Iterable[_Union[InfinibandDevice, _Mapping]]] = ..., devices_with_acs_enabled: _Optional[int] = ..., devices_with_acs_disabled: _Optional[int] = ..., partitions: _Optional[_Iterable[_Union[DiskPartition, _Mapping]]] = ..., cpus_summary: _Optional[_Union[CpusSummary, _Mapping]] = ..., memory: _Optional[_Union[Memory, _Mapping]] = ..., aws_instance_metadata: _Optional[_Union[AWSInstanceMetadata, _Mapping]] = ..., system_configuration: _Optional[_Union[SystemConfiguration, _Mapping]] = ...) -> None: ...

class NvidiaSystem(_message.Message):
    __slots__ = ("driver_version", "nvml_version", "cuda_version")
    DRIVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    NVML_VERSION_FIELD_NUMBER: _ClassVar[int]
    CUDA_VERSION_FIELD_NUMBER: _ClassVar[int]
    driver_version: str
    nvml_version: str
    cuda_version: str
    def __init__(self, driver_version: _Optional[str] = ..., nvml_version: _Optional[str] = ..., cuda_version: _Optional[str] = ...) -> None: ...

class Nvidia(_message.Message):
    __slots__ = ("driver_version", "driver_version_err", "nvml_version", "nvml_version_err", "cuda_version", "cuda_version_err", "gpus", "ecc_corrected_errors_count", "ecc_uncorrected_errors_count")
    DRIVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    DRIVER_VERSION_ERR_FIELD_NUMBER: _ClassVar[int]
    NVML_VERSION_FIELD_NUMBER: _ClassVar[int]
    NVML_VERSION_ERR_FIELD_NUMBER: _ClassVar[int]
    CUDA_VERSION_FIELD_NUMBER: _ClassVar[int]
    CUDA_VERSION_ERR_FIELD_NUMBER: _ClassVar[int]
    GPUS_FIELD_NUMBER: _ClassVar[int]
    ECC_CORRECTED_ERRORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ECC_UNCORRECTED_ERRORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    driver_version: str
    driver_version_err: str
    nvml_version: str
    nvml_version_err: str
    cuda_version: str
    cuda_version_err: str
    gpus: _containers.RepeatedCompositeFieldContainer[NvidiaGPU]
    ecc_corrected_errors_count: int
    ecc_uncorrected_errors_count: int
    def __init__(self, driver_version: _Optional[str] = ..., driver_version_err: _Optional[str] = ..., nvml_version: _Optional[str] = ..., nvml_version_err: _Optional[str] = ..., cuda_version: _Optional[str] = ..., cuda_version_err: _Optional[str] = ..., gpus: _Optional[_Iterable[_Union[NvidiaGPU, _Mapping]]] = ..., ecc_corrected_errors_count: _Optional[int] = ..., ecc_uncorrected_errors_count: _Optional[int] = ...) -> None: ...

class NvidiaGPU(_message.Message):
    __slots__ = ("name", "name_err", "index", "uuid", "uuid_err", "serial", "serial_err", "pci_id", "pci_id_err", "cuda_compatibility", "cuda_compatibility_err", "power_usage", "power_usage_err", "temperature", "temperature_err", "utilization", "utilization_err", "memory_utilization", "memory_utilization_err", "memory_free", "memory_used", "memory_reserved", "memory_total", "memory_err", "device_links", "devices_on_node", "devices_a_single_switch_away", "devices_on_same_host_bridge", "devices_in_system", "devices_in_board", "devices_multiple_switches_away", "device_links_err", "ecc_corrected_errors_count", "ecc_corrected_errors_count_err", "ecc_uncorrected_errors_count", "ecc_uncorrected_errors_count_err", "processes", "processes_err", "ecc_corrected_dram_errors_count", "ecc_corrected_dram_errors_count_err", "ecc_uncorrected_dram_errors_count", "ecc_uncorrected_dram_errors_count_err", "ecc_corrected_sram_errors_count", "ecc_corrected_sram_errors_count_err", "ecc_uncorrected_sram_errors_count", "ecc_uncorrected_sram_errors_count_err", "ecc_mode_err")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_ERR_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    UUID_ERR_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_ERR_FIELD_NUMBER: _ClassVar[int]
    PCI_ID_FIELD_NUMBER: _ClassVar[int]
    PCI_ID_ERR_FIELD_NUMBER: _ClassVar[int]
    CUDA_COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    CUDA_COMPATIBILITY_ERR_FIELD_NUMBER: _ClassVar[int]
    POWER_USAGE_FIELD_NUMBER: _ClassVar[int]
    POWER_USAGE_ERR_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_ERR_FIELD_NUMBER: _ClassVar[int]
    UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    UTILIZATION_ERR_FIELD_NUMBER: _ClassVar[int]
    MEMORY_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    MEMORY_UTILIZATION_ERR_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FREE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USED_FIELD_NUMBER: _ClassVar[int]
    MEMORY_RESERVED_FIELD_NUMBER: _ClassVar[int]
    MEMORY_TOTAL_FIELD_NUMBER: _ClassVar[int]
    MEMORY_ERR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LINKS_FIELD_NUMBER: _ClassVar[int]
    DEVICES_ON_NODE_FIELD_NUMBER: _ClassVar[int]
    DEVICES_A_SINGLE_SWITCH_AWAY_FIELD_NUMBER: _ClassVar[int]
    DEVICES_ON_SAME_HOST_BRIDGE_FIELD_NUMBER: _ClassVar[int]
    DEVICES_IN_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    DEVICES_IN_BOARD_FIELD_NUMBER: _ClassVar[int]
    DEVICES_MULTIPLE_SWITCHES_AWAY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LINKS_ERR_FIELD_NUMBER: _ClassVar[int]
    ECC_CORRECTED_ERRORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ECC_CORRECTED_ERRORS_COUNT_ERR_FIELD_NUMBER: _ClassVar[int]
    ECC_UNCORRECTED_ERRORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ECC_UNCORRECTED_ERRORS_COUNT_ERR_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_ERR_FIELD_NUMBER: _ClassVar[int]
    ECC_CORRECTED_DRAM_ERRORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ECC_CORRECTED_DRAM_ERRORS_COUNT_ERR_FIELD_NUMBER: _ClassVar[int]
    ECC_UNCORRECTED_DRAM_ERRORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ECC_UNCORRECTED_DRAM_ERRORS_COUNT_ERR_FIELD_NUMBER: _ClassVar[int]
    ECC_CORRECTED_SRAM_ERRORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ECC_CORRECTED_SRAM_ERRORS_COUNT_ERR_FIELD_NUMBER: _ClassVar[int]
    ECC_UNCORRECTED_SRAM_ERRORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ECC_UNCORRECTED_SRAM_ERRORS_COUNT_ERR_FIELD_NUMBER: _ClassVar[int]
    ECC_MODE_ERR_FIELD_NUMBER: _ClassVar[int]
    name: str
    name_err: str
    index: int
    uuid: str
    uuid_err: str
    serial: str
    serial_err: str
    pci_id: str
    pci_id_err: str
    cuda_compatibility: str
    cuda_compatibility_err: str
    power_usage: int
    power_usage_err: str
    temperature: int
    temperature_err: str
    utilization: int
    utilization_err: str
    memory_utilization: int
    memory_utilization_err: str
    memory_free: int
    memory_used: int
    memory_reserved: int
    memory_total: int
    memory_err: str
    device_links: _containers.RepeatedCompositeFieldContainer[NvidiaDeviceLink]
    devices_on_node: _containers.RepeatedScalarFieldContainer[int]
    devices_a_single_switch_away: _containers.RepeatedScalarFieldContainer[int]
    devices_on_same_host_bridge: _containers.RepeatedScalarFieldContainer[int]
    devices_in_system: _containers.RepeatedScalarFieldContainer[int]
    devices_in_board: _containers.RepeatedScalarFieldContainer[int]
    devices_multiple_switches_away: _containers.RepeatedScalarFieldContainer[int]
    device_links_err: str
    ecc_corrected_errors_count: int
    ecc_corrected_errors_count_err: str
    ecc_uncorrected_errors_count: int
    ecc_uncorrected_errors_count_err: str
    processes: _containers.RepeatedCompositeFieldContainer[GPUProcess]
    processes_err: str
    ecc_corrected_dram_errors_count: int
    ecc_corrected_dram_errors_count_err: str
    ecc_uncorrected_dram_errors_count: int
    ecc_uncorrected_dram_errors_count_err: str
    ecc_corrected_sram_errors_count: int
    ecc_corrected_sram_errors_count_err: str
    ecc_uncorrected_sram_errors_count: int
    ecc_uncorrected_sram_errors_count_err: str
    ecc_mode_err: str
    def __init__(self, name: _Optional[str] = ..., name_err: _Optional[str] = ..., index: _Optional[int] = ..., uuid: _Optional[str] = ..., uuid_err: _Optional[str] = ..., serial: _Optional[str] = ..., serial_err: _Optional[str] = ..., pci_id: _Optional[str] = ..., pci_id_err: _Optional[str] = ..., cuda_compatibility: _Optional[str] = ..., cuda_compatibility_err: _Optional[str] = ..., power_usage: _Optional[int] = ..., power_usage_err: _Optional[str] = ..., temperature: _Optional[int] = ..., temperature_err: _Optional[str] = ..., utilization: _Optional[int] = ..., utilization_err: _Optional[str] = ..., memory_utilization: _Optional[int] = ..., memory_utilization_err: _Optional[str] = ..., memory_free: _Optional[int] = ..., memory_used: _Optional[int] = ..., memory_reserved: _Optional[int] = ..., memory_total: _Optional[int] = ..., memory_err: _Optional[str] = ..., device_links: _Optional[_Iterable[_Union[NvidiaDeviceLink, _Mapping]]] = ..., devices_on_node: _Optional[_Iterable[int]] = ..., devices_a_single_switch_away: _Optional[_Iterable[int]] = ..., devices_on_same_host_bridge: _Optional[_Iterable[int]] = ..., devices_in_system: _Optional[_Iterable[int]] = ..., devices_in_board: _Optional[_Iterable[int]] = ..., devices_multiple_switches_away: _Optional[_Iterable[int]] = ..., device_links_err: _Optional[str] = ..., ecc_corrected_errors_count: _Optional[int] = ..., ecc_corrected_errors_count_err: _Optional[str] = ..., ecc_uncorrected_errors_count: _Optional[int] = ..., ecc_uncorrected_errors_count_err: _Optional[str] = ..., processes: _Optional[_Iterable[_Union[GPUProcess, _Mapping]]] = ..., processes_err: _Optional[str] = ..., ecc_corrected_dram_errors_count: _Optional[int] = ..., ecc_corrected_dram_errors_count_err: _Optional[str] = ..., ecc_uncorrected_dram_errors_count: _Optional[int] = ..., ecc_uncorrected_dram_errors_count_err: _Optional[str] = ..., ecc_corrected_sram_errors_count: _Optional[int] = ..., ecc_corrected_sram_errors_count_err: _Optional[str] = ..., ecc_uncorrected_sram_errors_count: _Optional[int] = ..., ecc_uncorrected_sram_errors_count_err: _Optional[str] = ..., ecc_mode_err: _Optional[str] = ...) -> None: ...

class GPUProcess(_message.Message):
    __slots__ = ("pid", "gpu_memory_used_bytes", "executable", "cmd", "start_time", "run_time", "file_descriptors", "resident_memory", "virtual_memory", "threads", "cpu_utilization", "memory_utilization", "gpu_memory_utilization")
    PID_FIELD_NUMBER: _ClassVar[int]
    GPU_MEMORY_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    EXECUTABLE_FIELD_NUMBER: _ClassVar[int]
    CMD_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    FILE_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    RESIDENT_MEMORY_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_MEMORY_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    CPU_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    MEMORY_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    GPU_MEMORY_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    pid: int
    gpu_memory_used_bytes: int
    executable: str
    cmd: str
    start_time: int
    run_time: int
    file_descriptors: int
    resident_memory: int
    virtual_memory: int
    threads: int
    cpu_utilization: float
    memory_utilization: float
    gpu_memory_utilization: float
    def __init__(self, pid: _Optional[int] = ..., gpu_memory_used_bytes: _Optional[int] = ..., executable: _Optional[str] = ..., cmd: _Optional[str] = ..., start_time: _Optional[int] = ..., run_time: _Optional[int] = ..., file_descriptors: _Optional[int] = ..., resident_memory: _Optional[int] = ..., virtual_memory: _Optional[int] = ..., threads: _Optional[int] = ..., cpu_utilization: _Optional[float] = ..., memory_utilization: _Optional[float] = ..., gpu_memory_utilization: _Optional[float] = ...) -> None: ...

class NvidiaDeviceLink(_message.Message):
    __slots__ = ("device_index", "remote_device_index", "version", "version_err", "remote_device_type", "remote_device_type_err", "remote_device_pci_id", "remote_device_pci_id_err", "replay_errors", "recovery_errors", "flow_control_digit_crc_errors", "data_crc_errors", "ecc_errors")
    DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    REMOTE_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_ERR_FIELD_NUMBER: _ClassVar[int]
    REMOTE_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_DEVICE_TYPE_ERR_FIELD_NUMBER: _ClassVar[int]
    REMOTE_DEVICE_PCI_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_DEVICE_PCI_ID_ERR_FIELD_NUMBER: _ClassVar[int]
    REPLAY_ERRORS_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_ERRORS_FIELD_NUMBER: _ClassVar[int]
    FLOW_CONTROL_DIGIT_CRC_ERRORS_FIELD_NUMBER: _ClassVar[int]
    DATA_CRC_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ECC_ERRORS_FIELD_NUMBER: _ClassVar[int]
    device_index: int
    remote_device_index: int
    version: int
    version_err: str
    remote_device_type: str
    remote_device_type_err: str
    remote_device_pci_id: str
    remote_device_pci_id_err: str
    replay_errors: int
    recovery_errors: int
    flow_control_digit_crc_errors: int
    data_crc_errors: int
    ecc_errors: int
    def __init__(self, device_index: _Optional[int] = ..., remote_device_index: _Optional[int] = ..., version: _Optional[int] = ..., version_err: _Optional[str] = ..., remote_device_type: _Optional[str] = ..., remote_device_type_err: _Optional[str] = ..., remote_device_pci_id: _Optional[str] = ..., remote_device_pci_id_err: _Optional[str] = ..., replay_errors: _Optional[int] = ..., recovery_errors: _Optional[int] = ..., flow_control_digit_crc_errors: _Optional[int] = ..., data_crc_errors: _Optional[int] = ..., ecc_errors: _Optional[int] = ...) -> None: ...

class InfinibandDevice(_message.Message):
    __slots__ = ("name", "board_id", "firmware_version", "hca_type", "ports", "node_desc", "node_guid", "sys_image_guid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    BOARD_ID_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    HCA_TYPE_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    NODE_DESC_FIELD_NUMBER: _ClassVar[int]
    NODE_GUID_FIELD_NUMBER: _ClassVar[int]
    SYS_IMAGE_GUID_FIELD_NUMBER: _ClassVar[int]
    name: str
    board_id: str
    firmware_version: str
    hca_type: str
    ports: _containers.RepeatedCompositeFieldContainer[InfinibandPort]
    node_desc: str
    node_guid: str
    sys_image_guid: str
    def __init__(self, name: _Optional[str] = ..., board_id: _Optional[str] = ..., firmware_version: _Optional[str] = ..., hca_type: _Optional[str] = ..., ports: _Optional[_Iterable[_Union[InfinibandPort, _Mapping]]] = ..., node_desc: _Optional[str] = ..., node_guid: _Optional[str] = ..., sys_image_guid: _Optional[str] = ...) -> None: ...

class InfinibandPort(_message.Message):
    __slots__ = ("name", "port", "state", "state_id", "phys_state", "phys_state_id", "rate", "counters", "hardware_counters")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_ID_FIELD_NUMBER: _ClassVar[int]
    PHYS_STATE_FIELD_NUMBER: _ClassVar[int]
    PHYS_STATE_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    port: int
    state: str
    state_id: int
    phys_state: str
    phys_state_id: int
    rate: int
    counters: InfinibandPortCounters
    hardware_counters: InfinibandPortHardwareCounters
    def __init__(self, name: _Optional[str] = ..., port: _Optional[int] = ..., state: _Optional[str] = ..., state_id: _Optional[int] = ..., phys_state: _Optional[str] = ..., phys_state_id: _Optional[int] = ..., rate: _Optional[int] = ..., counters: _Optional[_Union[InfinibandPortCounters, _Mapping]] = ..., hardware_counters: _Optional[_Union[InfinibandPortHardwareCounters, _Mapping]] = ...) -> None: ...

class InfinibandPortCounters(_message.Message):
    __slots__ = ("excessive_buffer_overrun_errors", "link_downed", "link_error_recovery", "local_link_integrity_errors", "multicast_rcv_packets", "multicast_xmit_packets", "port_rcv_constraint_errors", "port_rcv_data", "port_rcv_discards", "port_rcv_errors", "port_rcv_packets", "port_rcv_remote_physical_errors", "port_rcv_switch_relay_errors", "port_xmit_constraint_errors", "port_xmit_data", "port_xmit_discards", "port_xmit_packets", "port_xmit_wait", "symbol_error", "unicast_rcv_packets", "unicast_xmit_packets", "vl15_dropped")
    EXCESSIVE_BUFFER_OVERRUN_ERRORS_FIELD_NUMBER: _ClassVar[int]
    LINK_DOWNED_FIELD_NUMBER: _ClassVar[int]
    LINK_ERROR_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    LOCAL_LINK_INTEGRITY_ERRORS_FIELD_NUMBER: _ClassVar[int]
    MULTICAST_RCV_PACKETS_FIELD_NUMBER: _ClassVar[int]
    MULTICAST_XMIT_PACKETS_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_CONSTRAINT_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_DATA_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_DISCARDS_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_PACKETS_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_REMOTE_PHYSICAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_SWITCH_RELAY_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PORT_XMIT_CONSTRAINT_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PORT_XMIT_DATA_FIELD_NUMBER: _ClassVar[int]
    PORT_XMIT_DISCARDS_FIELD_NUMBER: _ClassVar[int]
    PORT_XMIT_PACKETS_FIELD_NUMBER: _ClassVar[int]
    PORT_XMIT_WAIT_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_ERROR_FIELD_NUMBER: _ClassVar[int]
    UNICAST_RCV_PACKETS_FIELD_NUMBER: _ClassVar[int]
    UNICAST_XMIT_PACKETS_FIELD_NUMBER: _ClassVar[int]
    VL15_DROPPED_FIELD_NUMBER: _ClassVar[int]
    excessive_buffer_overrun_errors: int
    link_downed: int
    link_error_recovery: int
    local_link_integrity_errors: int
    multicast_rcv_packets: int
    multicast_xmit_packets: int
    port_rcv_constraint_errors: int
    port_rcv_data: int
    port_rcv_discards: int
    port_rcv_errors: int
    port_rcv_packets: int
    port_rcv_remote_physical_errors: int
    port_rcv_switch_relay_errors: int
    port_xmit_constraint_errors: int
    port_xmit_data: int
    port_xmit_discards: int
    port_xmit_packets: int
    port_xmit_wait: int
    symbol_error: int
    unicast_rcv_packets: int
    unicast_xmit_packets: int
    vl15_dropped: int
    def __init__(self, excessive_buffer_overrun_errors: _Optional[int] = ..., link_downed: _Optional[int] = ..., link_error_recovery: _Optional[int] = ..., local_link_integrity_errors: _Optional[int] = ..., multicast_rcv_packets: _Optional[int] = ..., multicast_xmit_packets: _Optional[int] = ..., port_rcv_constraint_errors: _Optional[int] = ..., port_rcv_data: _Optional[int] = ..., port_rcv_discards: _Optional[int] = ..., port_rcv_errors: _Optional[int] = ..., port_rcv_packets: _Optional[int] = ..., port_rcv_remote_physical_errors: _Optional[int] = ..., port_rcv_switch_relay_errors: _Optional[int] = ..., port_xmit_constraint_errors: _Optional[int] = ..., port_xmit_data: _Optional[int] = ..., port_xmit_discards: _Optional[int] = ..., port_xmit_packets: _Optional[int] = ..., port_xmit_wait: _Optional[int] = ..., symbol_error: _Optional[int] = ..., unicast_rcv_packets: _Optional[int] = ..., unicast_xmit_packets: _Optional[int] = ..., vl15_dropped: _Optional[int] = ...) -> None: ...

class InfinibandPortHardwareCounters(_message.Message):
    __slots__ = ("duplicate_request", "implied_nak_seq_err", "lifespan", "local_ack_timeout_err", "np_cnp_sent", "np_ecn_marked_roce_packets", "out_of_buffer", "out_of_sequence", "packet_seq_err", "req_cqe_error", "req_cqe_flush_error", "req_remote_access_errors", "req_remote_invalid_request", "resp_cqe_error", "resp_cqe_flush_error", "resp_local_length_error", "resp_remote_access_errors", "rnr_nak_retry_err", "roce_adp_retrans", "roce_adp_retrans_to", "roce_slow_restart", "roce_slow_restart_cnps", "roce_slow_restart_trans", "rp_cnp_handled", "rp_cnp_ignored", "rx_atomic_requests", "rx_dct_connect", "rx_icrc_encapsulated", "rx_read_requests", "rx_write_requests")
    DUPLICATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    IMPLIED_NAK_SEQ_ERR_FIELD_NUMBER: _ClassVar[int]
    LIFESPAN_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ACK_TIMEOUT_ERR_FIELD_NUMBER: _ClassVar[int]
    NP_CNP_SENT_FIELD_NUMBER: _ClassVar[int]
    NP_ECN_MARKED_ROCE_PACKETS_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_BUFFER_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PACKET_SEQ_ERR_FIELD_NUMBER: _ClassVar[int]
    REQ_CQE_ERROR_FIELD_NUMBER: _ClassVar[int]
    REQ_CQE_FLUSH_ERROR_FIELD_NUMBER: _ClassVar[int]
    REQ_REMOTE_ACCESS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    REQ_REMOTE_INVALID_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESP_CQE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESP_CQE_FLUSH_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESP_LOCAL_LENGTH_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESP_REMOTE_ACCESS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    RNR_NAK_RETRY_ERR_FIELD_NUMBER: _ClassVar[int]
    ROCE_ADP_RETRANS_FIELD_NUMBER: _ClassVar[int]
    ROCE_ADP_RETRANS_TO_FIELD_NUMBER: _ClassVar[int]
    ROCE_SLOW_RESTART_FIELD_NUMBER: _ClassVar[int]
    ROCE_SLOW_RESTART_CNPS_FIELD_NUMBER: _ClassVar[int]
    ROCE_SLOW_RESTART_TRANS_FIELD_NUMBER: _ClassVar[int]
    RP_CNP_HANDLED_FIELD_NUMBER: _ClassVar[int]
    RP_CNP_IGNORED_FIELD_NUMBER: _ClassVar[int]
    RX_ATOMIC_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    RX_DCT_CONNECT_FIELD_NUMBER: _ClassVar[int]
    RX_ICRC_ENCAPSULATED_FIELD_NUMBER: _ClassVar[int]
    RX_READ_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    RX_WRITE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    duplicate_request: int
    implied_nak_seq_err: int
    lifespan: int
    local_ack_timeout_err: int
    np_cnp_sent: int
    np_ecn_marked_roce_packets: int
    out_of_buffer: int
    out_of_sequence: int
    packet_seq_err: int
    req_cqe_error: int
    req_cqe_flush_error: int
    req_remote_access_errors: int
    req_remote_invalid_request: int
    resp_cqe_error: int
    resp_cqe_flush_error: int
    resp_local_length_error: int
    resp_remote_access_errors: int
    rnr_nak_retry_err: int
    roce_adp_retrans: int
    roce_adp_retrans_to: int
    roce_slow_restart: int
    roce_slow_restart_cnps: int
    roce_slow_restart_trans: int
    rp_cnp_handled: int
    rp_cnp_ignored: int
    rx_atomic_requests: int
    rx_dct_connect: int
    rx_icrc_encapsulated: int
    rx_read_requests: int
    rx_write_requests: int
    def __init__(self, duplicate_request: _Optional[int] = ..., implied_nak_seq_err: _Optional[int] = ..., lifespan: _Optional[int] = ..., local_ack_timeout_err: _Optional[int] = ..., np_cnp_sent: _Optional[int] = ..., np_ecn_marked_roce_packets: _Optional[int] = ..., out_of_buffer: _Optional[int] = ..., out_of_sequence: _Optional[int] = ..., packet_seq_err: _Optional[int] = ..., req_cqe_error: _Optional[int] = ..., req_cqe_flush_error: _Optional[int] = ..., req_remote_access_errors: _Optional[int] = ..., req_remote_invalid_request: _Optional[int] = ..., resp_cqe_error: _Optional[int] = ..., resp_cqe_flush_error: _Optional[int] = ..., resp_local_length_error: _Optional[int] = ..., resp_remote_access_errors: _Optional[int] = ..., rnr_nak_retry_err: _Optional[int] = ..., roce_adp_retrans: _Optional[int] = ..., roce_adp_retrans_to: _Optional[int] = ..., roce_slow_restart: _Optional[int] = ..., roce_slow_restart_cnps: _Optional[int] = ..., roce_slow_restart_trans: _Optional[int] = ..., rp_cnp_handled: _Optional[int] = ..., rp_cnp_ignored: _Optional[int] = ..., rx_atomic_requests: _Optional[int] = ..., rx_dct_connect: _Optional[int] = ..., rx_icrc_encapsulated: _Optional[int] = ..., rx_read_requests: _Optional[int] = ..., rx_write_requests: _Optional[int] = ...) -> None: ...

class DiskPartition(_message.Message):
    __slots__ = ("mount_point", "total", "free", "utilization", "device")
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    FREE_FIELD_NUMBER: _ClassVar[int]
    UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    mount_point: str
    total: int
    free: int
    utilization: float
    device: str
    def __init__(self, mount_point: _Optional[str] = ..., total: _Optional[int] = ..., free: _Optional[int] = ..., utilization: _Optional[float] = ..., device: _Optional[str] = ...) -> None: ...

class CpusSummary(_message.Message):
    __slots__ = ("count", "throttled_percentage", "average_current_clock_speed", "average_maximum_clock_speed", "cpus_per_governor")
    class CpusPerGovernorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    COUNT_FIELD_NUMBER: _ClassVar[int]
    THROTTLED_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_CURRENT_CLOCK_SPEED_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_MAXIMUM_CLOCK_SPEED_FIELD_NUMBER: _ClassVar[int]
    CPUS_PER_GOVERNOR_FIELD_NUMBER: _ClassVar[int]
    count: int
    throttled_percentage: float
    average_current_clock_speed: float
    average_maximum_clock_speed: float
    cpus_per_governor: _containers.ScalarMap[str, int]
    def __init__(self, count: _Optional[int] = ..., throttled_percentage: _Optional[float] = ..., average_current_clock_speed: _Optional[float] = ..., average_maximum_clock_speed: _Optional[float] = ..., cpus_per_governor: _Optional[_Mapping[str, int]] = ...) -> None: ...

class Memory(_message.Message):
    __slots__ = ("total", "free", "available", "active", "swap_total", "swap_free")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    FREE_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SWAP_TOTAL_FIELD_NUMBER: _ClassVar[int]
    SWAP_FREE_FIELD_NUMBER: _ClassVar[int]
    total: int
    free: int
    available: int
    active: int
    swap_total: int
    swap_free: int
    def __init__(self, total: _Optional[int] = ..., free: _Optional[int] = ..., available: _Optional[int] = ..., active: _Optional[int] = ..., swap_total: _Optional[int] = ..., swap_free: _Optional[int] = ...) -> None: ...

class SystemConfiguration(_message.Message):
    __slots__ = ("ips", "architecture", "build", "family", "platform", "version", "boot_time")
    IPS_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BOOT_TIME_FIELD_NUMBER: _ClassVar[int]
    ips: _containers.RepeatedScalarFieldContainer[str]
    architecture: str
    build: str
    family: str
    platform: str
    version: str
    boot_time: _timestamp_pb2.Timestamp
    def __init__(self, ips: _Optional[_Iterable[str]] = ..., architecture: _Optional[str] = ..., build: _Optional[str] = ..., family: _Optional[str] = ..., platform: _Optional[str] = ..., version: _Optional[str] = ..., boot_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class IngestNodeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IngestAgentStatsRequest(_message.Message):
    __slots__ = ("host_name", "scraped_at", "agent_version", "uptime", "goroutines", "file_descriptors", "resident_memory", "virtual_memory", "threads", "cpu_utilization", "memory_utilization")
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    SCRAPED_AT_FIELD_NUMBER: _ClassVar[int]
    AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    GOROUTINES_FIELD_NUMBER: _ClassVar[int]
    FILE_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    RESIDENT_MEMORY_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_MEMORY_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    CPU_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    MEMORY_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    host_name: str
    scraped_at: _timestamp_pb2.Timestamp
    agent_version: str
    uptime: int
    goroutines: int
    file_descriptors: int
    resident_memory: int
    virtual_memory: int
    threads: int
    cpu_utilization: float
    memory_utilization: float
    def __init__(self, host_name: _Optional[str] = ..., scraped_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., agent_version: _Optional[str] = ..., uptime: _Optional[int] = ..., goroutines: _Optional[int] = ..., file_descriptors: _Optional[int] = ..., resident_memory: _Optional[int] = ..., virtual_memory: _Optional[int] = ..., threads: _Optional[int] = ..., cpu_utilization: _Optional[float] = ..., memory_utilization: _Optional[float] = ...) -> None: ...

class IngestAgentStatsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IngestNodeMetricsRequest(_message.Message):
    __slots__ = ("hostname", "scraped_at_unix_seconds", "cpu_utilization", "gpu_metrics", "slurm_cluster")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    SCRAPED_AT_UNIX_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CPU_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    GPU_METRICS_FIELD_NUMBER: _ClassVar[int]
    SLURM_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    scraped_at_unix_seconds: int
    cpu_utilization: float
    gpu_metrics: _containers.RepeatedCompositeFieldContainer[GPUMetrics]
    slurm_cluster: str
    def __init__(self, hostname: _Optional[str] = ..., scraped_at_unix_seconds: _Optional[int] = ..., cpu_utilization: _Optional[float] = ..., gpu_metrics: _Optional[_Iterable[_Union[GPUMetrics, _Mapping]]] = ..., slurm_cluster: _Optional[str] = ...) -> None: ...

class IngestNodeMetricsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GPUMetrics(_message.Message):
    __slots__ = ("name", "uuid", "serial", "index", "memory_used", "memory_total", "memory_utilization", "utilization", "temperature_celsius", "power_draw_milliwatts")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USED_FIELD_NUMBER: _ClassVar[int]
    MEMORY_TOTAL_FIELD_NUMBER: _ClassVar[int]
    MEMORY_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    POWER_DRAW_MILLIWATTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uuid: str
    serial: str
    index: int
    memory_used: int
    memory_total: int
    memory_utilization: int
    utilization: int
    temperature_celsius: int
    power_draw_milliwatts: int
    def __init__(self, name: _Optional[str] = ..., uuid: _Optional[str] = ..., serial: _Optional[str] = ..., index: _Optional[int] = ..., memory_used: _Optional[int] = ..., memory_total: _Optional[int] = ..., memory_utilization: _Optional[int] = ..., utilization: _Optional[int] = ..., temperature_celsius: _Optional[int] = ..., power_draw_milliwatts: _Optional[int] = ...) -> None: ...

class GPUProcessMetrics(_message.Message):
    __slots__ = ("run_time", "file_descriptors", "resident_memory_bytes", "virtual_memory", "threads", "cpu_utilization", "memory_utilization", "gpu_memory_utilization")
    RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    FILE_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    RESIDENT_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_MEMORY_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    CPU_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    MEMORY_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    GPU_MEMORY_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    run_time: int
    file_descriptors: int
    resident_memory_bytes: int
    virtual_memory: int
    threads: int
    cpu_utilization: float
    memory_utilization: float
    gpu_memory_utilization: float
    def __init__(self, run_time: _Optional[int] = ..., file_descriptors: _Optional[int] = ..., resident_memory_bytes: _Optional[int] = ..., virtual_memory: _Optional[int] = ..., threads: _Optional[int] = ..., cpu_utilization: _Optional[float] = ..., memory_utilization: _Optional[float] = ..., gpu_memory_utilization: _Optional[float] = ...) -> None: ...

class InfinibandDeviceMetrics(_message.Message):
    __slots__ = ("name", "ports")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    ports: _containers.RepeatedCompositeFieldContainer[InfinibandPortMetrics]
    def __init__(self, name: _Optional[str] = ..., ports: _Optional[_Iterable[_Union[InfinibandPortMetrics, _Mapping]]] = ...) -> None: ...

class InfinibandPortMetrics(_message.Message):
    __slots__ = ("infiniband_port_counters", "infiniband_port_hardware_counters")
    INFINIBAND_PORT_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    INFINIBAND_PORT_HARDWARE_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    infiniband_port_counters: InfinibandPortCounterMetrics
    infiniband_port_hardware_counters: InfinibandPortHardwareCounterMetrics
    def __init__(self, infiniband_port_counters: _Optional[_Union[InfinibandPortCounterMetrics, _Mapping]] = ..., infiniband_port_hardware_counters: _Optional[_Union[InfinibandPortHardwareCounterMetrics, _Mapping]] = ...) -> None: ...

class InfinibandPortCounterMetrics(_message.Message):
    __slots__ = ("excessive_buffer_overrun_errors", "link_downed", "link_error_recovery", "local_link_integrity_errors", "multicast_rcv_packets", "multicast_xmit_packets", "port_rcv_constraint_errors", "port_rcv_data", "port_rcv_discards", "port_rcv_errors", "port_rcv_packets", "port_rcv_remote_physical_errors", "port_rcv_switch_relay_errors", "port_xmit_constraint_errors", "port_xmit_data", "port_xmit_discards", "port_xmit_packets", "port_xmit_wait", "symbol_error", "unicast_rcv_packets", "unicast_xmit_packets", "vl15_dropped")
    EXCESSIVE_BUFFER_OVERRUN_ERRORS_FIELD_NUMBER: _ClassVar[int]
    LINK_DOWNED_FIELD_NUMBER: _ClassVar[int]
    LINK_ERROR_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    LOCAL_LINK_INTEGRITY_ERRORS_FIELD_NUMBER: _ClassVar[int]
    MULTICAST_RCV_PACKETS_FIELD_NUMBER: _ClassVar[int]
    MULTICAST_XMIT_PACKETS_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_CONSTRAINT_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_DATA_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_DISCARDS_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_PACKETS_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_REMOTE_PHYSICAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PORT_RCV_SWITCH_RELAY_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PORT_XMIT_CONSTRAINT_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PORT_XMIT_DATA_FIELD_NUMBER: _ClassVar[int]
    PORT_XMIT_DISCARDS_FIELD_NUMBER: _ClassVar[int]
    PORT_XMIT_PACKETS_FIELD_NUMBER: _ClassVar[int]
    PORT_XMIT_WAIT_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_ERROR_FIELD_NUMBER: _ClassVar[int]
    UNICAST_RCV_PACKETS_FIELD_NUMBER: _ClassVar[int]
    UNICAST_XMIT_PACKETS_FIELD_NUMBER: _ClassVar[int]
    VL15_DROPPED_FIELD_NUMBER: _ClassVar[int]
    excessive_buffer_overrun_errors: int
    link_downed: int
    link_error_recovery: int
    local_link_integrity_errors: int
    multicast_rcv_packets: int
    multicast_xmit_packets: int
    port_rcv_constraint_errors: int
    port_rcv_data: int
    port_rcv_discards: int
    port_rcv_errors: int
    port_rcv_packets: int
    port_rcv_remote_physical_errors: int
    port_rcv_switch_relay_errors: int
    port_xmit_constraint_errors: int
    port_xmit_data: int
    port_xmit_discards: int
    port_xmit_packets: int
    port_xmit_wait: int
    symbol_error: int
    unicast_rcv_packets: int
    unicast_xmit_packets: int
    vl15_dropped: int
    def __init__(self, excessive_buffer_overrun_errors: _Optional[int] = ..., link_downed: _Optional[int] = ..., link_error_recovery: _Optional[int] = ..., local_link_integrity_errors: _Optional[int] = ..., multicast_rcv_packets: _Optional[int] = ..., multicast_xmit_packets: _Optional[int] = ..., port_rcv_constraint_errors: _Optional[int] = ..., port_rcv_data: _Optional[int] = ..., port_rcv_discards: _Optional[int] = ..., port_rcv_errors: _Optional[int] = ..., port_rcv_packets: _Optional[int] = ..., port_rcv_remote_physical_errors: _Optional[int] = ..., port_rcv_switch_relay_errors: _Optional[int] = ..., port_xmit_constraint_errors: _Optional[int] = ..., port_xmit_data: _Optional[int] = ..., port_xmit_discards: _Optional[int] = ..., port_xmit_packets: _Optional[int] = ..., port_xmit_wait: _Optional[int] = ..., symbol_error: _Optional[int] = ..., unicast_rcv_packets: _Optional[int] = ..., unicast_xmit_packets: _Optional[int] = ..., vl15_dropped: _Optional[int] = ...) -> None: ...

class InfinibandPortHardwareCounterMetrics(_message.Message):
    __slots__ = ("duplicate_request", "implied_nak_seq_err", "lifespan", "local_ack_timeout_err", "np_cnp_sent", "np_ecn_marked_roce_packets", "out_of_buffer", "out_of_sequence", "packet_seq_err", "req_cqe_error", "req_cqe_flush_error", "req_remote_access_errors", "req_remote_invalid_request", "resp_cqe_error", "resp_cqe_flush_error", "resp_local_length_error", "resp_remote_access_errors", "rnr_nak_retry_err", "roce_adp_retrans", "roce_adp_retrans_to", "roce_slow_restart", "roce_slow_restart_cnps", "roce_slow_restart_trans", "rp_cnp_handled", "rp_cnp_ignored", "rx_atomic_requests", "rx_dct_connect", "rx_icrc_encapsulated", "rx_read_requests", "rx_write_requests")
    DUPLICATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    IMPLIED_NAK_SEQ_ERR_FIELD_NUMBER: _ClassVar[int]
    LIFESPAN_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ACK_TIMEOUT_ERR_FIELD_NUMBER: _ClassVar[int]
    NP_CNP_SENT_FIELD_NUMBER: _ClassVar[int]
    NP_ECN_MARKED_ROCE_PACKETS_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_BUFFER_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PACKET_SEQ_ERR_FIELD_NUMBER: _ClassVar[int]
    REQ_CQE_ERROR_FIELD_NUMBER: _ClassVar[int]
    REQ_CQE_FLUSH_ERROR_FIELD_NUMBER: _ClassVar[int]
    REQ_REMOTE_ACCESS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    REQ_REMOTE_INVALID_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESP_CQE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESP_CQE_FLUSH_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESP_LOCAL_LENGTH_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESP_REMOTE_ACCESS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    RNR_NAK_RETRY_ERR_FIELD_NUMBER: _ClassVar[int]
    ROCE_ADP_RETRANS_FIELD_NUMBER: _ClassVar[int]
    ROCE_ADP_RETRANS_TO_FIELD_NUMBER: _ClassVar[int]
    ROCE_SLOW_RESTART_FIELD_NUMBER: _ClassVar[int]
    ROCE_SLOW_RESTART_CNPS_FIELD_NUMBER: _ClassVar[int]
    ROCE_SLOW_RESTART_TRANS_FIELD_NUMBER: _ClassVar[int]
    RP_CNP_HANDLED_FIELD_NUMBER: _ClassVar[int]
    RP_CNP_IGNORED_FIELD_NUMBER: _ClassVar[int]
    RX_ATOMIC_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    RX_DCT_CONNECT_FIELD_NUMBER: _ClassVar[int]
    RX_ICRC_ENCAPSULATED_FIELD_NUMBER: _ClassVar[int]
    RX_READ_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    RX_WRITE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    duplicate_request: int
    implied_nak_seq_err: int
    lifespan: int
    local_ack_timeout_err: int
    np_cnp_sent: int
    np_ecn_marked_roce_packets: int
    out_of_buffer: int
    out_of_sequence: int
    packet_seq_err: int
    req_cqe_error: int
    req_cqe_flush_error: int
    req_remote_access_errors: int
    req_remote_invalid_request: int
    resp_cqe_error: int
    resp_cqe_flush_error: int
    resp_local_length_error: int
    resp_remote_access_errors: int
    rnr_nak_retry_err: int
    roce_adp_retrans: int
    roce_adp_retrans_to: int
    roce_slow_restart: int
    roce_slow_restart_cnps: int
    roce_slow_restart_trans: int
    rp_cnp_handled: int
    rp_cnp_ignored: int
    rx_atomic_requests: int
    rx_dct_connect: int
    rx_icrc_encapsulated: int
    rx_read_requests: int
    rx_write_requests: int
    def __init__(self, duplicate_request: _Optional[int] = ..., implied_nak_seq_err: _Optional[int] = ..., lifespan: _Optional[int] = ..., local_ack_timeout_err: _Optional[int] = ..., np_cnp_sent: _Optional[int] = ..., np_ecn_marked_roce_packets: _Optional[int] = ..., out_of_buffer: _Optional[int] = ..., out_of_sequence: _Optional[int] = ..., packet_seq_err: _Optional[int] = ..., req_cqe_error: _Optional[int] = ..., req_cqe_flush_error: _Optional[int] = ..., req_remote_access_errors: _Optional[int] = ..., req_remote_invalid_request: _Optional[int] = ..., resp_cqe_error: _Optional[int] = ..., resp_cqe_flush_error: _Optional[int] = ..., resp_local_length_error: _Optional[int] = ..., resp_remote_access_errors: _Optional[int] = ..., rnr_nak_retry_err: _Optional[int] = ..., roce_adp_retrans: _Optional[int] = ..., roce_adp_retrans_to: _Optional[int] = ..., roce_slow_restart: _Optional[int] = ..., roce_slow_restart_cnps: _Optional[int] = ..., roce_slow_restart_trans: _Optional[int] = ..., rp_cnp_handled: _Optional[int] = ..., rp_cnp_ignored: _Optional[int] = ..., rx_atomic_requests: _Optional[int] = ..., rx_dct_connect: _Optional[int] = ..., rx_icrc_encapsulated: _Optional[int] = ..., rx_read_requests: _Optional[int] = ..., rx_write_requests: _Optional[int] = ...) -> None: ...

class AWSInstanceMetadata(_message.Message):
    __slots__ = ("account_id", "instance_id", "region", "vpc_id", "subnet_id", "availability_zone", "ami", "instance_type", "tags")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    AMI_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    instance_id: str
    region: str
    vpc_id: str
    subnet_id: str
    availability_zone: str
    ami: str
    instance_type: str
    tags: _containers.ScalarMap[str, str]
    def __init__(self, account_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., region: _Optional[str] = ..., vpc_id: _Optional[str] = ..., subnet_id: _Optional[str] = ..., availability_zone: _Optional[str] = ..., ami: _Optional[str] = ..., instance_type: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class IngestProcessMetricsAlphaV1Request(_message.Message):
    __slots__ = ("process_metrics",)
    PROCESS_METRICS_FIELD_NUMBER: _ClassVar[int]
    process_metrics: ProcessMetricsAlphaV1
    def __init__(self, process_metrics: _Optional[_Union[ProcessMetricsAlphaV1, _Mapping]] = ...) -> None: ...

class IngestProcessMetricsAlphaV1Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProcessMetricsAlphaV1(_message.Message):
    __slots__ = ("tenant_id", "command_id", "launch_id", "hostname", "scraped_at", "cpu_utilization", "gpu_memory_used_kilobytes", "gpu_memory_utilization")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_ID_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    SCRAPED_AT_FIELD_NUMBER: _ClassVar[int]
    CPU_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    GPU_MEMORY_USED_KILOBYTES_FIELD_NUMBER: _ClassVar[int]
    GPU_MEMORY_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    command_id: str
    launch_id: str
    hostname: str
    scraped_at: _timestamp_pb2.Timestamp
    cpu_utilization: _wrappers_pb2.FloatValue
    gpu_memory_used_kilobytes: _wrappers_pb2.UInt64Value
    gpu_memory_utilization: _wrappers_pb2.FloatValue
    def __init__(self, tenant_id: _Optional[str] = ..., command_id: _Optional[str] = ..., launch_id: _Optional[str] = ..., hostname: _Optional[str] = ..., scraped_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cpu_utilization: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., gpu_memory_used_kilobytes: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., gpu_memory_utilization: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class IngestSlurmJobsRequest(_message.Message):
    __slots__ = ("jobs",)
    JOBS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[SlurmJob]
    def __init__(self, jobs: _Optional[_Iterable[_Union[SlurmJob, _Mapping]]] = ...) -> None: ...

class Link(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class SlurmJob(_message.Message):
    __slots__ = ("tenant_id", "cluster", "job_id", "job_name", "partition", "account", "user", "state", "exit_code", "submit", "start", "end", "nodes", "work_dir", "submit_line", "std_out", "std_err", "extra", "batch_script", "source_hostname", "log_files", "links", "alloc_cpus", "max_rss_bytes", "req_cpus", "req_mem_bytes", "alloc_tres", "req_tres", "alloc_gpus", "req_gpus", "array_job_master_id", "array_job_index", "alloc_tres_parsed", "req_tres_parsed", "gres_detail")
    class AllocTresParsedEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class ReqTresParsedEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    WORK_DIR_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_LINE_FIELD_NUMBER: _ClassVar[int]
    STD_OUT_FIELD_NUMBER: _ClassVar[int]
    STD_ERR_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    BATCH_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    LOG_FILES_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    ALLOC_CPUS_FIELD_NUMBER: _ClassVar[int]
    MAX_RSS_BYTES_FIELD_NUMBER: _ClassVar[int]
    REQ_CPUS_FIELD_NUMBER: _ClassVar[int]
    REQ_MEM_BYTES_FIELD_NUMBER: _ClassVar[int]
    ALLOC_TRES_FIELD_NUMBER: _ClassVar[int]
    REQ_TRES_FIELD_NUMBER: _ClassVar[int]
    ALLOC_GPUS_FIELD_NUMBER: _ClassVar[int]
    REQ_GPUS_FIELD_NUMBER: _ClassVar[int]
    ARRAY_JOB_MASTER_ID_FIELD_NUMBER: _ClassVar[int]
    ARRAY_JOB_INDEX_FIELD_NUMBER: _ClassVar[int]
    ALLOC_TRES_PARSED_FIELD_NUMBER: _ClassVar[int]
    REQ_TRES_PARSED_FIELD_NUMBER: _ClassVar[int]
    GRES_DETAIL_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    cluster: str
    job_id: str
    job_name: str
    partition: str
    account: str
    user: str
    state: str
    exit_code: str
    submit: _timestamp_pb2.Timestamp
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    nodes: _containers.RepeatedScalarFieldContainer[str]
    work_dir: str
    submit_line: str
    std_out: str
    std_err: str
    extra: str
    batch_script: str
    source_hostname: str
    log_files: _containers.RepeatedCompositeFieldContainer[SlurmLogFile]
    links: _containers.RepeatedCompositeFieldContainer[Link]
    alloc_cpus: int
    max_rss_bytes: int
    req_cpus: int
    req_mem_bytes: int
    alloc_tres: str
    req_tres: str
    alloc_gpus: int
    req_gpus: int
    array_job_master_id: str
    array_job_index: str
    alloc_tres_parsed: _containers.ScalarMap[str, int]
    req_tres_parsed: _containers.ScalarMap[str, int]
    gres_detail: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tenant_id: _Optional[str] = ..., cluster: _Optional[str] = ..., job_id: _Optional[str] = ..., job_name: _Optional[str] = ..., partition: _Optional[str] = ..., account: _Optional[str] = ..., user: _Optional[str] = ..., state: _Optional[str] = ..., exit_code: _Optional[str] = ..., submit: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., nodes: _Optional[_Iterable[str]] = ..., work_dir: _Optional[str] = ..., submit_line: _Optional[str] = ..., std_out: _Optional[str] = ..., std_err: _Optional[str] = ..., extra: _Optional[str] = ..., batch_script: _Optional[str] = ..., source_hostname: _Optional[str] = ..., log_files: _Optional[_Iterable[_Union[SlurmLogFile, _Mapping]]] = ..., links: _Optional[_Iterable[_Union[Link, _Mapping]]] = ..., alloc_cpus: _Optional[int] = ..., max_rss_bytes: _Optional[int] = ..., req_cpus: _Optional[int] = ..., req_mem_bytes: _Optional[int] = ..., alloc_tres: _Optional[str] = ..., req_tres: _Optional[str] = ..., alloc_gpus: _Optional[int] = ..., req_gpus: _Optional[int] = ..., array_job_master_id: _Optional[str] = ..., array_job_index: _Optional[str] = ..., alloc_tres_parsed: _Optional[_Mapping[str, int]] = ..., req_tres_parsed: _Optional[_Mapping[str, int]] = ..., gres_detail: _Optional[_Iterable[str]] = ...) -> None: ...

class SlurmLogFile(_message.Message):
    __slots__ = ("path", "content", "last_modified", "collected_at", "hash", "append_content")
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    COLLECTED_AT_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    APPEND_CONTENT_FIELD_NUMBER: _ClassVar[int]
    path: str
    content: bytes
    last_modified: _timestamp_pb2.Timestamp
    collected_at: _timestamp_pb2.Timestamp
    hash: str
    append_content: bytes
    def __init__(self, path: _Optional[str] = ..., content: _Optional[bytes] = ..., last_modified: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., collected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hash: _Optional[str] = ..., append_content: _Optional[bytes] = ...) -> None: ...

class IngestSlurmJobsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IngestSlurmNodesRequest(_message.Message):
    __slots__ = ("nodes",)
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[SlurmNode]
    def __init__(self, nodes: _Optional[_Iterable[_Union[SlurmNode, _Mapping]]] = ...) -> None: ...

class SlurmNode(_message.Message):
    __slots__ = ("tenant_id", "hostname", "scraped_at", "partitions", "available", "state", "reason", "cpus", "gres", "gres_used", "source_hostname")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    SCRAPED_AT_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    CPUS_FIELD_NUMBER: _ClassVar[int]
    GRES_FIELD_NUMBER: _ClassVar[int]
    GRES_USED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    hostname: str
    scraped_at: _timestamp_pb2.Timestamp
    partitions: _containers.RepeatedScalarFieldContainer[str]
    available: str
    state: str
    reason: str
    cpus: int
    gres: str
    gres_used: str
    source_hostname: str
    def __init__(self, tenant_id: _Optional[str] = ..., hostname: _Optional[str] = ..., scraped_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., partitions: _Optional[_Iterable[str]] = ..., available: _Optional[str] = ..., state: _Optional[str] = ..., reason: _Optional[str] = ..., cpus: _Optional[int] = ..., gres: _Optional[str] = ..., gres_used: _Optional[str] = ..., source_hostname: _Optional[str] = ...) -> None: ...

class IngestSlurmNodesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FudgeletConfig(_message.Message):
    __slots__ = ("config_file_contents", "config_file_path", "working_directory", "executable_path", "runtime_args")
    CONFIG_FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    EXECUTABLE_PATH_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_ARGS_FIELD_NUMBER: _ClassVar[int]
    config_file_contents: str
    config_file_path: str
    working_directory: str
    executable_path: str
    runtime_args: str
    def __init__(self, config_file_contents: _Optional[str] = ..., config_file_path: _Optional[str] = ..., working_directory: _Optional[str] = ..., executable_path: _Optional[str] = ..., runtime_args: _Optional[str] = ...) -> None: ...
