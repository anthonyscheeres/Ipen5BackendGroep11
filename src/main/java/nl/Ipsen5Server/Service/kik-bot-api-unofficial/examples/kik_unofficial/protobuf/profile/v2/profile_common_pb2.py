# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profile/v2/profile_common.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='profile/v2/profile_common.proto',
  package='common.profile.v2',
  syntax='proto3',
  serialized_pb=_b('\n\x1fprofile/v2/profile_common.proto\x12\x11\x63ommon.profile.v2\x1a\x19protobuf_validation.proto\"R\n\x15\x44isplayNameComponents\x12\x1d\n\nfirst_name\x18\x01 \x01(\tB\t\xca\x9d%\x05\x08\x01\x30\xff\x01\x12\x1a\n\tlast_name\x18\x02 \x01(\tB\x07\xca\x9d%\x03\x30\xff\x01\x42}\n\x16\x63om.kik.gen.profile.v2ZNgithub.com/kikinteractive/xiphias-model-common/generated/go/profile/v2;profile\xa2\x02\x12KPBCommonProfileV2b\x06proto3')
  ,
  dependencies=[protobuf__validation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DISPLAYNAMECOMPONENTS = _descriptor.Descriptor(
  name='DisplayNameComponents',
  full_name='common.profile.v2.DisplayNameComponents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='common.profile.v2.DisplayNameComponents.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\0010\377\001'))),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='common.profile.v2.DisplayNameComponents.last_name', index=1,
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
  serialized_start=81,
  serialized_end=163,
)

DESCRIPTOR.message_types_by_name['DisplayNameComponents'] = _DISPLAYNAMECOMPONENTS

DisplayNameComponents = _reflection.GeneratedProtocolMessageType('DisplayNameComponents', (_message.Message,), dict(
  DESCRIPTOR = _DISPLAYNAMECOMPONENTS,
  __module__ = 'profile.v2.profile_common_pb2'
  # @@protoc_insertion_point(class_scope:common.profile.v2.DisplayNameComponents)
  ))
_sym_db.RegisterMessage(DisplayNameComponents)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026com.kik.gen.profile.v2ZNgithub.com/kikinteractive/xiphias-model-common/generated/go/profile/v2;profile\242\002\022KPBCommonProfileV2'))
_DISPLAYNAMECOMPONENTS.fields_by_name['first_name'].has_options = True
_DISPLAYNAMECOMPONENTS.fields_by_name['first_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\0010\377\001'))
_DISPLAYNAMECOMPONENTS.fields_by_name['last_name'].has_options = True
_DISPLAYNAMECOMPONENTS.fields_by_name['last_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\0030\377\001'))
# @@protoc_insertion_point(module_scope)
