# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: entity/v1/subscription_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import kik_unofficial.protobuf.protobuf_validation_pb2 as protobuf__validation__pb2
from kik_unofficial.protobuf.entity.v1 import subscription_common_pb2 as entity_dot_v1_dot_subscription__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='entity/v1/subscription_service.proto',
  package='mobile.entity.v1',
  syntax='proto3',
  serialized_pb=_b('\n$entity/v1/subscription_service.proto\x12\x10mobile.entity.v1\x1a\x19protobuf_validation.proto\x1a#entity/v1/subscription_common.proto\"K\n\x17SyncMyRosterDataRequest\x12\x30\n\x05token\x18\x01 \x01(\x0b\x32!.common.entity.v1.RosterSyncToken\"\x8f\x02\n\x18SyncMyRosterDataResponse\x12\x41\n\x06result\x18\x01 \x01(\x0e\x32\x31.mobile.entity.v1.SyncMyRosterDataResponse.Result\x12<\n\x0broster_data\x18\x02 \x03(\x0b\x32\x1d.common.entity.v1.RosterEntryB\x08\xca\x9d%\x04\x80\x01\xf4\x03\x12\x30\n\x05token\x18\x03 \x01(\x0b\x32!.common.entity.v1.RosterSyncToken\x12\x10\n\x08has_more\x18\x04 \x01(\x08\".\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x0f\n\x0bNOT_ALLOWED\x10\x01\x12\x0b\n\x07\x44\x45LAYED\x10\x02\x32y\n\x0cSubscription\x12i\n\x10SyncMyRosterData\x12).mobile.entity.v1.SyncMyRosterDataRequest\x1a*.mobile.entity.v1.SyncMyRosterDataResponseBp\n\"com.kik.entity.subscription.mobileZJgithub.com/kikinteractive/xiphias-api-mobile/generated/go/entity/v1;entityb\x06proto3')
  ,
  dependencies=[protobuf__validation__pb2.DESCRIPTOR,entity_dot_v1_dot_subscription__common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SYNCMYROSTERDATARESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.entity.v1.SyncMyRosterDataResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_ALLOWED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELAYED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=425,
  serialized_end=471,
)
_sym_db.RegisterEnumDescriptor(_SYNCMYROSTERDATARESPONSE_RESULT)


_SYNCMYROSTERDATAREQUEST = _descriptor.Descriptor(
  name='SyncMyRosterDataRequest',
  full_name='mobile.entity.v1.SyncMyRosterDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='mobile.entity.v1.SyncMyRosterDataRequest.token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=197,
)


_SYNCMYROSTERDATARESPONSE = _descriptor.Descriptor(
  name='SyncMyRosterDataResponse',
  full_name='mobile.entity.v1.SyncMyRosterDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.entity.v1.SyncMyRosterDataResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roster_data', full_name='mobile.entity.v1.SyncMyRosterDataResponse.roster_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\004\200\001\364\003'))),
    _descriptor.FieldDescriptor(
      name='token', full_name='mobile.entity.v1.SyncMyRosterDataResponse.token', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_more', full_name='mobile.entity.v1.SyncMyRosterDataResponse.has_more', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SYNCMYROSTERDATARESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=471,
)

_SYNCMYROSTERDATAREQUEST.fields_by_name['token'].message_type = entity_dot_v1_dot_subscription__common__pb2._ROSTERSYNCTOKEN
_SYNCMYROSTERDATARESPONSE.fields_by_name['result'].enum_type = _SYNCMYROSTERDATARESPONSE_RESULT
_SYNCMYROSTERDATARESPONSE.fields_by_name['roster_data'].message_type = entity_dot_v1_dot_subscription__common__pb2._ROSTERENTRY
_SYNCMYROSTERDATARESPONSE.fields_by_name['token'].message_type = entity_dot_v1_dot_subscription__common__pb2._ROSTERSYNCTOKEN
_SYNCMYROSTERDATARESPONSE_RESULT.containing_type = _SYNCMYROSTERDATARESPONSE
DESCRIPTOR.message_types_by_name['SyncMyRosterDataRequest'] = _SYNCMYROSTERDATAREQUEST
DESCRIPTOR.message_types_by_name['SyncMyRosterDataResponse'] = _SYNCMYROSTERDATARESPONSE

SyncMyRosterDataRequest = _reflection.GeneratedProtocolMessageType('SyncMyRosterDataRequest', (_message.Message,), dict(
  DESCRIPTOR = _SYNCMYROSTERDATAREQUEST,
  __module__ = 'entity.v1.subscription_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.entity.v1.SyncMyRosterDataRequest)
  ))
_sym_db.RegisterMessage(SyncMyRosterDataRequest)

SyncMyRosterDataResponse = _reflection.GeneratedProtocolMessageType('SyncMyRosterDataResponse', (_message.Message,), dict(
  DESCRIPTOR = _SYNCMYROSTERDATARESPONSE,
  __module__ = 'entity.v1.subscription_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.entity.v1.SyncMyRosterDataResponse)
  ))
_sym_db.RegisterMessage(SyncMyRosterDataResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.kik.entity.subscription.mobileZJgithub.com/kikinteractive/xiphias-api-mobile/generated/go/entity/v1;entity'))
_SYNCMYROSTERDATARESPONSE.fields_by_name['roster_data'].has_options = True
_SYNCMYROSTERDATARESPONSE.fields_by_name['roster_data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\004\200\001\364\003'))
# @@protoc_insertion_point(module_scope)
