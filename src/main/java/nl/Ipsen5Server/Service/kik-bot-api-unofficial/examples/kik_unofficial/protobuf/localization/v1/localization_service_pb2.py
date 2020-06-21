# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: localization/v1/localization_service.proto

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
import kik_unofficial.protobuf.protobuf_validation_pb2 as protobuf__validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='localization/v1/localization_service.proto',
  package='mobile.localization.v1',
  syntax='proto3',
  serialized_pb=_b('\n*localization/v1/localization_service.proto\x12\x16mobile.localization.v1\x1a\x12\x63ommon_model.proto\x1a\x19protobuf_validation.proto\"w\n\x10GetStringRequest\x12;\n\tstring_id\x18\x01 \x01(\x0b\x32 .mobile.localization.v1.StringIdB\x06\xca\x9d%\x02\x08\x01\x12 \n\x06locale\x18\x02 \x01(\x0b\x32\x10.common.XiLocaleJ\x04\x08\x03\x10\x04\"\x8e\x02\n\x11GetStringResponse\x12@\n\x06result\x18\x01 \x01(\x0e\x32\x30.mobile.localization.v1.GetStringResponse.Result\x12;\n\tstring_id\x18\x02 \x01(\x0b\x32 .mobile.localization.v1.StringIdB\x06\xca\x9d%\x02\x08\x01\x12\x38\n\x0cstring_value\x18\x03 \x01(\x0b\x32\".mobile.localization.v1.StringText\"@\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x14\n\x10STRING_NOT_FOUND\x10\x01\x12\x18\n\x14LOCALE_NOT_AVAILABLE\x10\x02\"\x7f\n\x11GetStringsRequest\x12\x42\n\nstring_ids\x18\x01 \x03(\x0b\x32 .mobile.localization.v1.StringIdB\x0c\xca\x9d%\x08\x08\x01x\x01\x80\x01\x80\x08\x12 \n\x06locale\x18\x02 \x01(\x0b\x32\x10.common.XiLocaleJ\x04\x08\x03\x10\x04\"#\n\x08StringId\x12\x17\n\x02id\x18\x01 \x01(\tB\x0b\xca\x9d%\x07\x08\x01(\x01\x30\xff\x01\"(\n\nStringText\x12\x1a\n\x04text\x18\x01 \x01(\tB\x0c\xca\x9d%\x08\x08\x01(\x01\x30\xff\xff\x03\"N\n\x13\x45xperimentSubjectId\x12)\n\x08user_jid\x18\x01 \x01(\x0b\x32\x15.common.XiBareUserJidH\x00\x42\x0c\n\nsubject_id2\xda\x01\n\x0cLocalization\x12\x62\n\tGetString\x12(.mobile.localization.v1.GetStringRequest\x1a).mobile.localization.v1.GetStringResponse\"\x00\x12\x66\n\nGetStrings\x12).mobile.localization.v1.GetStringsRequest\x1a).mobile.localization.v1.GetStringResponse\"\x00\x30\x01\x42r\n\x18\x63om.kik.localization.rpcZVgithub.com/kikinteractive/xiphias-api-mobile/generated/go/localization/v1;localizationb\x06proto3')
  ,
  dependencies=[common__model__pb2.DESCRIPTOR,protobuf__validation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETSTRINGRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.localization.v1.GetStringResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING_NOT_FOUND', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCALE_NOT_AVAILABLE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=445,
  serialized_end=509,
)
_sym_db.RegisterEnumDescriptor(_GETSTRINGRESPONSE_RESULT)


_GETSTRINGREQUEST = _descriptor.Descriptor(
  name='GetStringRequest',
  full_name='mobile.localization.v1.GetStringRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='string_id', full_name='mobile.localization.v1.GetStringRequest.string_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='locale', full_name='mobile.localization.v1.GetStringRequest.locale', index=1,
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
  serialized_start=117,
  serialized_end=236,
)


_GETSTRINGRESPONSE = _descriptor.Descriptor(
  name='GetStringResponse',
  full_name='mobile.localization.v1.GetStringResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.localization.v1.GetStringResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_id', full_name='mobile.localization.v1.GetStringResponse.string_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='mobile.localization.v1.GetStringResponse.string_value', index=2,
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
    _GETSTRINGRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=509,
)


_GETSTRINGSREQUEST = _descriptor.Descriptor(
  name='GetStringsRequest',
  full_name='mobile.localization.v1.GetStringsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='string_ids', full_name='mobile.localization.v1.GetStringsRequest.string_ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\010\010\001x\001\200\001\200\010'))),
    _descriptor.FieldDescriptor(
      name='locale', full_name='mobile.localization.v1.GetStringsRequest.locale', index=1,
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
  serialized_start=511,
  serialized_end=638,
)


_STRINGID = _descriptor.Descriptor(
  name='StringId',
  full_name='mobile.localization.v1.StringId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mobile.localization.v1.StringId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001(\0010\377\001'))),
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
  serialized_start=640,
  serialized_end=675,
)


_STRINGTEXT = _descriptor.Descriptor(
  name='StringText',
  full_name='mobile.localization.v1.StringText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='mobile.localization.v1.StringText.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\010\010\001(\0010\377\377\003'))),
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
  serialized_start=677,
  serialized_end=717,
)


_EXPERIMENTSUBJECTID = _descriptor.Descriptor(
  name='ExperimentSubjectId',
  full_name='mobile.localization.v1.ExperimentSubjectId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_jid', full_name='mobile.localization.v1.ExperimentSubjectId.user_jid', index=0,
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
    _descriptor.OneofDescriptor(
      name='subject_id', full_name='mobile.localization.v1.ExperimentSubjectId.subject_id',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=719,
  serialized_end=797,
)

_GETSTRINGREQUEST.fields_by_name['string_id'].message_type = _STRINGID
_GETSTRINGREQUEST.fields_by_name['locale'].message_type = common__model__pb2._XILOCALE
_GETSTRINGRESPONSE.fields_by_name['result'].enum_type = _GETSTRINGRESPONSE_RESULT
_GETSTRINGRESPONSE.fields_by_name['string_id'].message_type = _STRINGID
_GETSTRINGRESPONSE.fields_by_name['string_value'].message_type = _STRINGTEXT
_GETSTRINGRESPONSE_RESULT.containing_type = _GETSTRINGRESPONSE
_GETSTRINGSREQUEST.fields_by_name['string_ids'].message_type = _STRINGID
_GETSTRINGSREQUEST.fields_by_name['locale'].message_type = common__model__pb2._XILOCALE
_EXPERIMENTSUBJECTID.fields_by_name['user_jid'].message_type = common__model__pb2._XIBAREUSERJID
_EXPERIMENTSUBJECTID.oneofs_by_name['subject_id'].fields.append(
  _EXPERIMENTSUBJECTID.fields_by_name['user_jid'])
_EXPERIMENTSUBJECTID.fields_by_name['user_jid'].containing_oneof = _EXPERIMENTSUBJECTID.oneofs_by_name['subject_id']
DESCRIPTOR.message_types_by_name['GetStringRequest'] = _GETSTRINGREQUEST
DESCRIPTOR.message_types_by_name['GetStringResponse'] = _GETSTRINGRESPONSE
DESCRIPTOR.message_types_by_name['GetStringsRequest'] = _GETSTRINGSREQUEST
DESCRIPTOR.message_types_by_name['StringId'] = _STRINGID
DESCRIPTOR.message_types_by_name['StringText'] = _STRINGTEXT
DESCRIPTOR.message_types_by_name['ExperimentSubjectId'] = _EXPERIMENTSUBJECTID

GetStringRequest = _reflection.GeneratedProtocolMessageType('GetStringRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSTRINGREQUEST,
  __module__ = 'localization.v1.localization_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.localization.v1.GetStringRequest)
  ))
_sym_db.RegisterMessage(GetStringRequest)

GetStringResponse = _reflection.GeneratedProtocolMessageType('GetStringResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETSTRINGRESPONSE,
  __module__ = 'localization.v1.localization_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.localization.v1.GetStringResponse)
  ))
_sym_db.RegisterMessage(GetStringResponse)

GetStringsRequest = _reflection.GeneratedProtocolMessageType('GetStringsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSTRINGSREQUEST,
  __module__ = 'localization.v1.localization_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.localization.v1.GetStringsRequest)
  ))
_sym_db.RegisterMessage(GetStringsRequest)

StringId = _reflection.GeneratedProtocolMessageType('StringId', (_message.Message,), dict(
  DESCRIPTOR = _STRINGID,
  __module__ = 'localization.v1.localization_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.localization.v1.StringId)
  ))
_sym_db.RegisterMessage(StringId)

StringText = _reflection.GeneratedProtocolMessageType('StringText', (_message.Message,), dict(
  DESCRIPTOR = _STRINGTEXT,
  __module__ = 'localization.v1.localization_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.localization.v1.StringText)
  ))
_sym_db.RegisterMessage(StringText)

ExperimentSubjectId = _reflection.GeneratedProtocolMessageType('ExperimentSubjectId', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENTSUBJECTID,
  __module__ = 'localization.v1.localization_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.localization.v1.ExperimentSubjectId)
  ))
_sym_db.RegisterMessage(ExperimentSubjectId)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030com.kik.localization.rpcZVgithub.com/kikinteractive/xiphias-api-mobile/generated/go/localization/v1;localization'))
_GETSTRINGREQUEST.fields_by_name['string_id'].has_options = True
_GETSTRINGREQUEST.fields_by_name['string_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_GETSTRINGRESPONSE.fields_by_name['string_id'].has_options = True
_GETSTRINGRESPONSE.fields_by_name['string_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_GETSTRINGSREQUEST.fields_by_name['string_ids'].has_options = True
_GETSTRINGSREQUEST.fields_by_name['string_ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\010\010\001x\001\200\001\200\010'))
_STRINGID.fields_by_name['id'].has_options = True
_STRINGID.fields_by_name['id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001(\0010\377\001'))
_STRINGTEXT.fields_by_name['text'].has_options = True
_STRINGTEXT.fields_by_name['text']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\010\010\001(\0010\377\377\003'))
# @@protoc_insertion_point(module_scope)
