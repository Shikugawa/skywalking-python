# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ..common import Common_pb2 as common_dot_Common__pb2
from ..language_agent import Tracing_pb2 as language__agent_dot_Tracing__pb2


class TraceSegmentReportServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.collect = channel.stream_unary(
                '/TraceSegmentReportService/collect',
                request_serializer=language__agent_dot_Tracing__pb2.SegmentObject.SerializeToString,
                response_deserializer=common_dot_Common__pb2.Commands.FromString,
                )


class TraceSegmentReportServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def collect(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TraceSegmentReportServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'collect': grpc.stream_unary_rpc_method_handler(
                    servicer.collect,
                    request_deserializer=language__agent_dot_Tracing__pb2.SegmentObject.FromString,
                    response_serializer=common_dot_Common__pb2.Commands.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TraceSegmentReportService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TraceSegmentReportService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def collect(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/TraceSegmentReportService/collect',
            language__agent_dot_Tracing__pb2.SegmentObject.SerializeToString,
            common_dot_Common__pb2.Commands.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
