# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: accounts/v1/user_info_shared.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import kik_unofficial.protobuf.protobuf_validation_pb2 as protobuf__validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='accounts/v1/user_info_shared.proto',
  package='common.accounts.v1',
  syntax='proto3',
  serialized_pb=_b('\n\"accounts/v1/user_info_shared.proto\x12\x12\x63ommon.accounts.v1\x1a\x19protobuf_validation.proto\"R\n\x15\x44isplayNameComponents\x12\x1d\n\nfirst_name\x18\x01 \x01(\tB\t\xca\x9d%\x05\x08\x01\x30\xff\x01\x12\x1a\n\tlast_name\x18\x02 \x01(\tB\x07\xca\x9d%\x03\x30\xff\x01*r\n\rAccountStatus\x12\t\n\x05UNSET\x10\x00\x12\x19\n\x15\x44\x45\x41\x43TIVATED_CONFIRMED\x10\n\x12\x1b\n\x17\x44\x45\x41\x43TIVATED_UNCONFIRMED\x10\t\x12\x0f\n\x0bUNCONFIRMED\x10\x0b\x12\r\n\tCONFIRMED\x10\x0c\x42\x8c\x01\n\x16\x63om.kik.accounts.modelB\x13UserInfoSharedProtoP\x01ZPgithub.com/kikinteractive/xiphias-model-common/generated/go/accounts/v1;accounts\xa0\x01\x01\xa2\x02\x05XIACCb\x06proto3')
  ,
  dependencies=[protobuf__validation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ACCOUNTSTATUS = _descriptor.EnumDescriptor(
  name='AccountStatus',
  full_name='common.accounts.v1.AccountStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEACTIVATED_CONFIRMED', index=1, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEACTIVATED_UNCONFIRMED', index=2, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNCONFIRMED', index=3, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRMED', index=4, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=169,
  serialized_end=283,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNTSTATUS)

AccountStatus = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTSTATUS)
UNSET = 0
DEACTIVATED_CONFIRMED = 10
DEACTIVATED_UNCONFIRMED = 9
UNCONFIRMED = 11
CONFIRMED = 12



_DISPLAYNAMECOMPONENTS = _descriptor.Descriptor(
  name='DisplayNameComponents',
  full_name='common.accounts.v1.DisplayNameComponents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='common.accounts.v1.DisplayNameComponents.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\0010\377\001'))),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='common.accounts.v1.DisplayNameComponents.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\0030\377\001'))),
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
  serialized_start=85,
  serialized_end=167,
)

DESCRIPTOR.message_types_by_name['DisplayNameComponents'] = _DISPLAYNAMECOMPONENTS
DESCRIPTOR.enum_types_by_name['AccountStatus'] = _ACCOUNTSTATUS

DisplayNameComponents = _reflection.GeneratedProtocolMessageType('DisplayNameComponents', (_message.Message,), dict(
  DESCRIPTOR = _DISPLAYNAMECOMPONENTS,
  __module__ = 'accounts.v1.user_info_shared_pb2'
  # @@protoc_insertion_point(class_scope:common.accounts.v1.DisplayNameComponents)
  ))
_sym_db.RegisterMessage(DisplayNameComponents)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026com.kik.accounts.modelB\023UserInfoSharedProtoP\001ZPgithub.com/kikinteractive/xiphias-model-common/generated/go/accounts/v1;accounts\240\001\001\242\002\005XIACC'))
_DISPLAYNAMECOMPONENTS.fields_by_name['first_name'].has_options = True
_DISPLAYNAMECOMPONENTS.fields_by_name['first_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\0010\377\001'))
_DISPLAYNAMECOMPONENTS.fields_by_name['last_name'].has_options = True
_DISPLAYNAMECOMPONENTS.fields_by_name['last_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\0030\377\001'))
# @@protoc_insertion_point(module_scope)
