# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import client_pb2 as client__pb2

GRPC_GENERATED_VERSION = '1.63.0'
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
        + f' but the generated code in client_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class commandStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.deposita = channel.unary_unary(
                '/client.command/deposita',
                request_serializer=client__pb2.msg_deposita.SerializeToString,
                response_deserializer=client__pb2.msg_response.FromString,
                _registered_method=True)
        self.preleva = channel.unary_unary(
                '/client.command/preleva',
                request_serializer=client__pb2.msg_preleva.SerializeToString,
                response_deserializer=client__pb2.msg_response.FromString,
                _registered_method=True)


class commandServicer(object):
    """Missing associated documentation comment in .proto file."""

    def deposita(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def preleva(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_commandServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'deposita': grpc.unary_unary_rpc_method_handler(
                    servicer.deposita,
                    request_deserializer=client__pb2.msg_deposita.FromString,
                    response_serializer=client__pb2.msg_response.SerializeToString,
            ),
            'preleva': grpc.unary_unary_rpc_method_handler(
                    servicer.preleva,
                    request_deserializer=client__pb2.msg_preleva.FromString,
                    response_serializer=client__pb2.msg_response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'client.command', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class command(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def deposita(request,
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
            '/client.command/deposita',
            client__pb2.msg_deposita.SerializeToString,
            client__pb2.msg_response.FromString,
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
    def preleva(request,
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
            '/client.command/preleva',
            client__pb2.msg_preleva.SerializeToString,
            client__pb2.msg_response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)