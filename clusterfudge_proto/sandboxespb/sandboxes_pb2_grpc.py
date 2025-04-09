# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from ..sandboxespb import sandboxes_pb2 as sandboxespb_dot_sandboxes__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in sandboxespb/sandboxes_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class SandboxesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateSandbox = channel.unary_unary(
                '/sandboxespb.Sandboxes/CreateSandbox',
                request_serializer=sandboxespb_dot_sandboxes__pb2.CreateSandboxRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.CreateSandboxResponse.FromString,
                _registered_method=True)
        self.ListSandboxes = channel.unary_unary(
                '/sandboxespb.Sandboxes/ListSandboxes',
                request_serializer=sandboxespb_dot_sandboxes__pb2.ListSandboxesRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.ListSandboxesResponse.FromString,
                _registered_method=True)
        self.DeleteSandbox = channel.unary_unary(
                '/sandboxespb.Sandboxes/DeleteSandbox',
                request_serializer=sandboxespb_dot_sandboxes__pb2.DeleteSandboxRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.DeleteSandboxResponse.FromString,
                _registered_method=True)
        self.GetSandbox = channel.unary_unary(
                '/sandboxespb.Sandboxes/GetSandbox',
                request_serializer=sandboxespb_dot_sandboxes__pb2.GetSandboxRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.GetSandboxResponse.FromString,
                _registered_method=True)
        self.ComputerUse = channel.unary_unary(
                '/sandboxespb.Sandboxes/ComputerUse',
                request_serializer=sandboxespb_dot_sandboxes__pb2.ComputerUseRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.ComputerUseResponse.FromString,
                _registered_method=True)
        self.ClaudeComputerUse = channel.unary_unary(
                '/sandboxespb.Sandboxes/ClaudeComputerUse',
                request_serializer=sandboxespb_dot_sandboxes__pb2.ClaudeComputerUseRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.ClaudeComputerUseResponse.FromString,
                _registered_method=True)
        self.GetComputerUseRequestLogs = channel.unary_unary(
                '/sandboxespb.Sandboxes/GetComputerUseRequestLogs',
                request_serializer=sandboxespb_dot_sandboxes__pb2.GetComputerUseRequestLogsRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.GetComputerUseRequestLogsResponse.FromString,
                _registered_method=True)
        self.WriteToTerminal = channel.unary_unary(
                '/sandboxespb.Sandboxes/WriteToTerminal',
                request_serializer=sandboxespb_dot_sandboxes__pb2.WriteToTerminalRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.WriteToTerminalResponse.FromString,
                _registered_method=True)
        self.KillTerminal = channel.unary_unary(
                '/sandboxespb.Sandboxes/KillTerminal',
                request_serializer=sandboxespb_dot_sandboxes__pb2.KillTerminalRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.KillTerminalResponse.FromString,
                _registered_method=True)
        self.ResetTerminal = channel.unary_unary(
                '/sandboxespb.Sandboxes/ResetTerminal',
                request_serializer=sandboxespb_dot_sandboxes__pb2.ResetTerminalRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.ResetTerminalResponse.FromString,
                _registered_method=True)
        self.ResetAllTerminals = channel.unary_unary(
                '/sandboxespb.Sandboxes/ResetAllTerminals',
                request_serializer=sandboxespb_dot_sandboxes__pb2.ResetAllTerminalsRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.ResetAllTerminalsResponse.FromString,
                _registered_method=True)
        self.GetTerminalHistory = channel.unary_unary(
                '/sandboxespb.Sandboxes/GetTerminalHistory',
                request_serializer=sandboxespb_dot_sandboxes__pb2.GetTerminalHistoryRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.GetTerminalHistoryResponse.FromString,
                _registered_method=True)
        self.DownloadFile = channel.unary_unary(
                '/sandboxespb.Sandboxes/DownloadFile',
                request_serializer=sandboxespb_dot_sandboxes__pb2.DownloadFileRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.DownloadFileResponse.FromString,
                _registered_method=True)
        self.DownloadFolder = channel.unary_unary(
                '/sandboxespb.Sandboxes/DownloadFolder',
                request_serializer=sandboxespb_dot_sandboxes__pb2.DownloadFolderRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.DownloadFolderResponse.FromString,
                _registered_method=True)
        self.CreateFile = channel.unary_unary(
                '/sandboxespb.Sandboxes/CreateFile',
                request_serializer=sandboxespb_dot_sandboxes__pb2.CreateFileRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.CreateFileResponse.FromString,
                _registered_method=True)
        self.WriteToProcess = channel.unary_unary(
                '/sandboxespb.Sandboxes/WriteToProcess',
                request_serializer=sandboxespb_dot_sandboxes__pb2.WriteToProcessRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.WriteToProcessResponse.FromString,
                _registered_method=True)
        self.KillProcess = channel.unary_unary(
                '/sandboxespb.Sandboxes/KillProcess',
                request_serializer=sandboxespb_dot_sandboxes__pb2.KillProcessRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.KillProcessResponse.FromString,
                _registered_method=True)
        self.GetProcess = channel.unary_unary(
                '/sandboxespb.Sandboxes/GetProcess',
                request_serializer=sandboxespb_dot_sandboxes__pb2.GetProcessRequest.SerializeToString,
                response_deserializer=sandboxespb_dot_sandboxes__pb2.GetProcessResponse.FromString,
                _registered_method=True)


class SandboxesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateSandbox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSandboxes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSandbox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSandbox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ComputerUse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClaudeComputerUse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetComputerUseRequestLogs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteToTerminal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KillTerminal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetTerminal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetAllTerminals(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTerminalHistory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFolder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteToProcess(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KillProcess(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProcess(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SandboxesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateSandbox': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSandbox,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.CreateSandboxRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.CreateSandboxResponse.SerializeToString,
            ),
            'ListSandboxes': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSandboxes,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.ListSandboxesRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.ListSandboxesResponse.SerializeToString,
            ),
            'DeleteSandbox': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSandbox,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.DeleteSandboxRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.DeleteSandboxResponse.SerializeToString,
            ),
            'GetSandbox': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSandbox,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.GetSandboxRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.GetSandboxResponse.SerializeToString,
            ),
            'ComputerUse': grpc.unary_unary_rpc_method_handler(
                    servicer.ComputerUse,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.ComputerUseRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.ComputerUseResponse.SerializeToString,
            ),
            'ClaudeComputerUse': grpc.unary_unary_rpc_method_handler(
                    servicer.ClaudeComputerUse,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.ClaudeComputerUseRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.ClaudeComputerUseResponse.SerializeToString,
            ),
            'GetComputerUseRequestLogs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetComputerUseRequestLogs,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.GetComputerUseRequestLogsRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.GetComputerUseRequestLogsResponse.SerializeToString,
            ),
            'WriteToTerminal': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteToTerminal,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.WriteToTerminalRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.WriteToTerminalResponse.SerializeToString,
            ),
            'KillTerminal': grpc.unary_unary_rpc_method_handler(
                    servicer.KillTerminal,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.KillTerminalRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.KillTerminalResponse.SerializeToString,
            ),
            'ResetTerminal': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetTerminal,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.ResetTerminalRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.ResetTerminalResponse.SerializeToString,
            ),
            'ResetAllTerminals': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetAllTerminals,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.ResetAllTerminalsRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.ResetAllTerminalsResponse.SerializeToString,
            ),
            'GetTerminalHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTerminalHistory,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.GetTerminalHistoryRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.GetTerminalHistoryResponse.SerializeToString,
            ),
            'DownloadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.DownloadFileRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.DownloadFileResponse.SerializeToString,
            ),
            'DownloadFolder': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadFolder,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.DownloadFolderRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.DownloadFolderResponse.SerializeToString,
            ),
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.CreateFileRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.CreateFileResponse.SerializeToString,
            ),
            'WriteToProcess': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteToProcess,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.WriteToProcessRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.WriteToProcessResponse.SerializeToString,
            ),
            'KillProcess': grpc.unary_unary_rpc_method_handler(
                    servicer.KillProcess,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.KillProcessRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.KillProcessResponse.SerializeToString,
            ),
            'GetProcess': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProcess,
                    request_deserializer=sandboxespb_dot_sandboxes__pb2.GetProcessRequest.FromString,
                    response_serializer=sandboxespb_dot_sandboxes__pb2.GetProcessResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sandboxespb.Sandboxes', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('sandboxespb.Sandboxes', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Sandboxes(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateSandbox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/CreateSandbox',
            sandboxespb_dot_sandboxes__pb2.CreateSandboxRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.CreateSandboxResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListSandboxes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/ListSandboxes',
            sandboxespb_dot_sandboxes__pb2.ListSandboxesRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.ListSandboxesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteSandbox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/DeleteSandbox',
            sandboxespb_dot_sandboxes__pb2.DeleteSandboxRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.DeleteSandboxResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSandbox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/GetSandbox',
            sandboxespb_dot_sandboxes__pb2.GetSandboxRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.GetSandboxResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ComputerUse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/ComputerUse',
            sandboxespb_dot_sandboxes__pb2.ComputerUseRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.ComputerUseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ClaudeComputerUse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/ClaudeComputerUse',
            sandboxespb_dot_sandboxes__pb2.ClaudeComputerUseRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.ClaudeComputerUseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetComputerUseRequestLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/GetComputerUseRequestLogs',
            sandboxespb_dot_sandboxes__pb2.GetComputerUseRequestLogsRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.GetComputerUseRequestLogsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def WriteToTerminal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/WriteToTerminal',
            sandboxespb_dot_sandboxes__pb2.WriteToTerminalRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.WriteToTerminalResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def KillTerminal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/KillTerminal',
            sandboxespb_dot_sandboxes__pb2.KillTerminalRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.KillTerminalResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ResetTerminal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/ResetTerminal',
            sandboxespb_dot_sandboxes__pb2.ResetTerminalRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.ResetTerminalResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ResetAllTerminals(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/ResetAllTerminals',
            sandboxespb_dot_sandboxes__pb2.ResetAllTerminalsRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.ResetAllTerminalsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTerminalHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/GetTerminalHistory',
            sandboxespb_dot_sandboxes__pb2.GetTerminalHistoryRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.GetTerminalHistoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/DownloadFile',
            sandboxespb_dot_sandboxes__pb2.DownloadFileRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.DownloadFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DownloadFolder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/DownloadFolder',
            sandboxespb_dot_sandboxes__pb2.DownloadFolderRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.DownloadFolderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/CreateFile',
            sandboxespb_dot_sandboxes__pb2.CreateFileRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.CreateFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def WriteToProcess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/WriteToProcess',
            sandboxespb_dot_sandboxes__pb2.WriteToProcessRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.WriteToProcessResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def KillProcess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/KillProcess',
            sandboxespb_dot_sandboxes__pb2.KillProcessRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.KillProcessResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetProcess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/sandboxespb.Sandboxes/GetProcess',
            sandboxespb_dot_sandboxes__pb2.GetProcessRequest.SerializeToString,
            sandboxespb_dot_sandboxes__pb2.GetProcessResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
