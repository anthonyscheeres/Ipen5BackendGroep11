# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: persona/v2/persona_info_service.proto

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
from kik_unofficial.protobuf.common.v2 import model_pb2 as common_dot_v2_dot_model__pb2
from kik_unofficial.protobuf.persona.v2 import persona_common_pb2 as persona_dot_v2_dot_persona__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='persona/v2/persona_info_service.proto',
  package='mobile.persona.v2',
  syntax='proto3',
  serialized_pb=_b('\n%persona/v2/persona_info_service.proto\x12\x11mobile.persona.v2\x1a\x19protobuf_validation.proto\x1a\x15\x63ommon/v2/model.proto\x1a\x1fpersona/v2/persona_common.proto\"Q\n\x16GetPersonaShortRequest\x12\x37\n\x0bpersona_ids\x18\x01 \x03(\x0b\x32\x14.common.v2.PersonaIdB\x0c\xca\x9d%\x08\x08\x01x\x01\x80\x01\x80\x08\"\x9c\x02\n\x17GetPersonaShortResponse\x12\x41\n\x06result\x18\x01 \x01(\x0e\x32\x31.mobile.persona.v2.GetPersonaShortResponse.Result\x12=\n\x08personas\x18\x02 \x03(\x0b\x32\x1f.common.persona.v2.PersonaShortB\n\xca\x9d%\x06x\x00\x80\x01\x80\x08\x12\x37\n\rnot_found_ids\x18\x03 \x03(\x0b\x32\x14.common.v2.PersonaIdB\n\xca\x9d%\x06x\x00\x80\x01\x80\x08\x12\x34\n\nfailed_ids\x18\x04 \x03(\x0b\x32\x14.common.v2.PersonaIdB\n\xca\x9d%\x06x\x00\x80\x01\x80\x08\"\x10\n\x06Result\x12\x06\n\x02OK\x10\x00\"P\n\x15GetPersonaFullRequest\x12\x37\n\x0bpersona_ids\x18\x01 \x03(\x0b\x32\x14.common.v2.PersonaIdB\x0c\xca\x9d%\x08\x08\x01x\x01\x80\x01\x80\x08\"\x99\x02\n\x16GetPersonaFullResponse\x12@\n\x06result\x18\x01 \x01(\x0e\x32\x30.mobile.persona.v2.GetPersonaFullResponse.Result\x12<\n\x08personas\x18\x02 \x03(\x0b\x32\x1e.common.persona.v2.PersonaFullB\n\xca\x9d%\x06x\x00\x80\x01\x80\x08\x12\x37\n\rnot_found_ids\x18\x03 \x03(\x0b\x32\x14.common.v2.PersonaIdB\n\xca\x9d%\x06x\x00\x80\x01\x80\x08\x12\x34\n\nfailed_ids\x18\x04 \x03(\x0b\x32\x14.common.v2.PersonaIdB\n\xca\x9d%\x06x\x00\x80\x01\x80\x08\"\x10\n\x06Result\x12\x06\n\x02OK\x10\x00\"P\n\x1fGetPersonaFullByUsernameRequest\x12-\n\x08username\x18\x01 \x01(\x0b\x32\x13.common.v2.UsernameB\x06\xca\x9d%\x02\x08\x01\"\xc0\x01\n GetPersonaFullByUsernameResponse\x12J\n\x06result\x18\x01 \x01(\x0e\x32:.mobile.persona.v2.GetPersonaFullByUsernameResponse.Result\x12/\n\x07persona\x18\x02 \x01(\x0b\x32\x1e.common.persona.v2.PersonaFull\"\x1f\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\r\n\tNOT_FOUND\x10\x01\x32\xea\x02\n\x0bPersonaInfo\x12j\n\x0fGetPersonaShort\x12).mobile.persona.v2.GetPersonaShortRequest\x1a*.mobile.persona.v2.GetPersonaShortResponse\"\x00\x12g\n\x0eGetPersonaFull\x12(.mobile.persona.v2.GetPersonaFullRequest\x1a).mobile.persona.v2.GetPersonaFullResponse\"\x00\x12\x85\x01\n\x18GetPersonaFullByUsername\x12\x32.mobile.persona.v2.GetPersonaFullByUsernameRequest\x1a\x33.mobile.persona.v2.GetPersonaFullByUsernameResponse\"\x00\x42{\n\x16\x63om.kik.gen.persona.v2ZLgithub.com/kikinteractive/xiphias-api-mobile/generated/go/persona/v2;persona\xa2\x02\x12KPBMobilePersonaV2b\x06proto3')
  ,
  dependencies=[protobuf__validation__pb2.DESCRIPTOR,common_dot_v2_dot_model__pb2.DESCRIPTOR,persona_dot_v2_dot_persona__common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETPERSONASHORTRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.persona.v2.GetPersonaShortResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=495,
  serialized_end=511,
)
_sym_db.RegisterEnumDescriptor(_GETPERSONASHORTRESPONSE_RESULT)

_GETPERSONAFULLRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.persona.v2.GetPersonaFullResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=495,
  serialized_end=511,
)
_sym_db.RegisterEnumDescriptor(_GETPERSONAFULLRESPONSE_RESULT)

_GETPERSONAFULLBYUSERNAMERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.persona.v2.GetPersonaFullByUsernameResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1123,
  serialized_end=1154,
)
_sym_db.RegisterEnumDescriptor(_GETPERSONAFULLBYUSERNAMERESPONSE_RESULT)


_GETPERSONASHORTREQUEST = _descriptor.Descriptor(
  name='GetPersonaShortRequest',
  full_name='mobile.persona.v2.GetPersonaShortRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='persona_ids', full_name='mobile.persona.v2.GetPersonaShortRequest.persona_ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\010\010\001x\001\200\001\200\010'))),
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
  serialized_start=143,
  serialized_end=224,
)


_GETPERSONASHORTRESPONSE = _descriptor.Descriptor(
  name='GetPersonaShortResponse',
  full_name='mobile.persona.v2.GetPersonaShortResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.persona.v2.GetPersonaShortResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='personas', full_name='mobile.persona.v2.GetPersonaShortResponse.personas', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006x\000\200\001\200\010'))),
    _descriptor.FieldDescriptor(
      name='not_found_ids', full_name='mobile.persona.v2.GetPersonaShortResponse.not_found_ids', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006x\000\200\001\200\010'))),
    _descriptor.FieldDescriptor(
      name='failed_ids', full_name='mobile.persona.v2.GetPersonaShortResponse.failed_ids', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006x\000\200\001\200\010'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETPERSONASHORTRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=511,
)


_GETPERSONAFULLREQUEST = _descriptor.Descriptor(
  name='GetPersonaFullRequest',
  full_name='mobile.persona.v2.GetPersonaFullRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='persona_ids', full_name='mobile.persona.v2.GetPersonaFullRequest.persona_ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\010\010\001x\001\200\001\200\010'))),
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
  serialized_start=513,
  serialized_end=593,
)


_GETPERSONAFULLRESPONSE = _descriptor.Descriptor(
  name='GetPersonaFullResponse',
  full_name='mobile.persona.v2.GetPersonaFullResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.persona.v2.GetPersonaFullResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='personas', full_name='mobile.persona.v2.GetPersonaFullResponse.personas', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006x\000\200\001\200\010'))),
    _descriptor.FieldDescriptor(
      name='not_found_ids', full_name='mobile.persona.v2.GetPersonaFullResponse.not_found_ids', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006x\000\200\001\200\010'))),
    _descriptor.FieldDescriptor(
      name='failed_ids', full_name='mobile.persona.v2.GetPersonaFullResponse.failed_ids', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006x\000\200\001\200\010'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETPERSONAFULLRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=596,
  serialized_end=877,
)


_GETPERSONAFULLBYUSERNAMEREQUEST = _descriptor.Descriptor(
  name='GetPersonaFullByUsernameRequest',
  full_name='mobile.persona.v2.GetPersonaFullByUsernameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='mobile.persona.v2.GetPersonaFullByUsernameRequest.username', index=0,
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
  serialized_start=879,
  serialized_end=959,
)


_GETPERSONAFULLBYUSERNAMERESPONSE = _descriptor.Descriptor(
  name='GetPersonaFullByUsernameResponse',
  full_name='mobile.persona.v2.GetPersonaFullByUsernameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.persona.v2.GetPersonaFullByUsernameResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='persona', full_name='mobile.persona.v2.GetPersonaFullByUsernameResponse.persona', index=1,
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
    _GETPERSONAFULLBYUSERNAMERESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=962,
  serialized_end=1154,
)

_GETPERSONASHORTREQUEST.fields_by_name['persona_ids'].message_type = common_dot_v2_dot_model__pb2._PERSONAID
_GETPERSONASHORTRESPONSE.fields_by_name['result'].enum_type = _GETPERSONASHORTRESPONSE_RESULT
_GETPERSONASHORTRESPONSE.fields_by_name['personas'].message_type = persona_dot_v2_dot_persona__common__pb2._PERSONASHORT
_GETPERSONASHORTRESPONSE.fields_by_name['not_found_ids'].message_type = common_dot_v2_dot_model__pb2._PERSONAID
_GETPERSONASHORTRESPONSE.fields_by_name['failed_ids'].message_type = common_dot_v2_dot_model__pb2._PERSONAID
_GETPERSONASHORTRESPONSE_RESULT.containing_type = _GETPERSONASHORTRESPONSE
_GETPERSONAFULLREQUEST.fields_by_name['persona_ids'].message_type = common_dot_v2_dot_model__pb2._PERSONAID
_GETPERSONAFULLRESPONSE.fields_by_name['result'].enum_type = _GETPERSONAFULLRESPONSE_RESULT
_GETPERSONAFULLRESPONSE.fields_by_name['personas'].message_type = persona_dot_v2_dot_persona__common__pb2._PERSONAFULL
_GETPERSONAFULLRESPONSE.fields_by_name['not_found_ids'].message_type = common_dot_v2_dot_model__pb2._PERSONAID
_GETPERSONAFULLRESPONSE.fields_by_name['failed_ids'].message_type = common_dot_v2_dot_model__pb2._PERSONAID
_GETPERSONAFULLRESPONSE_RESULT.containing_type = _GETPERSONAFULLRESPONSE
_GETPERSONAFULLBYUSERNAMEREQUEST.fields_by_name['username'].message_type = common_dot_v2_dot_model__pb2._USERNAME
_GETPERSONAFULLBYUSERNAMERESPONSE.fields_by_name['result'].enum_type = _GETPERSONAFULLBYUSERNAMERESPONSE_RESULT
_GETPERSONAFULLBYUSERNAMERESPONSE.fields_by_name['persona'].message_type = persona_dot_v2_dot_persona__common__pb2._PERSONAFULL
_GETPERSONAFULLBYUSERNAMERESPONSE_RESULT.containing_type = _GETPERSONAFULLBYUSERNAMERESPONSE
DESCRIPTOR.message_types_by_name['GetPersonaShortRequest'] = _GETPERSONASHORTREQUEST
DESCRIPTOR.message_types_by_name['GetPersonaShortResponse'] = _GETPERSONASHORTRESPONSE
DESCRIPTOR.message_types_by_name['GetPersonaFullRequest'] = _GETPERSONAFULLREQUEST
DESCRIPTOR.message_types_by_name['GetPersonaFullResponse'] = _GETPERSONAFULLRESPONSE
DESCRIPTOR.message_types_by_name['GetPersonaFullByUsernameRequest'] = _GETPERSONAFULLBYUSERNAMEREQUEST
DESCRIPTOR.message_types_by_name['GetPersonaFullByUsernameResponse'] = _GETPERSONAFULLBYUSERNAMERESPONSE

GetPersonaShortRequest = _reflection.GeneratedProtocolMessageType('GetPersonaShortRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPERSONASHORTREQUEST,
  __module__ = 'persona.v2.persona_info_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.persona.v2.GetPersonaShortRequest)
  ))
_sym_db.RegisterMessage(GetPersonaShortRequest)

GetPersonaShortResponse = _reflection.GeneratedProtocolMessageType('GetPersonaShortResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPERSONASHORTRESPONSE,
  __module__ = 'persona.v2.persona_info_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.persona.v2.GetPersonaShortResponse)
  ))
_sym_db.RegisterMessage(GetPersonaShortResponse)

GetPersonaFullRequest = _reflection.GeneratedProtocolMessageType('GetPersonaFullRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPERSONAFULLREQUEST,
  __module__ = 'persona.v2.persona_info_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.persona.v2.GetPersonaFullRequest)
  ))
_sym_db.RegisterMessage(GetPersonaFullRequest)

GetPersonaFullResponse = _reflection.GeneratedProtocolMessageType('GetPersonaFullResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPERSONAFULLRESPONSE,
  __module__ = 'persona.v2.persona_info_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.persona.v2.GetPersonaFullResponse)
  ))
_sym_db.RegisterMessage(GetPersonaFullResponse)

GetPersonaFullByUsernameRequest = _reflection.GeneratedProtocolMessageType('GetPersonaFullByUsernameRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPERSONAFULLBYUSERNAMEREQUEST,
  __module__ = 'persona.v2.persona_info_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.persona.v2.GetPersonaFullByUsernameRequest)
  ))
_sym_db.RegisterMessage(GetPersonaFullByUsernameRequest)

GetPersonaFullByUsernameResponse = _reflection.GeneratedProtocolMessageType('GetPersonaFullByUsernameResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPERSONAFULLBYUSERNAMERESPONSE,
  __module__ = 'persona.v2.persona_info_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.persona.v2.GetPersonaFullByUsernameResponse)
  ))
_sym_db.RegisterMessage(GetPersonaFullByUsernameResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026com.kik.gen.persona.v2ZLgithub.com/kikinteractive/xiphias-api-mobile/generated/go/persona/v2;persona\242\002\022KPBMobilePersonaV2'))
_GETPERSONASHORTREQUEST.fields_by_name['persona_ids'].has_options = True
_GETPERSONASHORTREQUEST.fields_by_name['persona_ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\010\010\001x\001\200\001\200\010'))
_GETPERSONASHORTRESPONSE.fields_by_name['personas'].has_options = True
_GETPERSONASHORTRESPONSE.fields_by_name['personas']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006x\000\200\001\200\010'))
_GETPERSONASHORTRESPONSE.fields_by_name['not_found_ids'].has_options = True
_GETPERSONASHORTRESPONSE.fields_by_name['not_found_ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006x\000\200\001\200\010'))
_GETPERSONASHORTRESPONSE.fields_by_name['failed_ids'].has_options = True
_GETPERSONASHORTRESPONSE.fields_by_name['failed_ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006x\000\200\001\200\010'))
_GETPERSONAFULLREQUEST.fields_by_name['persona_ids'].has_options = True
_GETPERSONAFULLREQUEST.fields_by_name['persona_ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\010\010\001x\001\200\001\200\010'))
_GETPERSONAFULLRESPONSE.fields_by_name['personas'].has_options = True
_GETPERSONAFULLRESPONSE.fields_by_name['personas']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006x\000\200\001\200\010'))
_GETPERSONAFULLRESPONSE.fields_by_name['not_found_ids'].has_options = True
_GETPERSONAFULLRESPONSE.fields_by_name['not_found_ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006x\000\200\001\200\010'))
_GETPERSONAFULLRESPONSE.fields_by_name['failed_ids'].has_options = True
_GETPERSONAFULLRESPONSE.fields_by_name['failed_ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006x\000\200\001\200\010'))
_GETPERSONAFULLBYUSERNAMEREQUEST.fields_by_name['username'].has_options = True
_GETPERSONAFULLBYUSERNAMEREQUEST.fields_by_name['username']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
# @@protoc_insertion_point(module_scope)
