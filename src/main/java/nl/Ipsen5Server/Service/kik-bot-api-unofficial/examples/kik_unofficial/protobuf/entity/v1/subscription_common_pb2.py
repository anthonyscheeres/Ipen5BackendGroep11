# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: entity/v1/subscription_common.proto

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
from kik_unofficial.protobuf.entity.v1 import entity_common_pb2 as entity_dot_v1_dot_entity__common__pb2
from kik_unofficial.protobuf.common.v1 import model_pb2 as common_dot_v1_dot_model__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='entity/v1/subscription_common.proto',
  package='common.entity.v1',
  syntax='proto3',
  serialized_pb=_b('\n#entity/v1/subscription_common.proto\x12\x10\x63ommon.entity.v1\x1a\x19protobuf_validation.proto\x1a\x1d\x65ntity/v1/entity_common.proto\x1a\x15\x63ommon/v1/model.proto\"/\n\x0fRosterSyncToken\x12\x1c\n\x07payload\x18\x01 \x01(\x0c\x42\x0b\xca\x9d%\x07\x08\x01(\x01\x30\x80(\"C\n\x0f\x41liasBlockEntry\x12\x30\n\talias_jid\x18\x01 \x01(\x0b\x32\x15.common.v1.XiAliasJidB\x06\xca\x9d%\x02\x08\x01\"\xf3\x01\n\x0bRosterEntry\x12<\n\tuser_data\x18\x01 \x01(\x0b\x32\'.common.entity.v1.EntityUserRosterEntryH\x00\x12>\n\ngroup_data\x18\x02 \x01(\x0b\x32(.common.entity.v1.EntityGroupRosterEntryH\x00\x12=\n\x10\x61lias_block_data\x18\x04 \x01(\x0b\x32!.common.entity.v1.AliasBlockEntryH\x00\x12\x12\n\nis_blocked\x18\x03 \x01(\x08\x42\x13\n\x11roster_entry_kindBn\n\x14\x63om.kik.entity.modelZLgithub.com/kikinteractive/xiphias-model-common/generated/go/entity/v1;entity\xa0\x01\x01\xa2\x02\x04SUBSb\x06proto3')
  ,
  dependencies=[protobuf__validation__pb2.DESCRIPTOR,entity_dot_v1_dot_entity__common__pb2.DESCRIPTOR,common_dot_v1_dot_model__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ROSTERSYNCTOKEN = _descriptor.Descriptor(
  name='RosterSyncToken',
  full_name='common.entity.v1.RosterSyncToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='common.entity.v1.RosterSyncToken.payload', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001(\0010\200('))),
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
  serialized_start=138,
  serialized_end=185,
)


_ALIASBLOCKENTRY = _descriptor.Descriptor(
  name='AliasBlockEntry',
  full_name='common.entity.v1.AliasBlockEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alias_jid', full_name='common.entity.v1.AliasBlockEntry.alias_jid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
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
  serialized_start=187,
  serialized_end=254,
)


_ROSTERENTRY = _descriptor.Descriptor(
  name='RosterEntry',
  full_name='common.entity.v1.RosterEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_data', full_name='common.entity.v1.RosterEntry.user_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_data', full_name='common.entity.v1.RosterEntry.group_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alias_block_data', full_name='common.entity.v1.RosterEntry.alias_block_data', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_blocked', full_name='common.entity.v1.RosterEntry.is_blocked', index=3,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
    _descriptor.OneofDescriptor(
      name='roster_entry_kind', full_name='common.entity.v1.RosterEntry.roster_entry_kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=257,
  serialized_end=500,
)

_ALIASBLOCKENTRY.fields_by_name['alias_jid'].message_type = common_dot_v1_dot_model__pb2._XIALIASJID
_ROSTERENTRY.fields_by_name['user_data'].message_type = entity_dot_v1_dot_entity__common__pb2._ENTITYUSERROSTERENTRY
_ROSTERENTRY.fields_by_name['group_data'].message_type = entity_dot_v1_dot_entity__common__pb2._ENTITYGROUPROSTERENTRY
_ROSTERENTRY.fields_by_name['alias_block_data'].message_type = _ALIASBLOCKENTRY
_ROSTERENTRY.oneofs_by_name['roster_entry_kind'].fields.append(
  _ROSTERENTRY.fields_by_name['user_data'])
_ROSTERENTRY.fields_by_name['user_data'].containing_oneof = _ROSTERENTRY.oneofs_by_name['roster_entry_kind']
_ROSTERENTRY.oneofs_by_name['roster_entry_kind'].fields.append(
  _ROSTERENTRY.fields_by_name['group_data'])
_ROSTERENTRY.fields_by_name['group_data'].containing_oneof = _ROSTERENTRY.oneofs_by_name['roster_entry_kind']
_ROSTERENTRY.oneofs_by_name['roster_entry_kind'].fields.append(
  _ROSTERENTRY.fields_by_name['alias_block_data'])
_ROSTERENTRY.fields_by_name['alias_block_data'].containing_oneof = _ROSTERENTRY.oneofs_by_name['roster_entry_kind']
DESCRIPTOR.message_types_by_name['RosterSyncToken'] = _ROSTERSYNCTOKEN
DESCRIPTOR.message_types_by_name['AliasBlockEntry'] = _ALIASBLOCKENTRY
DESCRIPTOR.message_types_by_name['RosterEntry'] = _ROSTERENTRY

RosterSyncToken = _reflection.GeneratedProtocolMessageType('RosterSyncToken', (_message.Message,), dict(
  DESCRIPTOR = _ROSTERSYNCTOKEN,
  __module__ = 'entity.v1.subscription_common_pb2'
  # @@protoc_insertion_point(class_scope:common.entity.v1.RosterSyncToken)
  ))
_sym_db.RegisterMessage(RosterSyncToken)

AliasBlockEntry = _reflection.GeneratedProtocolMessageType('AliasBlockEntry', (_message.Message,), dict(
  DESCRIPTOR = _ALIASBLOCKENTRY,
  __module__ = 'entity.v1.subscription_common_pb2'
  # @@protoc_insertion_point(class_scope:common.entity.v1.AliasBlockEntry)
  ))
_sym_db.RegisterMessage(AliasBlockEntry)

RosterEntry = _reflection.GeneratedProtocolMessageType('RosterEntry', (_message.Message,), dict(
  DESCRIPTOR = _ROSTERENTRY,
  __module__ = 'entity.v1.subscription_common_pb2'
  # @@protoc_insertion_point(class_scope:common.entity.v1.RosterEntry)
  ))
_sym_db.RegisterMessage(RosterEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\024com.kik.entity.modelZLgithub.com/kikinteractive/xiphias-model-common/generated/go/entity/v1;entity\240\001\001\242\002\004SUBS'))
_ROSTERSYNCTOKEN.fields_by_name['payload'].has_options = True
_ROSTERSYNCTOKEN.fields_by_name['payload']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001(\0010\200('))
_ALIASBLOCKENTRY.fields_by_name['alias_jid'].has_options = True
_ALIASBLOCKENTRY.fields_by_name['alias_jid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
# @@protoc_insertion_point(module_scope)
