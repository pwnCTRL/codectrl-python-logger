# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x15\x63odectrl.auth_service\x1a\x1bgoogle/protobuf/empty.proto\"\x15\n\x04Name\x12\r\n\x05inner\x18\x01 \x01(\t\"/\n\x10TokenPermissions\x12\x0c\n\x04read\x18\x01 \x01(\x08\x12\r\n\x05write\x18\x02 \x01(\x08\"\xa4\x01\n\x05Token\x12)\n\x04name\x18\x01 \x01(\x0b\x32\x1b.codectrl.auth_service.Name\x12<\n\x0bpermissions\x18\x02 \x01(\x0b\x32\'.codectrl.auth_service.TokenPermissions\x12\x32\n\x06intent\x18\x03 \x01(\x0e\x32\".codectrl.auth_service.TokenIntent\"u\n\x14GenerateTokenRequest\x12)\n\x04name\x18\x01 \x01(\x0b\x32\x1b.codectrl.auth_service.Name\x12\x32\n\x06intent\x18\x02 \x01(\x0e\x32\".codectrl.auth_service.TokenIntent\"u\n\x12VerifyTokenRequest\x12+\n\x05token\x18\x01 \x01(\x0b\x32\x1c.codectrl.auth_service.Token\x12\x32\n\x06intent\x18\x02 \x01(\x0e\x32\".codectrl.auth_service.TokenIntent\"p\n\x18VerifyTokenRequestResult\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x43\n\x06status\x18\x02 \x01(\x0e\x32\x33.codectrl.auth_service.VerifyTokenRequestResultEnum\"p\n\x18RevokeTokenRequestResult\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x43\n\x06status\x18\x02 \x01(\x0e\x32\x33.codectrl.auth_service.RevokeTokenRequestResultEnum\"\x9f\x01\n\x1aGenerateTokenRequestResult\x12\x45\n\x06status\x18\x01 \x01(\x0e\x32\x35.codectrl.auth_service.GenerateTokenRequestResultEnum\x12\x30\n\x05token\x18\x02 \x01(\x0b\x32\x1c.codectrl.auth_service.TokenH\x00\x88\x01\x01\x42\x08\n\x06_token\"\x17\n\x08LoginUrl\x12\x0b\n\x03url\x18\x01 \x01(\t*\'\n\x0bTokenIntent\x12\n\n\x06LOGGER\x10\x00\x12\x0c\n\x08\x46RONTEND\x10\x01*N\n\x1cVerifyTokenRequestResultEnum\x12\x10\n\x0cUNAUTHORISED\x10\x00\x12\x0c\n\x08NOTFOUND\x10\x01\x12\x0e\n\nAUTHORISED\x10\x02*s\n\x1eGenerateTokenRequestResultEnum\x12\x17\n\x13NAME_ALREADY_EXISTS\x10\x00\x12\x18\n\x14TOKEN_ALREADY_EXISTS\x10\x01\x12\x1e\n\x1aTOKEN_GENERATION_SUCCEEDED\x10\x02*S\n\x1cRevokeTokenRequestResultEnum\x12\x13\n\x0fTOKEN_NOT_FOUND\x10\x00\x12\x1e\n\x1aTOKEN_REVOKATION_SUCCEEDED\x10\x01\x32\xe8\x03\n\x0e\x41uthentication\x12k\n\x0bVerifyToken\x12).codectrl.auth_service.VerifyTokenRequest\x1a/.codectrl.auth_service.VerifyTokenRequestResult\"\x00\x12q\n\rGenerateToken\x12+.codectrl.auth_service.GenerateTokenRequest\x1a\x31.codectrl.auth_service.GenerateTokenRequestResult\"\x00\x12^\n\x0bRevokeToken\x12\x1c.codectrl.auth_service.Token\x1a/.codectrl.auth_service.RevokeTokenRequestResult\"\x00\x12L\n\x0cRefreshToken\x12\x1c.codectrl.auth_service.Token\x1a\x1c.codectrl.auth_service.Token\"\x00\x12H\n\x0bGithubLogin\x12\x16.google.protobuf.Empty\x1a\x1f.codectrl.auth_service.LoginUrl\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TOKENINTENT._serialized_start=958
  _TOKENINTENT._serialized_end=997
  _VERIFYTOKENREQUESTRESULTENUM._serialized_start=999
  _VERIFYTOKENREQUESTRESULTENUM._serialized_end=1077
  _GENERATETOKENREQUESTRESULTENUM._serialized_start=1079
  _GENERATETOKENREQUESTRESULTENUM._serialized_end=1194
  _REVOKETOKENREQUESTRESULTENUM._serialized_start=1196
  _REVOKETOKENREQUESTRESULTENUM._serialized_end=1279
  _NAME._serialized_start=66
  _NAME._serialized_end=87
  _TOKENPERMISSIONS._serialized_start=89
  _TOKENPERMISSIONS._serialized_end=136
  _TOKEN._serialized_start=139
  _TOKEN._serialized_end=303
  _GENERATETOKENREQUEST._serialized_start=305
  _GENERATETOKENREQUEST._serialized_end=422
  _VERIFYTOKENREQUEST._serialized_start=424
  _VERIFYTOKENREQUEST._serialized_end=541
  _VERIFYTOKENREQUESTRESULT._serialized_start=543
  _VERIFYTOKENREQUESTRESULT._serialized_end=655
  _REVOKETOKENREQUESTRESULT._serialized_start=657
  _REVOKETOKENREQUESTRESULT._serialized_end=769
  _GENERATETOKENREQUESTRESULT._serialized_start=772
  _GENERATETOKENREQUESTRESULT._serialized_end=931
  _LOGINURL._serialized_start=933
  _LOGINURL._serialized_end=956
  _AUTHENTICATION._serialized_start=1282
  _AUTHENTICATION._serialized_end=1770
# @@protoc_insertion_point(module_scope)
