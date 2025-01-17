# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: groups/v1/group_search_service.proto

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
from kik_unofficial.protobuf.groups.v1 import groups_common_pb2 as groups_dot_v1_dot_groups__common__pb2
from kik_unofficial.protobuf.google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='groups/v1/group_search_service.proto',
  package='mobile.groups.v1',
  syntax='proto3',
  serialized_pb=_b('\n$groups/v1/group_search_service.proto\x12\x10mobile.groups.v1\x1a\x12\x63ommon_model.proto\x1a\x19protobuf_validation.proto\x1a\x1dgroups/v1/groups_common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"2\n\x14PublicGroupJoinToken\x12\x1a\n\x05token\x18\x01 \x01(\x0c\x42\x0b\xca\x9d%\x07\x08\x01(\x01\x30\x80(\"\x1c\n\x1aGetGroupSuggestionsRequest\"\xd5\x01\n\x1bGetGroupSuggestionsResponse\x12\x44\n\x06result\x18\x01 \x01(\x0e\x32\x34.mobile.groups.v1.GetGroupSuggestionsResponse.Result\x12\x45\n\nsuggestion\x18\x02 \x03(\x0b\x32%.mobile.groups.v1.LimitedGroupDetailsB\n\xca\x9d%\x06\x08\x00\x80\x01\x80\x08\")\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x17\n\x13RATE_LIMIT_EXCEEDED\x10\x01\"A\n\x11\x46indGroupsRequest\x12,\n\x05query\x18\x01 \x01(\tB\x1d\xca\x9d%\x19\x08\x01\x12\x15^[A-Za-z0-9._]{1,32}$\"\xe0\x01\n\x12\x46indGroupsResponse\x12;\n\x06result\x18\x01 \x01(\x0e\x32+.mobile.groups.v1.FindGroupsResponse.Result\x12?\n\x05match\x18\x02 \x03(\x0b\x32%.mobile.groups.v1.LimitedGroupDetailsB\t\xca\x9d%\x05\x08\x00\x80\x01\x19\x12!\n\x19is_available_for_creation\x18\x03 \x01(\x08\")\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x17\n\x13RATE_LIMIT_EXCEEDED\x10\x01\"\xc8\x02\n\x13LimitedGroupDetails\x12\'\n\x03jid\x18\x01 \x01(\x0b\x32\x12.common.XiGroupJidB\x06\xca\x9d%\x02\x08\x00\x12@\n\x0c\x64isplay_data\x18\x02 \x01(\x0b\x32\".common.groups.v1.GroupDisplayDataB\x06\xca\x9d%\x02\x08\x00\x12\x14\n\x0cmember_count\x18\x03 \x01(\r\x12>\n\x12last_activity_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x06\xca\x9d%\x02\x08\x00\x12\x16\n\x0emax_group_size\x18\x05 \x01(\r\x12\x16\n\x0e\x61\x63tive_members\x18\x06 \x01(\r\x12@\n\x10group_join_token\x18\x64 \x01(\x0b\x32&.mobile.groups.v1.PublicGroupJoinToken2\xde\x01\n\x0bGroupSearch\x12Y\n\nFindGroups\x12#.mobile.groups.v1.FindGroupsRequest\x1a$.mobile.groups.v1.FindGroupsResponse\"\x00\x12t\n\x13GetGroupSuggestions\x12,.mobile.groups.v1.GetGroupSuggestionsRequest\x1a-.mobile.groups.v1.GetGroupSuggestionsResponse\"\x00\x42\\\n\x0e\x63om.kik.groupsZJgithub.com/kikinteractive/xiphias-api-mobile/generated/go/groups/v1;groupsb\x06proto3')
  ,
  dependencies=[common__model__pb2.DESCRIPTOR,protobuf__validation__pb2.DESCRIPTOR,groups_dot_v1_dot_groups__common__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETGROUPSUGGESTIONSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.groups.v1.GetGroupSuggestionsResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATE_LIMIT_EXCEEDED', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=424,
  serialized_end=465,
)
_sym_db.RegisterEnumDescriptor(_GETGROUPSUGGESTIONSRESPONSE_RESULT)

_FINDGROUPSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.groups.v1.FindGroupsResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATE_LIMIT_EXCEEDED', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=424,
  serialized_end=465,
)
_sym_db.RegisterEnumDescriptor(_FINDGROUPSRESPONSE_RESULT)


_PUBLICGROUPJOINTOKEN = _descriptor.Descriptor(
  name='PublicGroupJoinToken',
  full_name='mobile.groups.v1.PublicGroupJoinToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='mobile.groups.v1.PublicGroupJoinToken.token', index=0,
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
  serialized_start=169,
  serialized_end=219,
)


_GETGROUPSUGGESTIONSREQUEST = _descriptor.Descriptor(
  name='GetGroupSuggestionsRequest',
  full_name='mobile.groups.v1.GetGroupSuggestionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=221,
  serialized_end=249,
)


_GETGROUPSUGGESTIONSRESPONSE = _descriptor.Descriptor(
  name='GetGroupSuggestionsResponse',
  full_name='mobile.groups.v1.GetGroupSuggestionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.groups.v1.GetGroupSuggestionsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='suggestion', full_name='mobile.groups.v1.GetGroupSuggestionsResponse.suggestion', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006\010\000\200\001\200\010'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETGROUPSUGGESTIONSRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=465,
)


_FINDGROUPSREQUEST = _descriptor.Descriptor(
  name='FindGroupsRequest',
  full_name='mobile.groups.v1.FindGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='mobile.groups.v1.FindGroupsRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\031\010\001\022\025^[A-Za-z0-9._]{1,32}$'))),
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
  serialized_start=467,
  serialized_end=532,
)


_FINDGROUPSRESPONSE = _descriptor.Descriptor(
  name='FindGroupsResponse',
  full_name='mobile.groups.v1.FindGroupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.groups.v1.FindGroupsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match', full_name='mobile.groups.v1.FindGroupsResponse.match', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\000\200\001\031'))),
    _descriptor.FieldDescriptor(
      name='is_available_for_creation', full_name='mobile.groups.v1.FindGroupsResponse.is_available_for_creation', index=2,
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
    _FINDGROUPSRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=535,
  serialized_end=759,
)


_LIMITEDGROUPDETAILS = _descriptor.Descriptor(
  name='LimitedGroupDetails',
  full_name='mobile.groups.v1.LimitedGroupDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jid', full_name='mobile.groups.v1.LimitedGroupDetails.jid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\000'))),
    _descriptor.FieldDescriptor(
      name='display_data', full_name='mobile.groups.v1.LimitedGroupDetails.display_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\000'))),
    _descriptor.FieldDescriptor(
      name='member_count', full_name='mobile.groups.v1.LimitedGroupDetails.member_count', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_activity_time', full_name='mobile.groups.v1.LimitedGroupDetails.last_activity_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\000'))),
    _descriptor.FieldDescriptor(
      name='max_group_size', full_name='mobile.groups.v1.LimitedGroupDetails.max_group_size', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_members', full_name='mobile.groups.v1.LimitedGroupDetails.active_members', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_join_token', full_name='mobile.groups.v1.LimitedGroupDetails.group_join_token', index=6,
      number=100, type=11, cpp_type=10, label=1,
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
  serialized_start=762,
  serialized_end=1090,
)

_GETGROUPSUGGESTIONSRESPONSE.fields_by_name['result'].enum_type = _GETGROUPSUGGESTIONSRESPONSE_RESULT
_GETGROUPSUGGESTIONSRESPONSE.fields_by_name['suggestion'].message_type = _LIMITEDGROUPDETAILS
_GETGROUPSUGGESTIONSRESPONSE_RESULT.containing_type = _GETGROUPSUGGESTIONSRESPONSE
_FINDGROUPSRESPONSE.fields_by_name['result'].enum_type = _FINDGROUPSRESPONSE_RESULT
_FINDGROUPSRESPONSE.fields_by_name['match'].message_type = _LIMITEDGROUPDETAILS
_FINDGROUPSRESPONSE_RESULT.containing_type = _FINDGROUPSRESPONSE
_LIMITEDGROUPDETAILS.fields_by_name['jid'].message_type = common__model__pb2._XIGROUPJID
_LIMITEDGROUPDETAILS.fields_by_name['display_data'].message_type = groups_dot_v1_dot_groups__common__pb2._GROUPDISPLAYDATA
_LIMITEDGROUPDETAILS.fields_by_name['last_activity_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LIMITEDGROUPDETAILS.fields_by_name['group_join_token'].message_type = _PUBLICGROUPJOINTOKEN
DESCRIPTOR.message_types_by_name['PublicGroupJoinToken'] = _PUBLICGROUPJOINTOKEN
DESCRIPTOR.message_types_by_name['GetGroupSuggestionsRequest'] = _GETGROUPSUGGESTIONSREQUEST
DESCRIPTOR.message_types_by_name['GetGroupSuggestionsResponse'] = _GETGROUPSUGGESTIONSRESPONSE
DESCRIPTOR.message_types_by_name['FindGroupsRequest'] = _FINDGROUPSREQUEST
DESCRIPTOR.message_types_by_name['FindGroupsResponse'] = _FINDGROUPSRESPONSE
DESCRIPTOR.message_types_by_name['LimitedGroupDetails'] = _LIMITEDGROUPDETAILS

PublicGroupJoinToken = _reflection.GeneratedProtocolMessageType('PublicGroupJoinToken', (_message.Message,), dict(
  DESCRIPTOR = _PUBLICGROUPJOINTOKEN,
  __module__ = 'groups.v1.group_search_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.groups.v1.PublicGroupJoinToken)
  ))
_sym_db.RegisterMessage(PublicGroupJoinToken)

GetGroupSuggestionsRequest = _reflection.GeneratedProtocolMessageType('GetGroupSuggestionsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETGROUPSUGGESTIONSREQUEST,
  __module__ = 'groups.v1.group_search_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.groups.v1.GetGroupSuggestionsRequest)
  ))
_sym_db.RegisterMessage(GetGroupSuggestionsRequest)

GetGroupSuggestionsResponse = _reflection.GeneratedProtocolMessageType('GetGroupSuggestionsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETGROUPSUGGESTIONSRESPONSE,
  __module__ = 'groups.v1.group_search_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.groups.v1.GetGroupSuggestionsResponse)
  ))
_sym_db.RegisterMessage(GetGroupSuggestionsResponse)

FindGroupsRequest = _reflection.GeneratedProtocolMessageType('FindGroupsRequest', (_message.Message,), dict(
  DESCRIPTOR = _FINDGROUPSREQUEST,
  __module__ = 'groups.v1.group_search_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.groups.v1.FindGroupsRequest)
  ))
_sym_db.RegisterMessage(FindGroupsRequest)

FindGroupsResponse = _reflection.GeneratedProtocolMessageType('FindGroupsResponse', (_message.Message,), dict(
  DESCRIPTOR = _FINDGROUPSRESPONSE,
  __module__ = 'groups.v1.group_search_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.groups.v1.FindGroupsResponse)
  ))
_sym_db.RegisterMessage(FindGroupsResponse)

LimitedGroupDetails = _reflection.GeneratedProtocolMessageType('LimitedGroupDetails', (_message.Message,), dict(
  DESCRIPTOR = _LIMITEDGROUPDETAILS,
  __module__ = 'groups.v1.group_search_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.groups.v1.LimitedGroupDetails)
  ))
_sym_db.RegisterMessage(LimitedGroupDetails)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\016com.kik.groupsZJgithub.com/kikinteractive/xiphias-api-mobile/generated/go/groups/v1;groups'))
_PUBLICGROUPJOINTOKEN.fields_by_name['token'].has_options = True
_PUBLICGROUPJOINTOKEN.fields_by_name['token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001(\0010\200('))
_GETGROUPSUGGESTIONSRESPONSE.fields_by_name['suggestion'].has_options = True
_GETGROUPSUGGESTIONSRESPONSE.fields_by_name['suggestion']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\006\010\000\200\001\200\010'))
_FINDGROUPSREQUEST.fields_by_name['query'].has_options = True
_FINDGROUPSREQUEST.fields_by_name['query']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\031\010\001\022\025^[A-Za-z0-9._]{1,32}$'))
_FINDGROUPSRESPONSE.fields_by_name['match'].has_options = True
_FINDGROUPSRESPONSE.fields_by_name['match']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005\010\000\200\001\031'))
_LIMITEDGROUPDETAILS.fields_by_name['jid'].has_options = True
_LIMITEDGROUPDETAILS.fields_by_name['jid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\000'))
_LIMITEDGROUPDETAILS.fields_by_name['display_data'].has_options = True
_LIMITEDGROUPDETAILS.fields_by_name['display_data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\000'))
_LIMITEDGROUPDETAILS.fields_by_name['last_activity_time'].has_options = True
_LIMITEDGROUPDETAILS.fields_by_name['last_activity_time']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\000'))
# @@protoc_insertion_point(module_scope)
