# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cc_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import log_pb2 as log__pb2
from . import auth_pb2 as auth__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x63_service.proto\x12\x15\x63odectrl.logs_service\x1a\tlog.proto\x1a\nauth.proto\x1a\x1bgoogle/protobuf/empty.proto\"V\n\nConnection\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x30\n\x05token\x18\x02 \x01(\x0b\x32\x1c.codectrl.auth_service.TokenH\x00\x88\x01\x01\x42\x08\n\x06_token\"\xb1\x01\n\rRequestResult\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x34\n\x06status\x18\x02 \x01(\x0e\x32$.codectrl.logs_service.RequestStatus\x12J\n\nauthStatus\x18\x03 \x01(\x0b\x32\x31.codectrl.auth_service.GenerateTokenRequestResultH\x00\x88\x01\x01\x42\r\n\x0b_authStatus\"[\n\rServerDetails\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x0e\n\x06uptime\x18\x03 \x01(\x04\x12\x1e\n\x16requiresAuthentication\x18\x04 \x01(\x08*)\n\rRequestStatus\x12\r\n\tCONFIRMED\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x32\xa4\x03\n\tLogServer\x12\x45\n\x06GetLog\x12!.codectrl.logs_service.Connection\x1a\x16.codectrl.data.log.Log\"\x00\x12H\n\x07GetLogs\x12!.codectrl.logs_service.Connection\x1a\x16.codectrl.data.log.Log\"\x00\x30\x01\x12R\n\x10GetServerDetails\x12\x16.google.protobuf.Empty\x1a$.codectrl.logs_service.ServerDetails\"\x00\x12M\n\x0eRegisterClient\x12\x16.google.protobuf.Empty\x1a!.codectrl.logs_service.Connection\"\x00\x12\x63\n\x16RegisterExistingClient\x12!.codectrl.logs_service.Connection\x1a$.codectrl.logs_service.RequestResult\"\x00\x32\xa4\x01\n\tLogClient\x12I\n\x07SendLog\x12\x16.codectrl.data.log.Log\x1a$.codectrl.logs_service.RequestResult\"\x00\x12L\n\x08SendLogs\x12\x16.codectrl.data.log.Log\x1a$.codectrl.logs_service.RequestResult\"\x00(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cc_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUESTSTATUS._serialized_start=456
  _REQUESTSTATUS._serialized_end=497
  _CONNECTION._serialized_start=95
  _CONNECTION._serialized_end=181
  _REQUESTRESULT._serialized_start=184
  _REQUESTRESULT._serialized_end=361
  _SERVERDETAILS._serialized_start=363
  _SERVERDETAILS._serialized_end=454
  _LOGSERVER._serialized_start=500
  _LOGSERVER._serialized_end=920
  _LOGCLIENT._serialized_start=923
  _LOGCLIENT._serialized_end=1087
# @@protoc_insertion_point(module_scope)