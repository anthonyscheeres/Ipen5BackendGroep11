# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messagepath/v1/mentions.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import kik_unofficial.protobuf.common_model_pb2 as common__model__pb2
from kik_unofficial.protobuf.common.v1 import model_pb2 as common_dot_v1_dot_model__pb2
import kik_unofficial.protobuf.protobuf_validation_pb2 as protobuf__validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='messagepath/v1/mentions.proto',
  package='common.messagepath.v1',
  syntax='proto3',
  serialized_pb=_b('\n\x1dmessagepath/v1/mentions.proto\x12\x15\x63ommon.messagepath.v1\x1a\x12\x63ommon_model.proto\x1a\x15\x63ommon/v1/model.proto\x1a\x19protobuf_validation.proto\"\x98\x01\n\x16MentionReplyAttachment\x12;\n\x12original_mentioner\x18\x01 \x01(\x0b\x32\x15.common.XiBareUserJidB\x08\x18\x01\xca\x9d%\x02\x08\x00\x12\x41\n\x15original_mentioner_v2\x18\x02 \x01(\x0b\x32\".common.v1.XiBareUserJidOrAliasJidBz\n\x19\x63om.kik.messagepath.modelZVgithub.com/kikinteractive/xiphias-model-common/generated/go/messagepath/v1;messagepath\xa2\x02\x04MPTHb\x06proto3')
  ,
  dependencies=[common__model__pb2.DESCRIPTOR,common_dot_v1_dot_model__pb2.DESCRIPTOR,protobuf__validation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MENTIONREPLYATTACHMENT = _descriptor.Descriptor(
  name='MentionReplyAttachment',
  full_name='common.messagepath.v1.MentionReplyAttachment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='original_mentioner', full_name='common.messagepath.v1.MentionReplyAttachment.original_mentioner', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001\312\235%\002\010\000'))),
    _descriptor.FieldDescriptor(
      name='original_mentioner_v2', full_name='common.messagepath.v1.MentionReplyAttachment.original_mentioner_v2', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=127,
  serialized_end=279,
)

_MENTIONREPLYATTACHMENT.fields_by_name['original_mentioner'].message_type = common__model__pb2._XIBAREUSERJID
_MENTIONREPLYATTACHMENT.fields_by_name['original_mentioner_v2'].message_type = common_dot_v1_dot_model__pb2._XIBAREUSERJIDORALIASJID
DESCRIPTOR.message_types_by_name['MentionReplyAttachment'] = _MENTIONREPLYATTACHMENT

MentionReplyAttachment = _reflection.GeneratedProtocolMessageType('MentionReplyAttachment', (_message.Message,), dict(
  DESCRIPTOR = _MENTIONREPLYATTACHMENT,
  __module__ = 'messagepath.v1.mentions_pb2'
  # @@protoc_insertion_point(class_scope:common.messagepath.v1.MentionReplyAttachment)
  ))
_sym_db.RegisterMessage(MentionReplyAttachment)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\031com.kik.messagepath.modelZVgithub.com/kikinteractive/xiphias-model-common/generated/go/messagepath/v1;messagepath\242\002\004MPTH'))
_MENTIONREPLYATTACHMENT.fields_by_name['original_mentioner'].has_options = True
_MENTIONREPLYATTACHMENT.fields_by_name['original_mentioner']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001\312\235%\002\010\000'))
# @@protoc_insertion_point(module_scope)
