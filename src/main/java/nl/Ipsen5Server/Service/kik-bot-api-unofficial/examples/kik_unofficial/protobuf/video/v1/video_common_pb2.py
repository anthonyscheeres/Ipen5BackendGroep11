# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: video/v1/video_common.proto

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
from kik_unofficial.protobuf.google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='video/v1/video_common.proto',
  package='common.video.v1',
  syntax='proto3',
  serialized_pb=_b('\n\x1bvideo/v1/video_common.proto\x12\x0f\x63ommon.video.v1\x1a\x12\x63ommon_model.proto\x1a\x19protobuf_validation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"n\n\x07\x43onvoId\x12\x36\n\none_to_one\x18\x01 \x01(\x0b\x32 .common.video.v1.OneToOneConvoIdH\x00\x12#\n\x05group\x18\x02 \x01(\x0b\x32\x12.common.XiGroupJidH\x00\x42\x06\n\x04kind\"G\n\x0fOneToOneConvoId\x12\x34\n\x05users\x18\x01 \x03(\x0b\x32\x15.common.XiBareUserJidB\x0e\xca\x9d%\n\x08\x01x\x02\x80\x01\x02\x88\x01\x00\"\xfb\x02\n\x0f\x43onvoVideoState\x12\x32\n\x08\x63onvo_id\x18\x01 \x01(\x0b\x32\x18.common.video.v1.ConvoIdB\x06\xca\x9d%\x02\x08\x01\x12L\n\x0buser_states\x18\x02 \x03(\x0b\x32*.common.video.v1.ConvoVideoState.UserStateB\x0b\xca\x9d%\x07\x08\x00x\x00\x80\x01\x64\x12\x35\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x06\xca\x9d%\x02\x08\x01\x1a\xae\x01\n\tUserState\x12+\n\x04user\x18\x01 \x01(\x0b\x32\x15.common.XiBareUserJidB\x06\xca\x9d%\x02\x08\x01\x12?\n\x05state\x18\x02 \x01(\x0e\x32\x30.common.video.v1.ConvoVideoState.UserState.State\"3\n\x05State\x12\x0b\n\x07NOT_SET\x10\x00\x12\x0e\n\nCONNECTING\x10\x05\x12\r\n\tCONNECTED\x10\n\"b\n\x18\x43onferenceConnectionInfo\x12\x17\n\x04host\x18\x01 \x01(\tB\t\xca\x9d%\x05\x08\x01\x30\x80\x08\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x1f\n\rconference_id\x18\x03 \x01(\tB\x08\xca\x9d%\x04\x08\x01\x30 \":\n\x1aMediaServerConnectionToken\x12\x1c\n\x07payload\x18\x01 \x01(\x0c\x42\x0b\xca\x9d%\x07\x08\x01(\x01\x30\x80(B[\n\rcom.kik.videoZJgithub.com/kikinteractive/xiphias-model-common/generated/go/video/v1;videob\x06proto3')
  ,
  dependencies=[common__model__pb2.DESCRIPTOR,protobuf__validation__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CONVOVIDEOSTATE_USERSTATE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='common.video.v1.ConvoVideoState.UserState.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_SET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECTING', index=1, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECTED', index=2, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=642,
  serialized_end=693,
)
_sym_db.RegisterEnumDescriptor(_CONVOVIDEOSTATE_USERSTATE_STATE)


_CONVOID = _descriptor.Descriptor(
  name='ConvoId',
  full_name='common.video.v1.ConvoId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='one_to_one', full_name='common.video.v1.ConvoId.one_to_one', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='common.video.v1.ConvoId.group', index=1,
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
      name='kind', full_name='common.video.v1.ConvoId.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=128,
  serialized_end=238,
)


_ONETOONECONVOID = _descriptor.Descriptor(
  name='OneToOneConvoId',
  full_name='common.video.v1.OneToOneConvoId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='common.video.v1.OneToOneConvoId.users', index=0,
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
  serialized_start=240,
  serialized_end=311,
)


_CONVOVIDEOSTATE_USERSTATE = _descriptor.Descriptor(
  name='UserState',
  full_name='common.video.v1.ConvoVideoState.UserState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='common.video.v1.ConvoVideoState.UserState.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='state', full_name='common.video.v1.ConvoVideoState.UserState.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONVOVIDEOSTATE_USERSTATE_STATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=519,
  serialized_end=693,
)

_CONVOVIDEOSTATE = _descriptor.Descriptor(
  name='ConvoVideoState',
  full_name='common.video.v1.ConvoVideoState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='convo_id', full_name='common.video.v1.ConvoVideoState.convo_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='user_states', full_name='common.video.v1.ConvoVideoState.user_states', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\000x\000\200\001d'))),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='common.video.v1.ConvoVideoState.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
  ],
  extensions=[
  ],
  nested_types=[_CONVOVIDEOSTATE_USERSTATE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=693,
)


_CONFERENCECONNECTIONINFO = _descriptor.Descriptor(
  name='ConferenceConnectionInfo',
  full_name='common.video.v1.ConferenceConnectionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='common.video.v1.ConferenceConnectionInfo.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\0010\200\010'))),
    _descriptor.FieldDescriptor(
      name='port', full_name='common.video.v1.ConferenceConnectionInfo.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conference_id', full_name='common.video.v1.ConferenceConnectionInfo.conference_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\004\010\0010 '))),
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
  serialized_start=695,
  serialized_end=793,
)


_MEDIASERVERCONNECTIONTOKEN = _descriptor.Descriptor(
  name='MediaServerConnectionToken',
  full_name='common.video.v1.MediaServerConnectionToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='common.video.v1.MediaServerConnectionToken.payload', index=0,
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
  serialized_start=795,
  serialized_end=853,
)

_CONVOID.fields_by_name['one_to_one'].message_type = _ONETOONECONVOID
_CONVOID.fields_by_name['group'].message_type = common__model__pb2._XIGROUPJID
_CONVOID.oneofs_by_name['kind'].fields.append(
  _CONVOID.fields_by_name['one_to_one'])
_CONVOID.fields_by_name['one_to_one'].containing_oneof = _CONVOID.oneofs_by_name['kind']
_CONVOID.oneofs_by_name['kind'].fields.append(
  _CONVOID.fields_by_name['group'])
_CONVOID.fields_by_name['group'].containing_oneof = _CONVOID.oneofs_by_name['kind']
_ONETOONECONVOID.fields_by_name['users'].message_type = common__model__pb2._XIBAREUSERJID
_CONVOVIDEOSTATE_USERSTATE.fields_by_name['user'].message_type = common__model__pb2._XIBAREUSERJID
_CONVOVIDEOSTATE_USERSTATE.fields_by_name['state'].enum_type = _CONVOVIDEOSTATE_USERSTATE_STATE
_CONVOVIDEOSTATE_USERSTATE.containing_type = _CONVOVIDEOSTATE
_CONVOVIDEOSTATE_USERSTATE_STATE.containing_type = _CONVOVIDEOSTATE_USERSTATE
_CONVOVIDEOSTATE.fields_by_name['convo_id'].message_type = _CONVOID
_CONVOVIDEOSTATE.fields_by_name['user_states'].message_type = _CONVOVIDEOSTATE_USERSTATE
_CONVOVIDEOSTATE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['ConvoId'] = _CONVOID
DESCRIPTOR.message_types_by_name['OneToOneConvoId'] = _ONETOONECONVOID
DESCRIPTOR.message_types_by_name['ConvoVideoState'] = _CONVOVIDEOSTATE
DESCRIPTOR.message_types_by_name['ConferenceConnectionInfo'] = _CONFERENCECONNECTIONINFO
DESCRIPTOR.message_types_by_name['MediaServerConnectionToken'] = _MEDIASERVERCONNECTIONTOKEN

ConvoId = _reflection.GeneratedProtocolMessageType('ConvoId', (_message.Message,), dict(
  DESCRIPTOR = _CONVOID,
  __module__ = 'video.v1.video_common_pb2'
  # @@protoc_insertion_point(class_scope:common.video.v1.ConvoId)
  ))
_sym_db.RegisterMessage(ConvoId)

OneToOneConvoId = _reflection.GeneratedProtocolMessageType('OneToOneConvoId', (_message.Message,), dict(
  DESCRIPTOR = _ONETOONECONVOID,
  __module__ = 'video.v1.video_common_pb2'
  # @@protoc_insertion_point(class_scope:common.video.v1.OneToOneConvoId)
  ))
_sym_db.RegisterMessage(OneToOneConvoId)

ConvoVideoState = _reflection.GeneratedProtocolMessageType('ConvoVideoState', (_message.Message,), dict(

  UserState = _reflection.GeneratedProtocolMessageType('UserState', (_message.Message,), dict(
    DESCRIPTOR = _CONVOVIDEOSTATE_USERSTATE,
    __module__ = 'video.v1.video_common_pb2'
    # @@protoc_insertion_point(class_scope:common.video.v1.ConvoVideoState.UserState)
    ))
  ,
  DESCRIPTOR = _CONVOVIDEOSTATE,
  __module__ = 'video.v1.video_common_pb2'
  # @@protoc_insertion_point(class_scope:common.video.v1.ConvoVideoState)
  ))
_sym_db.RegisterMessage(ConvoVideoState)
_sym_db.RegisterMessage(ConvoVideoState.UserState)

ConferenceConnectionInfo = _reflection.GeneratedProtocolMessageType('ConferenceConnectionInfo', (_message.Message,), dict(
  DESCRIPTOR = _CONFERENCECONNECTIONINFO,
  __module__ = 'video.v1.video_common_pb2'
  # @@protoc_insertion_point(class_scope:common.video.v1.ConferenceConnectionInfo)
  ))
_sym_db.RegisterMessage(ConferenceConnectionInfo)

MediaServerConnectionToken = _reflection.GeneratedProtocolMessageType('MediaServerConnectionToken', (_message.Message,), dict(
  DESCRIPTOR = _MEDIASERVERCONNECTIONTOKEN,
  __module__ = 'video.v1.video_common_pb2'
  # @@protoc_insertion_point(class_scope:common.video.v1.MediaServerConnectionToken)
  ))
_sym_db.RegisterMessage(MediaServerConnectionToken)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\rcom.kik.videoZJgithub.com/kikinteractive/xiphias-model-common/generated/go/video/v1;video'))
_ONETOONECONVOID.fields_by_name['users'].has_options = True
_ONETOONECONVOID.fields_by_name['users']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\n\010\001x\002\200\001\002\210\001\000'))
_CONVOVIDEOSTATE_USERSTATE.fields_by_name['user'].has_options = True
_CONVOVIDEOSTATE_USERSTATE.fields_by_name['user']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_CONVOVIDEOSTATE.fields_by_name['convo_id'].has_options = True
_CONVOVIDEOSTATE.fields_by_name['convo_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_CONVOVIDEOSTATE.fields_by_name['user_states'].has_options = True
_CONVOVIDEOSTATE.fields_by_name['user_states']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\000x\000\200\001d'))
_CONVOVIDEOSTATE.fields_by_name['timestamp'].has_options = True
_CONVOVIDEOSTATE.fields_by_name['timestamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_CONFERENCECONNECTIONINFO.fields_by_name['host'].has_options = True
_CONFERENCECONNECTIONINFO.fields_by_name['host']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\0010\200\010'))
_CONFERENCECONNECTIONINFO.fields_by_name['conference_id'].has_options = True
_CONFERENCECONNECTIONINFO.fields_by_name['conference_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\004\010\0010 '))
_MEDIASERVERCONNECTIONTOKEN.fields_by_name['payload'].has_options = True
_MEDIASERVERCONNECTIONTOKEN.fields_by_name['payload']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001(\0010\200('))
# @@protoc_insertion_point(module_scope)
