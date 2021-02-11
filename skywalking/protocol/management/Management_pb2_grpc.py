# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ..common import Common_pb2 as common_dot_Common__pb2
from ..management import Management_pb2 as management_dot_Management__pb2


class ManagementServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.reportInstanceProperties = channel.unary_unary(
                '/ManagementService/reportInstanceProperties',
                request_serializer=management_dot_Management__pb2.InstanceProperties.SerializeToString,
                response_deserializer=common_dot_Common__pb2.Commands.FromString,
                )
        self.keepAlive = channel.unary_unary(
                '/ManagementService/keepAlive',
                request_serializer=management_dot_Management__pb2.InstancePingPkg.SerializeToString,
                response_deserializer=common_dot_Common__pb2.Commands.FromString,
                )


class ManagementServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def reportInstanceProperties(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def keepAlive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ManagementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'reportInstanceProperties': grpc.unary_unary_rpc_method_handler(
                    servicer.reportInstanceProperties,
                    request_deserializer=management_dot_Management__pb2.InstanceProperties.FromString,
                    response_serializer=common_dot_Common__pb2.Commands.SerializeToString,
            ),
            'keepAlive': grpc.unary_unary_rpc_method_handler(
                    servicer.keepAlive,
                    request_deserializer=management_dot_Management__pb2.InstancePingPkg.FromString,
                    response_serializer=common_dot_Common__pb2.Commands.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ManagementService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ManagementService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def reportInstanceProperties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ManagementService/reportInstanceProperties',
            management_dot_Management__pb2.InstanceProperties.SerializeToString,
            common_dot_Common__pb2.Commands.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def keepAlive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ManagementService/keepAlive',
            management_dot_Management__pb2.InstancePingPkg.SerializeToString,
            common_dot_Common__pb2.Commands.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
