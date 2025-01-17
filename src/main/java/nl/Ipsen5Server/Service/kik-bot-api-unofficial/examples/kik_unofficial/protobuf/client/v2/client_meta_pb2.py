# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client/v2/client_meta.proto

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
from kik_unofficial.protobuf.common.v2 import model_pb2 as common_dot_v2_dot_model__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='client/v2/client_meta.proto',
  package='common.client.v2',
  syntax='proto3',
  serialized_pb=_b('\n\x1b\x63lient/v2/client_meta.proto\x12\x10\x63ommon.client.v2\x1a\x11kik_options.proto\x1a\x19protobuf_validation.proto\x1a\x15\x63ommon/v2/model.proto\"\xb6\x01\n\rDeviceDetails\x12?\n\x0b\x64\x65vice_type\x18\x01 \x01(\x0e\x32*.common.client.v2.DeviceDetails.DeviceType\x12\x36\n\tclient_id\x18\x02 \x01(\x0b\x32\x1b.common.v2.ClientInstanceIdB\x06\xca\x9d%\x02\x08\x01\",\n\nDeviceType\x12\x0b\n\x07\x41NDROID\x10\x00\x12\x07\n\x03IOS\x10\x01\x12\x08\n\x04TEST\x10\x02\"\xa5\x01\n\rClientVersion\x12%\n\x05major\x18\x01 \x01(\rB\x16\xca\x9d%\x12\x39\x01\x00\x00\x00\x00\x00\x00\x00\x41\x00\x00\x00\x80\x00\x00\x00\x00\x12\x1c\n\x05minor\x18\x02 \x01(\rB\r\xca\x9d%\tA\x00\x00\x00\x80\x00\x00\x00\x00\x12\x1d\n\x06\x62ugfix\x18\x03 \x01(\rB\r\xca\x9d%\tA\x00\x00\x00\x80\x00\x00\x00\x00\x12\x15\n\x05\x62uild\x18\x04 \x01(\tB\x06\xca\x9d%\x02\x30\n\x12\x19\n\tdev_build\x18\x05 \x01(\tB\x06\xca\x9d%\x02\x30\n\"Q\n\x0c\x43lientLocale\x12\x41\n\x06locale\x18\x01 \x01(\tB1\xca\x9d%-\x12+^(?i)[a-z]{2,8}(?:_([a-z]{2}|[0-9]{2,3}))?$B\x9e\x01\n\x1c\x63om.kik.gen.common.client.v2B\x10\x43lientModelProtoP\x01ZLgithub.com/kikinteractive/xiphias-model-common/generated/go/client/v2;client\xa0\x01\x01\xa2\x02\x12KPBCCommonClientV2\xaa\xa3*\x02\x08\x01\x62\x06proto3')
  ,
  dependencies=[kik__options__pb2.DESCRIPTOR,protobuf__validation__pb2.DESCRIPTOR,common_dot_v2_dot_model__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DEVICEDETAILS_DEVICETYPE = _descriptor.EnumDescriptor(
  name='DeviceType',
  full_name='common.client.v2.DeviceDetails.DeviceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANDROID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IOS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=257,
  serialized_end=301,
)
_sym_db.RegisterEnumDescriptor(_DEVICEDETAILS_DEVICETYPE)


_DEVICEDETAILS = _descriptor.Descriptor(
  name='DeviceDetails',
  full_name='common.client.v2.DeviceDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_type', full_name='common.client.v2.DeviceDetails.device_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='common.client.v2.DeviceDetails.client_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DEVICEDETAILS_DEVICETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=301,
)


_CLIENTVERSION = _descriptor.Descriptor(
  name='ClientVersion',
  full_name='common.client.v2.ClientVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='major', full_name='common.client.v2.ClientVersion.major', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\0229\001\000\000\000\000\000\000\000A\000\000\000\200\000\000\000\000'))),
    _descriptor.FieldDescriptor(
      name='minor', full_name='common.client.v2.ClientVersion.minor', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\tA\000\000\000\200\000\000\000\000'))),
    _descriptor.FieldDescriptor(
      name='bugfix', full_name='common.client.v2.ClientVersion.bugfix', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\tA\000\000\000\200\000\000\000\000'))),
    _descriptor.FieldDescriptor(
      name='build', full_name='common.client.v2.ClientVersion.build', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\0020\n'))),
    _descriptor.FieldDescriptor(
      name='dev_build', full_name='common.client.v2.ClientVersion.dev_build', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\0020\n'))),
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
  serialized_start=304,
  serialized_end=469,
)


_CLIENTLOCALE = _descriptor.Descriptor(
  name='ClientLocale',
  full_name='common.client.v2.ClientLocale',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='locale', full_name='common.client.v2.ClientLocale.locale', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%-\022+^(?i)[a-z]{2,8}(?:_([a-z]{2}|[0-9]{2,3}))?$'))),
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
  serialized_start=471,
  serialized_end=552,
)

_DEVICEDETAILS.fields_by_name['device_type'].enum_type = _DEVICEDETAILS_DEVICETYPE
_DEVICEDETAILS.fields_by_name['client_id'].message_type = common_dot_v2_dot_model__pb2._CLIENTINSTANCEID
_DEVICEDETAILS_DEVICETYPE.containing_type = _DEVICEDETAILS
DESCRIPTOR.message_types_by_name['DeviceDetails'] = _DEVICEDETAILS
DESCRIPTOR.message_types_by_name['ClientVersion'] = _CLIENTVERSION
DESCRIPTOR.message_types_by_name['ClientLocale'] = _CLIENTLOCALE

DeviceDetails = _reflection.GeneratedProtocolMessageType('DeviceDetails', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEDETAILS,
  __module__ = 'client.v2.client_meta_pb2'
  # @@protoc_insertion_point(class_scope:common.client.v2.DeviceDetails)
  ))
_sym_db.RegisterMessage(DeviceDetails)

ClientVersion = _reflection.GeneratedProtocolMessageType('ClientVersion', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTVERSION,
  __module__ = 'client.v2.client_meta_pb2'
  # @@protoc_insertion_point(class_scope:common.client.v2.ClientVersion)
  ))
_sym_db.RegisterMessage(ClientVersion)

ClientLocale = _reflection.GeneratedProtocolMessageType('ClientLocale', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTLOCALE,
  __module__ = 'client.v2.client_meta_pb2'
  # @@protoc_insertion_point(class_scope:common.client.v2.ClientLocale)
  ))
_sym_db.RegisterMessage(ClientLocale)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034com.kik.gen.common.client.v2B\020ClientModelProtoP\001ZLgithub.com/kikinteractive/xiphias-model-common/generated/go/client/v2;client\240\001\001\242\002\022KPBCCommonClientV2\252\243*\002\010\001'))
_DEVICEDETAILS.fields_by_name['client_id'].has_options = True
_DEVICEDETAILS.fields_by_name['client_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_CLIENTVERSION.fields_by_name['major'].has_options = True
_CLIENTVERSION.fields_by_name['major']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\0229\001\000\000\000\000\000\000\000A\000\000\000\200\000\000\000\000'))
_CLIENTVERSION.fields_by_name['minor'].has_options = True
_CLIENTVERSION.fields_by_name['minor']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\tA\000\000\000\200\000\000\000\000'))
_CLIENTVERSION.fields_by_name['bugfix'].has_options = True
_CLIENTVERSION.fields_by_name['bugfix']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\tA\000\000\000\200\000\000\000\000'))
_CLIENTVERSION.fields_by_name['build'].has_options = True
_CLIENTVERSION.fields_by_name['build']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\0020\n'))
_CLIENTVERSION.fields_by_name['dev_build'].has_options = True
_CLIENTVERSION.fields_by_name['dev_build']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\0020\n'))
_CLIENTLOCALE.fields_by_name['locale'].has_options = True
_CLIENTLOCALE.fields_by_name['locale']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%-\022+^(?i)[a-z]{2,8}(?:_([a-z]{2}|[0-9]{2,3}))?$'))
# @@protoc_insertion_point(module_scope)
