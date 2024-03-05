# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ..exec import exec_pb2 as exec_dot_exec__pb2


class ExecStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BulkCreateCommand = channel.unary_unary(
                '/clusterfudge.Exec/BulkCreateCommand',
                request_serializer=exec_dot_exec__pb2.BulkCreateCommandRequest.SerializeToString,
                response_deserializer=exec_dot_exec__pb2.BulkCreateCommandResponse.FromString,
                )
        self.CreateCommand = channel.unary_unary(
                '/clusterfudge.Exec/CreateCommand',
                request_serializer=exec_dot_exec__pb2.CreateCommandRequest.SerializeToString,
                response_deserializer=exec_dot_exec__pb2.Command.FromString,
                )
        self.GetCommand = channel.unary_unary(
                '/clusterfudge.Exec/GetCommand',
                request_serializer=exec_dot_exec__pb2.GetCommandRequest.SerializeToString,
                response_deserializer=exec_dot_exec__pb2.Command.FromString,
                )
        self.ListCommands = channel.unary_unary(
                '/clusterfudge.Exec/ListCommands',
                request_serializer=exec_dot_exec__pb2.ListCommandsRequest.SerializeToString,
                response_deserializer=exec_dot_exec__pb2.ListCommandsResponse.FromString,
                )
        self.UpdateCommand = channel.unary_unary(
                '/clusterfudge.Exec/UpdateCommand',
                request_serializer=exec_dot_exec__pb2.UpdateCommandRequest.SerializeToString,
                response_deserializer=exec_dot_exec__pb2.Command.FromString,
                )


class ExecServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BulkCreateCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCommands(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExecServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BulkCreateCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.BulkCreateCommand,
                    request_deserializer=exec_dot_exec__pb2.BulkCreateCommandRequest.FromString,
                    response_serializer=exec_dot_exec__pb2.BulkCreateCommandResponse.SerializeToString,
            ),
            'CreateCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCommand,
                    request_deserializer=exec_dot_exec__pb2.CreateCommandRequest.FromString,
                    response_serializer=exec_dot_exec__pb2.Command.SerializeToString,
            ),
            'GetCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCommand,
                    request_deserializer=exec_dot_exec__pb2.GetCommandRequest.FromString,
                    response_serializer=exec_dot_exec__pb2.Command.SerializeToString,
            ),
            'ListCommands': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCommands,
                    request_deserializer=exec_dot_exec__pb2.ListCommandsRequest.FromString,
                    response_serializer=exec_dot_exec__pb2.ListCommandsResponse.SerializeToString,
            ),
            'UpdateCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCommand,
                    request_deserializer=exec_dot_exec__pb2.UpdateCommandRequest.FromString,
                    response_serializer=exec_dot_exec__pb2.Command.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'clusterfudge.Exec', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Exec(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BulkCreateCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Exec/BulkCreateCommand',
            exec_dot_exec__pb2.BulkCreateCommandRequest.SerializeToString,
            exec_dot_exec__pb2.BulkCreateCommandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Exec/CreateCommand',
            exec_dot_exec__pb2.CreateCommandRequest.SerializeToString,
            exec_dot_exec__pb2.Command.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Exec/GetCommand',
            exec_dot_exec__pb2.GetCommandRequest.SerializeToString,
            exec_dot_exec__pb2.Command.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCommands(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Exec/ListCommands',
            exec_dot_exec__pb2.ListCommandsRequest.SerializeToString,
            exec_dot_exec__pb2.ListCommandsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Exec/UpdateCommand',
            exec_dot_exec__pb2.UpdateCommandRequest.SerializeToString,
            exec_dot_exec__pb2.Command.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
