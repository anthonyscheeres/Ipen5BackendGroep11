# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messagepath/v1/core_message_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kik_unofficial.protobuf.google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='messagepath/v1/core_message_options.proto',
  package='common.messagepath.v1',
  syntax='proto2',
  serialized_pb=_b('\n)messagepath/v1/core_message_options.proto\x12\x15\x63ommon.messagepath.v1\x1a google/protobuf/descriptor.proto\"\x87\x01\n\x1c\x43oreMessageOriginRestriction\x12H\n\x04\x64\x65ny\x18\x01 \x03(\x0e\x32:.common.messagepath.v1.CoreMessageOriginRestriction.Origin\"\x1d\n\x06Origin\x12\n\n\x06MOBILE\x10\x00\x12\x07\n\x03\x42OT\x10\x01:p\n\x12origin_restriction\x12\x1d.google.protobuf.FieldOptions\x18\xdb\xd3\x04 \x01(\x0b\x32\x33.common.messagepath.v1.CoreMessageOriginRestrictionBs\n\x19\x63om.kik.messagepath.modelZVgithub.com/kikinteractive/xiphias-model-common/generated/go/messagepath/v1;messagepath')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


ORIGIN_RESTRICTION_FIELD_NUMBER = 76251
origin_restriction = _descriptor.FieldDescriptor(
  name='origin_restriction', full_name='common.messagepath.v1.origin_restriction', index=0,
  number=76251, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)

_COREMESSAGEORIGINRESTRICTION_ORIGIN = _descriptor.EnumDescriptor(
  name='Origin',
  full_name='common.messagepath.v1.CoreMessageOriginRestriction.Origin',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=209,
  serialized_end=238,
)
_sym_db.RegisterEnumDescriptor(_COREMESSAGEORIGINRESTRICTION_ORIGIN)


_COREMESSAGEORIGINRESTRICTION = _descriptor.Descriptor(
  name='CoreMessageOriginRestriction',
  full_name='common.messagepath.v1.CoreMessageOriginRestriction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deny', full_name='common.messagepath.v1.CoreMessageOriginRestriction.deny', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COREMESSAGEORIGINRESTRICTION_ORIGIN,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=238,
)

_COREMESSAGEORIGINRESTRICTION.fields_by_name['deny'].enum_type = _COREMESSAGEORIGINRESTRICTION_ORIGIN
_COREMESSAGEORIGINRESTRICTION_ORIGIN.containing_type = _COREMESSAGEORIGINRESTRICTION
DESCRIPTOR.message_types_by_name['CoreMessageOriginRestriction'] = _COREMESSAGEORIGINRESTRICTION
DESCRIPTOR.extensions_by_name['origin_restriction'] = origin_restriction

CoreMessageOriginRestriction = _reflection.GeneratedProtocolMessageType('CoreMessageOriginRestriction', (_message.Message,), dict(
  DESCRIPTOR = _COREMESSAGEORIGINRESTRICTION,
  __module__ = 'messagepath.v1.core_message_options_pb2'
  # @@protoc_insertion_point(class_scope:common.messagepath.v1.CoreMessageOriginRestriction)
  ))
_sym_db.RegisterMessage(CoreMessageOriginRestriction)

origin_restriction.message_type = _COREMESSAGEORIGINRESTRICTION
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(origin_restriction)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\031com.kik.messagepath.modelZVgithub.com/kikinteractive/xiphias-model-common/generated/go/messagepath/v1;messagepath'))
# @@protoc_insertion_point(module_scope)
