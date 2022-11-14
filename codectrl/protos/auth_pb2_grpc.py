# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import auth_pb2 as auth__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AuthenticationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.VerifyToken = channel.unary_unary(
                '/codectrl.auth_service.Authentication/VerifyToken',
                request_serializer=auth__pb2.VerifyTokenRequest.SerializeToString,
                response_deserializer=auth__pb2.VerifyTokenRequestResult.FromString,
                )
        self.GenerateToken = channel.unary_unary(
                '/codectrl.auth_service.Authentication/GenerateToken',
                request_serializer=auth__pb2.GenerateTokenRequest.SerializeToString,
                response_deserializer=auth__pb2.GenerateTokenRequestResult.FromString,
                )
        self.RevokeToken = channel.unary_unary(
                '/codectrl.auth_service.Authentication/RevokeToken',
                request_serializer=auth__pb2.Token.SerializeToString,
                response_deserializer=auth__pb2.RevokeTokenRequestResult.FromString,
                )
        self.RefreshToken = channel.unary_unary(
                '/codectrl.auth_service.Authentication/RefreshToken',
                request_serializer=auth__pb2.Token.SerializeToString,
                response_deserializer=auth__pb2.Token.FromString,
                )
        self.GithubLogin = channel.unary_unary(
                '/codectrl.auth_service.Authentication/GithubLogin',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=auth__pb2.LoginUrl.FromString,
                )


class AuthenticationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def VerifyToken(self, request, context):
        """Takes a token and verifies that it is:
        a) In valid format
        b) Present in the database/filesystem (down to implementation)
        c) Has the correct permissions for the given intent
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevokeToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RefreshToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GithubLogin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthenticationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'VerifyToken': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyToken,
                    request_deserializer=auth__pb2.VerifyTokenRequest.FromString,
                    response_serializer=auth__pb2.VerifyTokenRequestResult.SerializeToString,
            ),
            'GenerateToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateToken,
                    request_deserializer=auth__pb2.GenerateTokenRequest.FromString,
                    response_serializer=auth__pb2.GenerateTokenRequestResult.SerializeToString,
            ),
            'RevokeToken': grpc.unary_unary_rpc_method_handler(
                    servicer.RevokeToken,
                    request_deserializer=auth__pb2.Token.FromString,
                    response_serializer=auth__pb2.RevokeTokenRequestResult.SerializeToString,
            ),
            'RefreshToken': grpc.unary_unary_rpc_method_handler(
                    servicer.RefreshToken,
                    request_deserializer=auth__pb2.Token.FromString,
                    response_serializer=auth__pb2.Token.SerializeToString,
            ),
            'GithubLogin': grpc.unary_unary_rpc_method_handler(
                    servicer.GithubLogin,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=auth__pb2.LoginUrl.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'codectrl.auth_service.Authentication', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Authentication(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def VerifyToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/codectrl.auth_service.Authentication/VerifyToken',
            auth__pb2.VerifyTokenRequest.SerializeToString,
            auth__pb2.VerifyTokenRequestResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/codectrl.auth_service.Authentication/GenerateToken',
            auth__pb2.GenerateTokenRequest.SerializeToString,
            auth__pb2.GenerateTokenRequestResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevokeToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/codectrl.auth_service.Authentication/RevokeToken',
            auth__pb2.Token.SerializeToString,
            auth__pb2.RevokeTokenRequestResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RefreshToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/codectrl.auth_service.Authentication/RefreshToken',
            auth__pb2.Token.SerializeToString,
            auth__pb2.Token.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GithubLogin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/codectrl.auth_service.Authentication/GithubLogin',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            auth__pb2.LoginUrl.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)