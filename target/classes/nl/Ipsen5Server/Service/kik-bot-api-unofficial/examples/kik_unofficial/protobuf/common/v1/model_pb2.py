# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/v1/model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .....kik_unofficial.protobuf import kik_options_pb2 as kik__options__pb2
from .....kik_unofficial.protobuf import protobuf_validation_pb2 as protobuf__validation__pb2
from .....kik_unofficial.protobuf import common_model_pb2 as common__model__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/v1/model.proto',
  package='common.v1',
  syntax='proto3',
  serialized_pb=_b('\n\x15\x63ommon/v1/model.proto\x12\tcommon.v1\x1a\x11kik_options.proto\x1a\x19protobuf_validation.proto\x1a\x12\x63ommon_model.proto\"@\n\nXiAliasJid\x12\x32\n\nlocal_part\x18\x01 \x01(\tB\x1e\xca\x9d%\x1a\x08\x01\x12\x16^[a-z0-9_-]{52}_[a|b]$\"\x86\x01\n\x17XiBareUserJidOrAliasJid\x12.\n\rbare_user_jid\x18\x01 \x01(\x0b\x32\x15.common.XiBareUserJidH\x00\x12/\n\x0e\x61lias_user_jid\x18\x02 \x01(\x0b\x32\x15.common.v1.XiAliasJidH\x00\x42\n\n\x08jid_type\"\xa0\x01\n\x08XiAnyJid\x12.\n\rbare_user_jid\x18\x01 \x01(\x0b\x32\x15.common.XiBareUserJidH\x00\x12/\n\x0e\x61lias_user_jid\x18\x02 \x01(\x0b\x32\x15.common.v1.XiAliasJidH\x00\x12\'\n\tgroup_jid\x18\x03 \x01(\x0b\x32\x12.common.XiGroupJidH\x00\x42\n\n\x08jid_type\"1\n\x0bXiKinUserId\x12\"\n\x02id\x18\x01 \x01(\tB\x16\xca\x9d%\x12\x08\x01\x12\x0e^[a-z2-7]{52}$\"j\n\tXiConvoId\x12\x30\n\none_to_one\x18\x01 \x01(\x0b\x32\x1a.common.v1.OneToOneConvoIdH\x00\x12#\n\x05group\x18\x02 \x01(\x0b\x32\x12.common.XiGroupJidH\x00\x42\x06\n\x04kind\"G\n\x0fOneToOneConvoId\x12\x34\n\x05users\x18\x01 \x03(\x0b\x32\x15.common.XiBareUserJidB\x0e\xca\x9d%\n\x08\x01x\x02\x80\x01\x02\x88\x01\x00\"O\n\x05XiJWT\x12\x46\n\x03jwt\x18\x01 \x01(\tB9\xca\x9d%5\x08\x01\x12\x31^[a-zA-Z0-9-_]+?.[a-zA-Z0-9-_]+?.[a-zA-Z0-9-_]+?$B{\n\x0e\x63om.kik.commonB\nModelProtoP\x01ZLgithub.com/kikinteractive/xiphias-model-common/generated/go/common/v1;common\xa0\x01\x01\xa2\x02\x03KPB\xaa\xa3*\x02\x08\x01\x62\x06proto3')
  ,
  dependencies=[kik__options__pb2.DESCRIPTOR,protobuf__validation__pb2.DESCRIPTOR,common__model__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_XIALIASJID = _descriptor.Descriptor(
  name='XiAliasJid',
  full_name='common.v1.XiAliasJid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='local_part', full_name='common.v1.XiAliasJid.local_part', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\032\010\001\022\026^[a-z0-9_-]{52}_[a|b]$'))),
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
  serialized_start=102,
  serialized_end=166,
)


_XIBAREUSERJIDORALIASJID = _descriptor.Descriptor(
  name='XiBareUserJidOrAliasJid',
  full_name='common.v1.XiBareUserJidOrAliasJid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bare_user_jid', full_name='common.v1.XiBareUserJidOrAliasJid.bare_user_jid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alias_user_jid', full_name='common.v1.XiBareUserJidOrAliasJid.alias_user_jid', index=1,
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
    _descriptor.OneofDescriptor(
      name='jid_type', full_name='common.v1.XiBareUserJidOrAliasJid.jid_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=169,
  serialized_end=303,
)


_XIANYJID = _descriptor.Descriptor(
  name='XiAnyJid',
  full_name='common.v1.XiAnyJid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bare_user_jid', full_name='common.v1.XiAnyJid.bare_user_jid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alias_user_jid', full_name='common.v1.XiAnyJid.alias_user_jid', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_jid', full_name='common.v1.XiAnyJid.group_jid', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='jid_type', full_name='common.v1.XiAnyJid.jid_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=306,
  serialized_end=466,
)


_XIKINUSERID = _descriptor.Descriptor(
  name='XiKinUserId',
  full_name='common.v1.XiKinUserId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='common.v1.XiKinUserId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\022\010\001\022\016^[a-z2-7]{52}$'))),
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
  serialized_start=468,
  serialized_end=517,
)


_XICONVOID = _descriptor.Descriptor(
  name='XiConvoId',
  full_name='common.v1.XiConvoId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='one_to_one', full_name='common.v1.XiConvoId.one_to_one', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='common.v1.XiConvoId.group', index=1,
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
    _descriptor.OneofDescriptor(
      name='kind', full_name='common.v1.XiConvoId.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=519,
  serialized_end=625,
)


_ONETOONECONVOID = _descriptor.Descriptor(
  name='OneToOneConvoId',
  full_name='common.v1.OneToOneConvoId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='common.v1.OneToOneConvoId.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\n\010\001x\002\200\001\002\210\001\000'))),
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
  serialized_start=627,
  serialized_end=698,
)


_XIJWT = _descriptor.Descriptor(
  name='XiJWT',
  full_name='common.v1.XiJWT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jwt', full_name='common.v1.XiJWT.jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%5\010\001\0221^[a-zA-Z0-9-_]+?.[a-zA-Z0-9-_]+?.[a-zA-Z0-9-_]+?$'))),
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
  serialized_start=700,
  serialized_end=779,
)

_XIBAREUSERJIDORALIASJID.fields_by_name['bare_user_jid'].message_type = common__model__pb2._XIBAREUSERJID
_XIBAREUSERJIDORALIASJID.fields_by_name['alias_user_jid'].message_type = _XIALIASJID
_XIBAREUSERJIDORALIASJID.oneofs_by_name['jid_type'].fields.append(
  _XIBAREUSERJIDORALIASJID.fields_by_name['bare_user_jid'])
_XIBAREUSERJIDORALIASJID.fields_by_name['bare_user_jid'].containing_oneof = _XIBAREUSERJIDORALIASJID.oneofs_by_name['jid_type']
_XIBAREUSERJIDORALIASJID.oneofs_by_name['jid_type'].fields.append(
  _XIBAREUSERJIDORALIASJID.fields_by_name['alias_user_jid'])
_XIBAREUSERJIDORALIASJID.fields_by_name['alias_user_jid'].containing_oneof = _XIBAREUSERJIDORALIASJID.oneofs_by_name['jid_type']
_XIANYJID.fields_by_name['bare_user_jid'].message_type = common__model__pb2._XIBAREUSERJID
_XIANYJID.fields_by_name['alias_user_jid'].message_type = _XIALIASJID
_XIANYJID.fields_by_name['group_jid'].message_type = common__model__pb2._XIGROUPJID
_XIANYJID.oneofs_by_name['jid_type'].fields.append(
  _XIANYJID.fields_by_name['bare_user_jid'])
_XIANYJID.fields_by_name['bare_user_jid'].containing_oneof = _XIANYJID.oneofs_by_name['jid_type']
_XIANYJID.oneofs_by_name['jid_type'].fields.append(
  _XIANYJID.fields_by_name['alias_user_jid'])
_XIANYJID.fields_by_name['alias_user_jid'].containing_oneof = _XIANYJID.oneofs_by_name['jid_type']
_XIANYJID.oneofs_by_name['jid_type'].fields.append(
  _XIANYJID.fields_by_name['group_jid'])
_XIANYJID.fields_by_name['group_jid'].containing_oneof = _XIANYJID.oneofs_by_name['jid_type']
_XICONVOID.fields_by_name['one_to_one'].message_type = _ONETOONECONVOID
_XICONVOID.fields_by_name['group'].message_type = common__model__pb2._XIGROUPJID
_XICONVOID.oneofs_by_name['kind'].fields.append(
  _XICONVOID.fields_by_name['one_to_one'])
_XICONVOID.fields_by_name['one_to_one'].containing_oneof = _XICONVOID.oneofs_by_name['kind']
_XICONVOID.oneofs_by_name['kind'].fields.append(
  _XICONVOID.fields_by_name['group'])
_XICONVOID.fields_by_name['group'].containing_oneof = _XICONVOID.oneofs_by_name['kind']
_ONETOONECONVOID.fields_by_name['users'].message_type = common__model__pb2._XIBAREUSERJID
DESCRIPTOR.message_types_by_name['XiAliasJid'] = _XIALIASJID
DESCRIPTOR.message_types_by_name['XiBareUserJidOrAliasJid'] = _XIBAREUSERJIDORALIASJID
DESCRIPTOR.message_types_by_name['XiAnyJid'] = _XIANYJID
DESCRIPTOR.message_types_by_name['XiKinUserId'] = _XIKINUSERID
DESCRIPTOR.message_types_by_name['XiConvoId'] = _XICONVOID
DESCRIPTOR.message_types_by_name['OneToOneConvoId'] = _ONETOONECONVOID
DESCRIPTOR.message_types_by_name['XiJWT'] = _XIJWT

XiAliasJid = _reflection.GeneratedProtocolMessageType('XiAliasJid', (_message.Message,), dict(
  DESCRIPTOR = _XIALIASJID,
  __module__ = 'common.v1.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v1.XiAliasJid)
  ))
_sym_db.RegisterMessage(XiAliasJid)

XiBareUserJidOrAliasJid = _reflection.GeneratedProtocolMessageType('XiBareUserJidOrAliasJid', (_message.Message,), dict(
  DESCRIPTOR = _XIBAREUSERJIDORALIASJID,
  __module__ = 'common.v1.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v1.XiBareUserJidOrAliasJid)
  ))
_sym_db.RegisterMessage(XiBareUserJidOrAliasJid)

XiAnyJid = _reflection.GeneratedProtocolMessageType('XiAnyJid', (_message.Message,), dict(
  DESCRIPTOR = _XIANYJID,
  __module__ = 'common.v1.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v1.XiAnyJid)
  ))
_sym_db.RegisterMessage(XiAnyJid)

XiKinUserId = _reflection.GeneratedProtocolMessageType('XiKinUserId', (_message.Message,), dict(
  DESCRIPTOR = _XIKINUSERID,
  __module__ = 'common.v1.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v1.XiKinUserId)
  ))
_sym_db.RegisterMessage(XiKinUserId)

XiConvoId = _reflection.GeneratedProtocolMessageType('XiConvoId', (_message.Message,), dict(
  DESCRIPTOR = _XICONVOID,
  __module__ = 'common.v1.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v1.XiConvoId)
  ))
_sym_db.RegisterMessage(XiConvoId)

OneToOneConvoId = _reflection.GeneratedProtocolMessageType('OneToOneConvoId', (_message.Message,), dict(
  DESCRIPTOR = _ONETOONECONVOID,
  __module__ = 'common.v1.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v1.OneToOneConvoId)
  ))
_sym_db.RegisterMessage(OneToOneConvoId)

XiJWT = _reflection.GeneratedProtocolMessageType('XiJWT', (_message.Message,), dict(
  DESCRIPTOR = _XIJWT,
  __module__ = 'common.v1.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v1.XiJWT)
  ))
_sym_db.RegisterMessage(XiJWT)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\016com.kik.commonB\nModelProtoP\001ZLgithub.com/kikinteractive/xiphias-model-common/generated/go/common/v1;common\240\001\001\242\002\003KPB\252\243*\002\010\001'))
_XIALIASJID.fields_by_name['local_part'].has_options = True
_XIALIASJID.fields_by_name['local_part']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\032\010\001\022\026^[a-z0-9_-]{52}_[a|b]$'))
_XIKINUSERID.fields_by_name['id'].has_options = True
_XIKINUSERID.fields_by_name['id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\022\010\001\022\016^[a-z2-7]{52}$'))
_ONETOONECONVOID.fields_by_name['users'].has_options = True
_ONETOONECONVOID.fields_by_name['users']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\n\010\001x\002\200\001\002\210\001\000'))
_XIJWT.fields_by_name['jwt'].has_options = True
_XIJWT.fields_by_name['jwt']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%5\010\001\0221^[a-zA-Z0-9-_]+?.[a-zA-Z0-9-_]+?.[a-zA-Z0-9-_]+?$'))
# @@protoc_insertion_point(module_scope)
