# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kik_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...kik_unofficial.protobuf.google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kik_options.proto',
  package='kik',
  syntax='proto2',
  serialized_pb=_b('\n\x11kik_options.proto\x12\x03kik\x1a google/protobuf/descriptor.proto\"t\n\x11\x43heckStyleOptions\x12\x1a\n\x0bignore_path\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x1d\n\x0eignore_version\x18\x02 \x01(\x08:\x05\x66\x61lse\x12$\n\x15ignore_package_prefix\x18\x03 \x01(\x08:\x05\x66\x61lse:J\n\ncheckstyle\x12\x1c.google.protobuf.FileOptions\x18\xb5\xa4\x05 \x01(\x0b\x32\x16.kik.CheckStyleOptionsBd\n\x0f\x63om.kik.optionsZQgithub.com/kikinteractive/xiphias-model-common/generated/go/kikoptions;kikoptions')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


CHECKSTYLE_FIELD_NUMBER = 86581
checkstyle = _descriptor.FieldDescriptor(
  name='checkstyle', full_name='kik.checkstyle', index=0,
  number=86581, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_CHECKSTYLEOPTIONS = _descriptor.Descriptor(
  name='CheckStyleOptions',
  full_name='kik.CheckStyleOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ignore_path', full_name='kik.CheckStyleOptions.ignore_path', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ignore_version', full_name='kik.CheckStyleOptions.ignore_version', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ignore_package_prefix', full_name='kik.CheckStyleOptions.ignore_package_prefix', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=176,
)

DESCRIPTOR.message_types_by_name['CheckStyleOptions'] = _CHECKSTYLEOPTIONS
DESCRIPTOR.extensions_by_name['checkstyle'] = checkstyle

CheckStyleOptions = _reflection.GeneratedProtocolMessageType('CheckStyleOptions', (_message.Message,), dict(
  DESCRIPTOR = _CHECKSTYLEOPTIONS,
  __module__ = 'kik_options_pb2'
  # @@protoc_insertion_point(class_scope:kik.CheckStyleOptions)
  ))
_sym_db.RegisterMessage(CheckStyleOptions)

checkstyle.message_type = _CHECKSTYLEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(checkstyle)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\017com.kik.optionsZQgithub.com/kikinteractive/xiphias-model-common/generated/go/kikoptions;kikoptions'))
# @@protoc_insertion_point(module_scope)
