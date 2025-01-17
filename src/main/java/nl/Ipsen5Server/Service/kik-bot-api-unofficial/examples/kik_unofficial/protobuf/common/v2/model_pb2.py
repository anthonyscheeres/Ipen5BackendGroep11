# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/v2/model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import kik_unofficial.protobuf.kik_options_pb2 as kik__options__pb2
import kik_unofficial.protobuf.protobuf_validation_pb2 as protobuf__validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/v2/model.proto',
  package='common.v2',
  syntax='proto3',
  serialized_pb=_b('\n\x15\x63ommon/v2/model.proto\x12\tcommon.v2\x1a\x11kik_options.proto\x1a\x19protobuf_validation.proto\"K\n\tAccountId\x12>\n\nlocal_part\x18\x01 \x01(\tB*\xca\x9d%&\x08\x01\x12\"^[a-z_0-9\\.]{2,30}(_[a-z0-9]{3})?$\")\n\tPersonaId\x12\x1c\n\traw_value\x18\x01 \x01(\x0c\x42\t\xca\x9d%\x05\x08\x01\x30\x80\x01\"(\n\x06\x43hatId\x12\x1e\n\traw_value\x18\x01 \x01(\x0c\x42\x0b\xca\x9d%\x07\x08\x01(\x01\x30\x80\x04\"A\n\nOneToOneId\x12\x33\n\x08personas\x18\x01 \x03(\x0b\x32\x14.common.v2.PersonaIdB\x0b\xca\x9d%\x07\x08\x01x\x02\x80\x01\x02\"/\n\x10\x43lientInstanceId\x12\x1b\n\traw_value\x18\x01 \x01(\x0c\x42\x08\xca\x9d%\x04\x08\x01\x30\x64\"%\n\x04Uuid\x12\x1d\n\traw_value\x18\x01 \x01(\x0c\x42\n\xca\x9d%\x06\x08\x01(\x10\x30\x10\"\x82\x01\n\x05\x45mail\x12y\n\x05\x65mail\x18\x01 \x01(\tBj\xca\x9d%f\x08\x01\x12_^[\\w\\-+]+(\\.[\\w\\-+]+)*@[A-Za-z0-9][A-Za-z0-9\\-]*(\\.[A-Za-z0-9][A-Za-z0-9\\-]*)*(\\.[A-Za-z]{2,})$0\xf8\x07\"4\n\x08Username\x12(\n\x08username\x18\x02 \x01(\tB\x16\xca\x9d%\x12\x08\x01\x12\x0e^[\\w\\.]{2,30}$B~\n\x15\x63om.kik.gen.common.v2P\x01ZLgithub.com/kikinteractive/xiphias-model-common/generated/go/common/v2;common\xa0\x01\x01\xa2\x02\x0bKPBCommonV2\xaa\xa3*\x02\x08\x01\x62\x06proto3')
  ,
  dependencies=[kik__options__pb2.DESCRIPTOR,protobuf__validation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ACCOUNTID = _descriptor.Descriptor(
  name='AccountId',
  full_name='common.v2.AccountId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='local_part', full_name='common.v2.AccountId.local_part', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%&\010\001\022\"^[a-z_0-9\\.]{2,30}(_[a-z0-9]{3})?$'))),
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
  serialized_start=82,
  serialized_end=157,
)


_PERSONAID = _descriptor.Descriptor(
  name='PersonaId',
  full_name='common.v2.PersonaId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_value', full_name='common.v2.PersonaId.raw_value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\0010\200\001'))),
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
  serialized_start=159,
  serialized_end=200,
)


_CHATID = _descriptor.Descriptor(
  name='ChatId',
  full_name='common.v2.ChatId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_value', full_name='common.v2.ChatId.raw_value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001(\0010\200\004'))),
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
  serialized_start=202,
  serialized_end=242,
)


_ONETOONEID = _descriptor.Descriptor(
  name='OneToOneId',
  full_name='common.v2.OneToOneId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='personas', full_name='common.v2.OneToOneId.personas', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001x\002\200\001\002'))),
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
  serialized_start=244,
  serialized_end=309,
)


_CLIENTINSTANCEID = _descriptor.Descriptor(
  name='ClientInstanceId',
  full_name='common.v2.ClientInstanceId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_value', full_name='common.v2.ClientInstanceId.raw_value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\004\010\0010d'))),
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
  serialized_start=311,
  serialized_end=358,
)


_UUID = _descriptor.Descriptor(
  name='Uuid',
  full_name='common.v2.Uuid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_value', full_name='common.v2.Uuid.raw_value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006\010\001(\0200\020'))),
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
  serialized_start=360,
  serialized_end=397,
)


_EMAIL = _descriptor.Descriptor(
  name='Email',
  full_name='common.v2.Email',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='common.v2.Email.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%f\010\001\022_^[\\w\\-+]+(\\.[\\w\\-+]+)*@[A-Za-z0-9][A-Za-z0-9\\-]*(\\.[A-Za-z0-9][A-Za-z0-9\\-]*)*(\\.[A-Za-z]{2,})$0\370\007'))),
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
  serialized_start=400,
  serialized_end=530,
)


_USERNAME = _descriptor.Descriptor(
  name='Username',
  full_name='common.v2.Username',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='common.v2.Username.username', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\022\010\001\022\016^[\\w\\.]{2,30}$'))),
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
  serialized_start=532,
  serialized_end=584,
)

_ONETOONEID.fields_by_name['personas'].message_type = _PERSONAID
DESCRIPTOR.message_types_by_name['AccountId'] = _ACCOUNTID
DESCRIPTOR.message_types_by_name['PersonaId'] = _PERSONAID
DESCRIPTOR.message_types_by_name['ChatId'] = _CHATID
DESCRIPTOR.message_types_by_name['OneToOneId'] = _ONETOONEID
DESCRIPTOR.message_types_by_name['ClientInstanceId'] = _CLIENTINSTANCEID
DESCRIPTOR.message_types_by_name['Uuid'] = _UUID
DESCRIPTOR.message_types_by_name['Email'] = _EMAIL
DESCRIPTOR.message_types_by_name['Username'] = _USERNAME

AccountId = _reflection.GeneratedProtocolMessageType('AccountId', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTID,
  __module__ = 'common.v2.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v2.AccountId)
  ))
_sym_db.RegisterMessage(AccountId)

PersonaId = _reflection.GeneratedProtocolMessageType('PersonaId', (_message.Message,), dict(
  DESCRIPTOR = _PERSONAID,
  __module__ = 'common.v2.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v2.PersonaId)
  ))
_sym_db.RegisterMessage(PersonaId)

ChatId = _reflection.GeneratedProtocolMessageType('ChatId', (_message.Message,), dict(
  DESCRIPTOR = _CHATID,
  __module__ = 'common.v2.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v2.ChatId)
  ))
_sym_db.RegisterMessage(ChatId)

OneToOneId = _reflection.GeneratedProtocolMessageType('OneToOneId', (_message.Message,), dict(
  DESCRIPTOR = _ONETOONEID,
  __module__ = 'common.v2.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v2.OneToOneId)
  ))
_sym_db.RegisterMessage(OneToOneId)

ClientInstanceId = _reflection.GeneratedProtocolMessageType('ClientInstanceId', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTINSTANCEID,
  __module__ = 'common.v2.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v2.ClientInstanceId)
  ))
_sym_db.RegisterMessage(ClientInstanceId)

Uuid = _reflection.GeneratedProtocolMessageType('Uuid', (_message.Message,), dict(
  DESCRIPTOR = _UUID,
  __module__ = 'common.v2.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v2.Uuid)
  ))
_sym_db.RegisterMessage(Uuid)

Email = _reflection.GeneratedProtocolMessageType('Email', (_message.Message,), dict(
  DESCRIPTOR = _EMAIL,
  __module__ = 'common.v2.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v2.Email)
  ))
_sym_db.RegisterMessage(Email)

Username = _reflection.GeneratedProtocolMessageType('Username', (_message.Message,), dict(
  DESCRIPTOR = _USERNAME,
  __module__ = 'common.v2.model_pb2'
  # @@protoc_insertion_point(class_scope:common.v2.Username)
  ))
_sym_db.RegisterMessage(Username)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025com.kik.gen.common.v2P\001ZLgithub.com/kikinteractive/xiphias-model-common/generated/go/common/v2;common\240\001\001\242\002\013KPBCommonV2\252\243*\002\010\001'))
_ACCOUNTID.fields_by_name['local_part'].has_options = True
_ACCOUNTID.fields_by_name['local_part']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%&\010\001\022\"^[a-z_0-9\\.]{2,30}(_[a-z0-9]{3})?$'))
_PERSONAID.fields_by_name['raw_value'].has_options = True
_PERSONAID.fields_by_name['raw_value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\0010\200\001'))
_CHATID.fields_by_name['raw_value'].has_options = True
_CHATID.fields_by_name['raw_value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001(\0010\200\004'))
_ONETOONEID.fields_by_name['personas'].has_options = True
_ONETOONEID.fields_by_name['personas']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001x\002\200\001\002'))
_CLIENTINSTANCEID.fields_by_name['raw_value'].has_options = True
_CLIENTINSTANCEID.fields_by_name['raw_value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\004\010\0010d'))
_UUID.fields_by_name['raw_value'].has_options = True
_UUID.fields_by_name['raw_value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006\010\001(\0200\020'))
_EMAIL.fields_by_name['email'].has_options = True
_EMAIL.fields_by_name['email']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%f\010\001\022_^[\\w\\-+]+(\\.[\\w\\-+]+)*@[A-Za-z0-9][A-Za-z0-9\\-]*(\\.[A-Za-z0-9][A-Za-z0-9\\-]*)*(\\.[A-Za-z]{2,})$0\370\007'))
_USERNAME.fields_by_name['username'].has_options = True
_USERNAME.fields_by_name['username']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\022\010\001\022\016^[\\w\\.]{2,30}$'))
# @@protoc_insertion_point(module_scope)
