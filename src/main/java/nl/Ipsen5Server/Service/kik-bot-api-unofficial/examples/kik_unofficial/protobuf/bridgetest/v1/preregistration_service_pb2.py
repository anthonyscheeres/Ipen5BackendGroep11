# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridgetest/v1/preregistration_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import kik_unofficial.protobuf.common_rpc_pb2 as common__rpc__pb2
from kik_unofficial.protobuf.bridgetest.v1 import bridgetest_common_pb2 as bridgetest_dot_v1_dot_bridgetest__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bridgetest/v1/preregistration_service.proto',
  package='mobile.bridgetest.v1',
  syntax='proto3',
  serialized_pb=_b('\n+bridgetest/v1/preregistration_service.proto\x12\x14mobile.bridgetest.v1\x1a\x10\x63ommon_rpc.proto\x1a%bridgetest/v1/bridgetest_common.proto2\xcf\x02\n\x0fPreRegistration\x12M\n\x04\x45\x63ho\x12!.common.bridgetest.v1.EchoRequest\x1a\".common.bridgetest.v1.EchoResponse\x12\x45\n\x07Workout\x12$.common.bridgetest.v1.WorkoutRequest\x1a\x14.common.VoidResponse\x12\x36\n\tException\x12\x13.common.VoidRequest\x1a\x14.common.VoidResponse\x12n\n\x0fValidateHeaders\x12,.common.bridgetest.v1.ValidateHeadersRequest\x1a-.common.bridgetest.v1.ValidateHeadersResponseBh\n\x12\x63om.kik.bridgetestZRgithub.com/kikinteractive/xiphias-api-mobile/generated/go/bridgetest/v1;bridgetestb\x06proto3')
  ,
  dependencies=[common__rpc__pb2.DESCRIPTOR,bridgetest_dot_v1_dot_bridgetest__common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\022com.kik.bridgetestZRgithub.com/kikinteractive/xiphias-api-mobile/generated/go/bridgetest/v1;bridgetest'))
# @@protoc_insertion_point(module_scope)
