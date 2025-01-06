# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from ..slurmpb import slurm_pb2 as slurmpb_dot_slurm__pb2

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
        + f' but the generated code in slurmpb/slurm_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class SlurmStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSlurmJob = channel.unary_unary(
                '/clusterfudge.Slurm/GetSlurmJob',
                request_serializer=slurmpb_dot_slurm__pb2.GetSlurmJobRequest.SerializeToString,
                response_deserializer=slurmpb_dot_slurm__pb2.GetSlurmJobResponse.FromString,
                _registered_method=True)
        self.ListSlurmJobs = channel.unary_unary(
                '/clusterfudge.Slurm/ListSlurmJobs',
                request_serializer=slurmpb_dot_slurm__pb2.ListSlurmJobsRequest.SerializeToString,
                response_deserializer=slurmpb_dot_slurm__pb2.ListSlurmJobsResponse.FromString,
                _registered_method=True)
        self.ListSlurmNodes = channel.unary_unary(
                '/clusterfudge.Slurm/ListSlurmNodes',
                request_serializer=slurmpb_dot_slurm__pb2.ListSlurmNodesRequest.SerializeToString,
                response_deserializer=slurmpb_dot_slurm__pb2.ListSlurmNodesResponse.FromString,
                _registered_method=True)
        self.CancelSlurmJob = channel.unary_unary(
                '/clusterfudge.Slurm/CancelSlurmJob',
                request_serializer=slurmpb_dot_slurm__pb2.CancelSlurmJobRequest.SerializeToString,
                response_deserializer=slurmpb_dot_slurm__pb2.CancelSlurmJobResponse.FromString,
                _registered_method=True)
        self.LaunchJupyter = channel.unary_unary(
                '/clusterfudge.Slurm/LaunchJupyter',
                request_serializer=slurmpb_dot_slurm__pb2.LaunchJupyterRequest.SerializeToString,
                response_deserializer=slurmpb_dot_slurm__pb2.LaunchJupyterResponse.FromString,
                _registered_method=True)


class SlurmServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSlurmJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSlurmJobs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSlurmNodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelSlurmJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LaunchJupyter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SlurmServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSlurmJob': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSlurmJob,
                    request_deserializer=slurmpb_dot_slurm__pb2.GetSlurmJobRequest.FromString,
                    response_serializer=slurmpb_dot_slurm__pb2.GetSlurmJobResponse.SerializeToString,
            ),
            'ListSlurmJobs': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSlurmJobs,
                    request_deserializer=slurmpb_dot_slurm__pb2.ListSlurmJobsRequest.FromString,
                    response_serializer=slurmpb_dot_slurm__pb2.ListSlurmJobsResponse.SerializeToString,
            ),
            'ListSlurmNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSlurmNodes,
                    request_deserializer=slurmpb_dot_slurm__pb2.ListSlurmNodesRequest.FromString,
                    response_serializer=slurmpb_dot_slurm__pb2.ListSlurmNodesResponse.SerializeToString,
            ),
            'CancelSlurmJob': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelSlurmJob,
                    request_deserializer=slurmpb_dot_slurm__pb2.CancelSlurmJobRequest.FromString,
                    response_serializer=slurmpb_dot_slurm__pb2.CancelSlurmJobResponse.SerializeToString,
            ),
            'LaunchJupyter': grpc.unary_unary_rpc_method_handler(
                    servicer.LaunchJupyter,
                    request_deserializer=slurmpb_dot_slurm__pb2.LaunchJupyterRequest.FromString,
                    response_serializer=slurmpb_dot_slurm__pb2.LaunchJupyterResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'clusterfudge.Slurm', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('clusterfudge.Slurm', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Slurm(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSlurmJob(request,
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
            '/clusterfudge.Slurm/GetSlurmJob',
            slurmpb_dot_slurm__pb2.GetSlurmJobRequest.SerializeToString,
            slurmpb_dot_slurm__pb2.GetSlurmJobResponse.FromString,
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
    def ListSlurmJobs(request,
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
            '/clusterfudge.Slurm/ListSlurmJobs',
            slurmpb_dot_slurm__pb2.ListSlurmJobsRequest.SerializeToString,
            slurmpb_dot_slurm__pb2.ListSlurmJobsResponse.FromString,
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
    def ListSlurmNodes(request,
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
            '/clusterfudge.Slurm/ListSlurmNodes',
            slurmpb_dot_slurm__pb2.ListSlurmNodesRequest.SerializeToString,
            slurmpb_dot_slurm__pb2.ListSlurmNodesResponse.FromString,
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
    def CancelSlurmJob(request,
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
            '/clusterfudge.Slurm/CancelSlurmJob',
            slurmpb_dot_slurm__pb2.CancelSlurmJobRequest.SerializeToString,
            slurmpb_dot_slurm__pb2.CancelSlurmJobResponse.FromString,
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
    def LaunchJupyter(request,
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
            '/clusterfudge.Slurm/LaunchJupyter',
            slurmpb_dot_slurm__pb2.LaunchJupyterRequest.SerializeToString,
            slurmpb_dot_slurm__pb2.LaunchJupyterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)