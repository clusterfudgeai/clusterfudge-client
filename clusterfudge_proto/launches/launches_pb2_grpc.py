# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ..launches import launches_pb2 as launches_dot_launches__pb2


class LaunchesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLaunch = channel.unary_unary(
                '/clusterfudge.Launches/GetLaunch',
                request_serializer=launches_dot_launches__pb2.GetLaunchRequest.SerializeToString,
                response_deserializer=launches_dot_launches__pb2.Launch.FromString,
                )
        self.GetLaunchDetails = channel.unary_unary(
                '/clusterfudge.Launches/GetLaunchDetails',
                request_serializer=launches_dot_launches__pb2.GetLaunchDetailsRequest.SerializeToString,
                response_deserializer=launches_dot_launches__pb2.LaunchDetails.FromString,
                )
        self.ListLaunches = channel.unary_unary(
                '/clusterfudge.Launches/ListLaunches',
                request_serializer=launches_dot_launches__pb2.ListLaunchesRequest.SerializeToString,
                response_deserializer=launches_dot_launches__pb2.ListLaunchesResponse.FromString,
                )
        self.ListLaunchesWithCommandStatuses = channel.unary_unary(
                '/clusterfudge.Launches/ListLaunchesWithCommandStatuses',
                request_serializer=launches_dot_launches__pb2.ListLaunchesRequest.SerializeToString,
                response_deserializer=launches_dot_launches__pb2.ListLaunchesWithCommandStatusesResponse.FromString,
                )
        self.CreateLaunch = channel.unary_unary(
                '/clusterfudge.Launches/CreateLaunch',
                request_serializer=launches_dot_launches__pb2.CreateLaunchRequest.SerializeToString,
                response_deserializer=launches_dot_launches__pb2.Launch.FromString,
                )
        self.StopLaunch = channel.unary_unary(
                '/clusterfudge.Launches/StopLaunch',
                request_serializer=launches_dot_launches__pb2.StopLaunchRequest.SerializeToString,
                response_deserializer=launches_dot_launches__pb2.StopLaunchResponse.FromString,
                )
        self.RerunLaunch = channel.unary_unary(
                '/clusterfudge.Launches/RerunLaunch',
                request_serializer=launches_dot_launches__pb2.RerunLaunchRequest.SerializeToString,
                response_deserializer=launches_dot_launches__pb2.RerunLaunchResponse.FromString,
                )
        self.ListResources = channel.unary_unary(
                '/clusterfudge.Launches/ListResources',
                request_serializer=launches_dot_launches__pb2.ListResourcesRequest.SerializeToString,
                response_deserializer=launches_dot_launches__pb2.ListResourcesResponse.FromString,
                )
        self.DownloadZip = channel.unary_unary(
                '/clusterfudge.Launches/DownloadZip',
                request_serializer=launches_dot_launches__pb2.DownloadZipRequest.SerializeToString,
                response_deserializer=launches_dot_launches__pb2.DownloadZipResponse.FromString,
                )


class LaunchesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetLaunch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLaunchDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListLaunches(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListLaunchesWithCommandStatuses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateLaunch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopLaunch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RerunLaunch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListResources(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadZip(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LaunchesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLaunch': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLaunch,
                    request_deserializer=launches_dot_launches__pb2.GetLaunchRequest.FromString,
                    response_serializer=launches_dot_launches__pb2.Launch.SerializeToString,
            ),
            'GetLaunchDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLaunchDetails,
                    request_deserializer=launches_dot_launches__pb2.GetLaunchDetailsRequest.FromString,
                    response_serializer=launches_dot_launches__pb2.LaunchDetails.SerializeToString,
            ),
            'ListLaunches': grpc.unary_unary_rpc_method_handler(
                    servicer.ListLaunches,
                    request_deserializer=launches_dot_launches__pb2.ListLaunchesRequest.FromString,
                    response_serializer=launches_dot_launches__pb2.ListLaunchesResponse.SerializeToString,
            ),
            'ListLaunchesWithCommandStatuses': grpc.unary_unary_rpc_method_handler(
                    servicer.ListLaunchesWithCommandStatuses,
                    request_deserializer=launches_dot_launches__pb2.ListLaunchesRequest.FromString,
                    response_serializer=launches_dot_launches__pb2.ListLaunchesWithCommandStatusesResponse.SerializeToString,
            ),
            'CreateLaunch': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateLaunch,
                    request_deserializer=launches_dot_launches__pb2.CreateLaunchRequest.FromString,
                    response_serializer=launches_dot_launches__pb2.Launch.SerializeToString,
            ),
            'StopLaunch': grpc.unary_unary_rpc_method_handler(
                    servicer.StopLaunch,
                    request_deserializer=launches_dot_launches__pb2.StopLaunchRequest.FromString,
                    response_serializer=launches_dot_launches__pb2.StopLaunchResponse.SerializeToString,
            ),
            'RerunLaunch': grpc.unary_unary_rpc_method_handler(
                    servicer.RerunLaunch,
                    request_deserializer=launches_dot_launches__pb2.RerunLaunchRequest.FromString,
                    response_serializer=launches_dot_launches__pb2.RerunLaunchResponse.SerializeToString,
            ),
            'ListResources': grpc.unary_unary_rpc_method_handler(
                    servicer.ListResources,
                    request_deserializer=launches_dot_launches__pb2.ListResourcesRequest.FromString,
                    response_serializer=launches_dot_launches__pb2.ListResourcesResponse.SerializeToString,
            ),
            'DownloadZip': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadZip,
                    request_deserializer=launches_dot_launches__pb2.DownloadZipRequest.FromString,
                    response_serializer=launches_dot_launches__pb2.DownloadZipResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'clusterfudge.Launches', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Launches(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetLaunch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Launches/GetLaunch',
            launches_dot_launches__pb2.GetLaunchRequest.SerializeToString,
            launches_dot_launches__pb2.Launch.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLaunchDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Launches/GetLaunchDetails',
            launches_dot_launches__pb2.GetLaunchDetailsRequest.SerializeToString,
            launches_dot_launches__pb2.LaunchDetails.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListLaunches(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Launches/ListLaunches',
            launches_dot_launches__pb2.ListLaunchesRequest.SerializeToString,
            launches_dot_launches__pb2.ListLaunchesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListLaunchesWithCommandStatuses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Launches/ListLaunchesWithCommandStatuses',
            launches_dot_launches__pb2.ListLaunchesRequest.SerializeToString,
            launches_dot_launches__pb2.ListLaunchesWithCommandStatusesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateLaunch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Launches/CreateLaunch',
            launches_dot_launches__pb2.CreateLaunchRequest.SerializeToString,
            launches_dot_launches__pb2.Launch.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopLaunch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Launches/StopLaunch',
            launches_dot_launches__pb2.StopLaunchRequest.SerializeToString,
            launches_dot_launches__pb2.StopLaunchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RerunLaunch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Launches/RerunLaunch',
            launches_dot_launches__pb2.RerunLaunchRequest.SerializeToString,
            launches_dot_launches__pb2.RerunLaunchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Launches/ListResources',
            launches_dot_launches__pb2.ListResourcesRequest.SerializeToString,
            launches_dot_launches__pb2.ListResourcesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadZip(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clusterfudge.Launches/DownloadZip',
            launches_dot_launches__pb2.DownloadZipRequest.SerializeToString,
            launches_dot_launches__pb2.DownloadZipResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
