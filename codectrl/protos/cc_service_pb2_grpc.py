# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import cc_service_pb2 as cc__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import log_pb2 as log__pb2


class LogServerStub(object):
    """LogServer is the service that should only be implemented by log servers that
    can be connected to by a CodeCtrl front-end. Language loggers should not
    implement this service or use it as a client for that matter. Ways of
    enforcing that only servers can receive logs iS TBD but will be worked on in
    the future.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLog = channel.unary_unary(
                '/codectrl.logs_service.LogServer/GetLog',
                request_serializer=cc__service__pb2.Connection.SerializeToString,
                response_deserializer=log__pb2.Log.FromString,
                )
        self.GetLogs = channel.unary_stream(
                '/codectrl.logs_service.LogServer/GetLogs',
                request_serializer=cc__service__pb2.Connection.SerializeToString,
                response_deserializer=log__pb2.Log.FromString,
                )
        self.GetServerDetails = channel.unary_unary(
                '/codectrl.logs_service.LogServer/GetServerDetails',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=cc__service__pb2.ServerDetails.FromString,
                )
        self.RegisterClient = channel.unary_unary(
                '/codectrl.logs_service.LogServer/RegisterClient',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=cc__service__pb2.Connection.FromString,
                )
        self.RegisterExistingClient = channel.unary_unary(
                '/codectrl.logs_service.LogServer/RegisterExistingClient',
                request_serializer=cc__service__pb2.Connection.SerializeToString,
                response_deserializer=cc__service__pb2.RequestResult.FromString,
                )


class LogServerServicer(object):
    """LogServer is the service that should only be implemented by log servers that
    can be connected to by a CodeCtrl front-end. Language loggers should not
    implement this service or use it as a client for that matter. Ways of
    enforcing that only servers can receive logs iS TBD but will be worked on in
    the future.
    """

    def GetLog(self, request, context):
        """Gets the latest log from the server, generally not used but is here for
        compatibiliy's sake in the case where a front-end cannot use a stream.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLogs(self, request, context):
        """Gets a stream of the available logs, this should be preferred over
        `GetLog` when possible.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServerDetails(self, request, context):
        """Gets the current details about the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterClient(self, request, context):
        """Registers a new front-end connection to a server instance and returns the
        `Connection` message with a `uuid`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterExistingClient(self, request, context):
        """Registers an already pre-existing connection to a server instance using an
        already generated `uuid` supplied in the `Connection`. Servers should
        verify that the supplied `uuid` is, in fact, a valid hyphenated v4 UUID.
        Returns a boolean whether or not the registration was succesful.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LogServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLog': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLog,
                    request_deserializer=cc__service__pb2.Connection.FromString,
                    response_serializer=log__pb2.Log.SerializeToString,
            ),
            'GetLogs': grpc.unary_stream_rpc_method_handler(
                    servicer.GetLogs,
                    request_deserializer=cc__service__pb2.Connection.FromString,
                    response_serializer=log__pb2.Log.SerializeToString,
            ),
            'GetServerDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerDetails,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=cc__service__pb2.ServerDetails.SerializeToString,
            ),
            'RegisterClient': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterClient,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=cc__service__pb2.Connection.SerializeToString,
            ),
            'RegisterExistingClient': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterExistingClient,
                    request_deserializer=cc__service__pb2.Connection.FromString,
                    response_serializer=cc__service__pb2.RequestResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'codectrl.logs_service.LogServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LogServer(object):
    """LogServer is the service that should only be implemented by log servers that
    can be connected to by a CodeCtrl front-end. Language loggers should not
    implement this service or use it as a client for that matter. Ways of
    enforcing that only servers can receive logs iS TBD but will be worked on in
    the future.
    """

    @staticmethod
    def GetLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/codectrl.logs_service.LogServer/GetLog',
            cc__service__pb2.Connection.SerializeToString,
            log__pb2.Log.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/codectrl.logs_service.LogServer/GetLogs',
            cc__service__pb2.Connection.SerializeToString,
            log__pb2.Log.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServerDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/codectrl.logs_service.LogServer/GetServerDetails',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            cc__service__pb2.ServerDetails.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/codectrl.logs_service.LogServer/RegisterClient',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            cc__service__pb2.Connection.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterExistingClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/codectrl.logs_service.LogServer/RegisterExistingClient',
            cc__service__pb2.Connection.SerializeToString,
            cc__service__pb2.RequestResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class LogClientStub(object):
    """LogClient is the service that needs to be implemented by log servers so they
    can determine how the logs are stored when they are received by the server.
    Loggers must only use this service as a client.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendLog = channel.unary_unary(
                '/codectrl.logs_service.LogClient/SendLog',
                request_serializer=log__pb2.Log.SerializeToString,
                response_deserializer=cc__service__pb2.RequestResult.FromString,
                )
        self.SendLogs = channel.stream_unary(
                '/codectrl.logs_service.LogClient/SendLogs',
                request_serializer=log__pb2.Log.SerializeToString,
                response_deserializer=cc__service__pb2.RequestResult.FromString,
                )


class LogClientServicer(object):
    """LogClient is the service that needs to be implemented by log servers so they
    can determine how the logs are stored when they are received by the server.
    Loggers must only use this service as a client.
    """

    def SendLog(self, request, context):
        """Sends a single log. Should only be used in cases where log batching is not
        possible or not determinable.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendLogs(self, request_iterator, context):
        """Sends a stream of logs. Should generally be preferred over `SendLog` as it
        allows for batch sending of `Log`s and _should_ be more efficient on
        resources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LogClientServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendLog': grpc.unary_unary_rpc_method_handler(
                    servicer.SendLog,
                    request_deserializer=log__pb2.Log.FromString,
                    response_serializer=cc__service__pb2.RequestResult.SerializeToString,
            ),
            'SendLogs': grpc.stream_unary_rpc_method_handler(
                    servicer.SendLogs,
                    request_deserializer=log__pb2.Log.FromString,
                    response_serializer=cc__service__pb2.RequestResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'codectrl.logs_service.LogClient', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LogClient(object):
    """LogClient is the service that needs to be implemented by log servers so they
    can determine how the logs are stored when they are received by the server.
    Loggers must only use this service as a client.
    """

    @staticmethod
    def SendLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/codectrl.logs_service.LogClient/SendLog',
            log__pb2.Log.SerializeToString,
            cc__service__pb2.RequestResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendLogs(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/codectrl.logs_service.LogClient/SendLogs',
            log__pb2.Log.SerializeToString,
            cc__service__pb2.RequestResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)