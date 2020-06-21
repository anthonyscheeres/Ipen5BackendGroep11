# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: matching/v1/anon_matching_service.proto

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
from kik_unofficial.protobuf.google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import kik_unofficial.protobuf.common_model_pb2 as common__model__pb2
from kik_unofficial.protobuf.common.v1 import model_pb2 as common_dot_v1_dot_model__pb2
from kik_unofficial.protobuf.matching.v1 import matching_common_pb2 as matching_dot_v1_dot_matching__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='matching/v1/anon_matching_service.proto',
  package='mobile.matching.v1',
  syntax='proto3',
  serialized_pb=_b('\n\'matching/v1/anon_matching_service.proto\x12\x12mobile.matching.v1\x1a\x19protobuf_validation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x12\x63ommon_model.proto\x1a\x15\x63ommon/v1/model.proto\x1a!matching/v1/matching_common.proto\"p\n\x16\x46indChatPartnerRequest\x12<\n\tinterests\x18\x01 \x03(\x0b\x32 .mobile.matching.v1.ChatInterestB\x07\xca\x9d%\x03\x80\x01\x05\x12\x18\n\x10matching_variant\x18\x02 \x01(\t\"\x80\x03\n\x17\x46indChatPartnerResponse\x12\x42\n\x06result\x18\x01 \x01(\x0e\x32\x32.mobile.matching.v1.FindChatPartnerResponse.Result\x12,\n\x14\x66ind_chat_request_id\x18\x02 \x01(\x0b\x32\x0e.common.XiUuid\x12;\n\x0fsession_details\x18\x03 \x01(\x0b\x32\".mobile.matching.v1.SessionDetails\x12\x38\n\x14rejected_expiry_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"|\n\x06Result\x12\x11\n\rPARTNER_FOUND\x10\x00\x12\x0c\n\x08IN_QUEUE\x10\x01\x12\x0c\n\x08REJECTED\x10\x02\x12\"\n\x1eREJECTED_NO_REMAINING_SESSIONS\x10\x03\x12\x1f\n\x1bREJECTED_TEMPORARILY_BANNED\x10\x04\"T\n\x1c\x43\x61ncelFindChatPartnerRequest\x12\x34\n\x14\x66ind_chat_request_id\x18\x01 \x01(\x0b\x32\x0e.common.XiUuidB\x06\xca\x9d%\x02\x08\x01\"\x98\x01\n\x1d\x43\x61ncelFindChatPartnerResponse\x12H\n\x06result\x18\x01 \x01(\x0e\x32\x38.mobile.matching.v1.CancelFindChatPartnerResponse.Result\"-\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x1b\n\x17SESSION_ALREADY_CREATED\x10\x01\"`\n\x15GetChatSessionRequest\x12G\n\x0bsession_key\x18\x01 \x01(\x0b\x32*.common.matching.v1.AnonMatchingSessionKeyB\x06\xca\x9d%\x02\x08\x01\"\xb9\x01\n\x16GetChatSessionResponse\x12\x41\n\x06result\x18\x01 \x01(\x0e\x32\x31.mobile.matching.v1.GetChatSessionResponse.Result\x12;\n\x0fsession_details\x18\x02 \x01(\x0b\x32\".mobile.matching.v1.SessionDetails\"\x1f\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\r\n\tNOT_FOUND\x10\x01\"`\n\x15\x45ndChatSessionRequest\x12G\n\x0bsession_key\x18\x01 \x01(\x0b\x32*.common.matching.v1.AnonMatchingSessionKeyB\x06\xca\x9d%\x02\x08\x01\"m\n\x16\x45ndChatSessionResponse\x12\x41\n\x06result\x18\x01 \x01(\x0e\x32\x31.mobile.matching.v1.EndChatSessionResponse.Result\"\x10\n\x06Result\x12\x06\n\x02OK\x10\x00\"\x1e\n\x1cGetRemainingAnonChatsRequest\"\x94\x01\n\x1dGetRemainingAnonChatsResponse\x12H\n\x06result\x18\x01 \x01(\x0e\x32\x38.mobile.matching.v1.GetRemainingAnonChatsResponse.Result\x12\x17\n\x0fremaining_chats\x18\x02 \x01(\x05\"\x10\n\x06Result\x12\x06\n\x02OK\x10\x00\"T\n\x0c\x43hatInterest\x12 \n\x0binterest_id\x18\x01 \x01(\tB\x0b\xca\x9d%\x07\x08\x01(\x01\x30\xff\x01\x12\"\n\rinterest_name\x18\x02 \x01(\tB\x0b\xca\x9d%\x07\x08\x01(\x01\x30\xff\x01\"\xa3\x02\n\x0eSessionDetails\x12*\n\nsession_id\x18\x01 \x01(\x0b\x32\x0e.common.XiUuidB\x06\xca\x9d%\x02\x08\x01\x12\x39\n\x12\x63hat_partner_alias\x18\x03 \x01(\x0b\x32\x15.common.v1.XiAliasJidB\x06\xca\x9d%\x02\x08\x01\x12\x34\n\x10session_end_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x13session_expiry_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12;\n\rsession_state\x18\x06 \x01(\x0e\x32$.common.matching.v1.ChatSessionState2\xc8\x04\n\x0c\x41nonMatching\x12j\n\x0f\x46indChatPartner\x12*.mobile.matching.v1.FindChatPartnerRequest\x1a+.mobile.matching.v1.FindChatPartnerResponse\x12|\n\x15\x43\x61ncelFindChatPartner\x12\x30.mobile.matching.v1.CancelFindChatPartnerRequest\x1a\x31.mobile.matching.v1.CancelFindChatPartnerResponse\x12g\n\x0e\x45ndChatSession\x12).mobile.matching.v1.EndChatSessionRequest\x1a*.mobile.matching.v1.EndChatSessionResponse\x12g\n\x0eGetChatSession\x12).mobile.matching.v1.GetChatSessionRequest\x1a*.mobile.matching.v1.GetChatSessionResponse\x12|\n\x15GetRemainingAnonChats\x12\x30.mobile.matching.v1.GetRemainingAnonChatsRequest\x1a\x31.mobile.matching.v1.GetRemainingAnonChatsResponseBf\n\x14\x63om.kik.matching.rpcZNgithub.com/kikinteractive/xiphias-api-mobile/generated/go/matching/v1;matchingb\x06proto3')
  ,
  dependencies=[protobuf__validation__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,common__model__pb2.DESCRIPTOR,common_dot_v1_dot_model__pb2.DESCRIPTOR,matching_dot_v1_dot_matching__common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_FINDCHATPARTNERRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.matching.v1.FindChatPartnerResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PARTNER_FOUND', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_QUEUE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECTED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECTED_NO_REMAINING_SESSIONS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECTED_TEMPORARILY_BANNED', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=576,
  serialized_end=700,
)
_sym_db.RegisterEnumDescriptor(_FINDCHATPARTNERRESPONSE_RESULT)

_CANCELFINDCHATPARTNERRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.matching.v1.CancelFindChatPartnerResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_ALREADY_CREATED', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=896,
  serialized_end=941,
)
_sym_db.RegisterEnumDescriptor(_CANCELFINDCHATPARTNERRESPONSE_RESULT)

_GETCHATSESSIONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.matching.v1.GetChatSessionResponse.Result',
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
  serialized_start=1196,
  serialized_end=1227,
)
_sym_db.RegisterEnumDescriptor(_GETCHATSESSIONRESPONSE_RESULT)

_ENDCHATSESSIONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.matching.v1.EndChatSessionResponse.Result',
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
  serialized_start=896,
  serialized_end=912,
)
_sym_db.RegisterEnumDescriptor(_ENDCHATSESSIONRESPONSE_RESULT)

_GETREMAININGANONCHATSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.matching.v1.GetRemainingAnonChatsResponse.Result',
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
  serialized_start=896,
  serialized_end=912,
)
_sym_db.RegisterEnumDescriptor(_GETREMAININGANONCHATSRESPONSE_RESULT)


_FINDCHATPARTNERREQUEST = _descriptor.Descriptor(
  name='FindChatPartnerRequest',
  full_name='mobile.matching.v1.FindChatPartnerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interests', full_name='mobile.matching.v1.FindChatPartnerRequest.interests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\003\200\001\005'))),
    _descriptor.FieldDescriptor(
      name='matching_variant', full_name='mobile.matching.v1.FindChatPartnerRequest.matching_variant', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=201,
  serialized_end=313,
)


_FINDCHATPARTNERRESPONSE = _descriptor.Descriptor(
  name='FindChatPartnerResponse',
  full_name='mobile.matching.v1.FindChatPartnerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.matching.v1.FindChatPartnerResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='find_chat_request_id', full_name='mobile.matching.v1.FindChatPartnerResponse.find_chat_request_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session_details', full_name='mobile.matching.v1.FindChatPartnerResponse.session_details', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rejected_expiry_time', full_name='mobile.matching.v1.FindChatPartnerResponse.rejected_expiry_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FINDCHATPARTNERRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=700,
)


_CANCELFINDCHATPARTNERREQUEST = _descriptor.Descriptor(
  name='CancelFindChatPartnerRequest',
  full_name='mobile.matching.v1.CancelFindChatPartnerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='find_chat_request_id', full_name='mobile.matching.v1.CancelFindChatPartnerRequest.find_chat_request_id', index=0,
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
  serialized_start=702,
  serialized_end=786,
)


_CANCELFINDCHATPARTNERRESPONSE = _descriptor.Descriptor(
  name='CancelFindChatPartnerResponse',
  full_name='mobile.matching.v1.CancelFindChatPartnerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.matching.v1.CancelFindChatPartnerResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CANCELFINDCHATPARTNERRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=789,
  serialized_end=941,
)


_GETCHATSESSIONREQUEST = _descriptor.Descriptor(
  name='GetChatSessionRequest',
  full_name='mobile.matching.v1.GetChatSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_key', full_name='mobile.matching.v1.GetChatSessionRequest.session_key', index=0,
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
  serialized_start=943,
  serialized_end=1039,
)


_GETCHATSESSIONRESPONSE = _descriptor.Descriptor(
  name='GetChatSessionResponse',
  full_name='mobile.matching.v1.GetChatSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.matching.v1.GetChatSessionResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session_details', full_name='mobile.matching.v1.GetChatSessionResponse.session_details', index=1,
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
    _GETCHATSESSIONRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1042,
  serialized_end=1227,
)


_ENDCHATSESSIONREQUEST = _descriptor.Descriptor(
  name='EndChatSessionRequest',
  full_name='mobile.matching.v1.EndChatSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_key', full_name='mobile.matching.v1.EndChatSessionRequest.session_key', index=0,
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
  serialized_start=1229,
  serialized_end=1325,
)


_ENDCHATSESSIONRESPONSE = _descriptor.Descriptor(
  name='EndChatSessionResponse',
  full_name='mobile.matching.v1.EndChatSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.matching.v1.EndChatSessionResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENDCHATSESSIONRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1327,
  serialized_end=1436,
)


_GETREMAININGANONCHATSREQUEST = _descriptor.Descriptor(
  name='GetRemainingAnonChatsRequest',
  full_name='mobile.matching.v1.GetRemainingAnonChatsRequest',
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
  serialized_start=1438,
  serialized_end=1468,
)


_GETREMAININGANONCHATSRESPONSE = _descriptor.Descriptor(
  name='GetRemainingAnonChatsResponse',
  full_name='mobile.matching.v1.GetRemainingAnonChatsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.matching.v1.GetRemainingAnonChatsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remaining_chats', full_name='mobile.matching.v1.GetRemainingAnonChatsResponse.remaining_chats', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETREMAININGANONCHATSRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1471,
  serialized_end=1619,
)


_CHATINTEREST = _descriptor.Descriptor(
  name='ChatInterest',
  full_name='mobile.matching.v1.ChatInterest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interest_id', full_name='mobile.matching.v1.ChatInterest.interest_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001(\0010\377\001'))),
    _descriptor.FieldDescriptor(
      name='interest_name', full_name='mobile.matching.v1.ChatInterest.interest_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1621,
  serialized_end=1705,
)


_SESSIONDETAILS = _descriptor.Descriptor(
  name='SessionDetails',
  full_name='mobile.matching.v1.SessionDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='mobile.matching.v1.SessionDetails.session_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='chat_partner_alias', full_name='mobile.matching.v1.SessionDetails.chat_partner_alias', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='session_end_time', full_name='mobile.matching.v1.SessionDetails.session_end_time', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session_expiry_time', full_name='mobile.matching.v1.SessionDetails.session_expiry_time', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session_state', full_name='mobile.matching.v1.SessionDetails.session_state', index=4,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1708,
  serialized_end=1999,
)

_FINDCHATPARTNERREQUEST.fields_by_name['interests'].message_type = _CHATINTEREST
_FINDCHATPARTNERRESPONSE.fields_by_name['result'].enum_type = _FINDCHATPARTNERRESPONSE_RESULT
_FINDCHATPARTNERRESPONSE.fields_by_name['find_chat_request_id'].message_type = common__model__pb2._XIUUID
_FINDCHATPARTNERRESPONSE.fields_by_name['session_details'].message_type = _SESSIONDETAILS
_FINDCHATPARTNERRESPONSE.fields_by_name['rejected_expiry_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FINDCHATPARTNERRESPONSE_RESULT.containing_type = _FINDCHATPARTNERRESPONSE
_CANCELFINDCHATPARTNERREQUEST.fields_by_name['find_chat_request_id'].message_type = common__model__pb2._XIUUID
_CANCELFINDCHATPARTNERRESPONSE.fields_by_name['result'].enum_type = _CANCELFINDCHATPARTNERRESPONSE_RESULT
_CANCELFINDCHATPARTNERRESPONSE_RESULT.containing_type = _CANCELFINDCHATPARTNERRESPONSE
_GETCHATSESSIONREQUEST.fields_by_name['session_key'].message_type = matching_dot_v1_dot_matching__common__pb2._ANONMATCHINGSESSIONKEY
_GETCHATSESSIONRESPONSE.fields_by_name['result'].enum_type = _GETCHATSESSIONRESPONSE_RESULT
_GETCHATSESSIONRESPONSE.fields_by_name['session_details'].message_type = _SESSIONDETAILS
_GETCHATSESSIONRESPONSE_RESULT.containing_type = _GETCHATSESSIONRESPONSE
_ENDCHATSESSIONREQUEST.fields_by_name['session_key'].message_type = matching_dot_v1_dot_matching__common__pb2._ANONMATCHINGSESSIONKEY
_ENDCHATSESSIONRESPONSE.fields_by_name['result'].enum_type = _ENDCHATSESSIONRESPONSE_RESULT
_ENDCHATSESSIONRESPONSE_RESULT.containing_type = _ENDCHATSESSIONRESPONSE
_GETREMAININGANONCHATSRESPONSE.fields_by_name['result'].enum_type = _GETREMAININGANONCHATSRESPONSE_RESULT
_GETREMAININGANONCHATSRESPONSE_RESULT.containing_type = _GETREMAININGANONCHATSRESPONSE
_SESSIONDETAILS.fields_by_name['session_id'].message_type = common__model__pb2._XIUUID
_SESSIONDETAILS.fields_by_name['chat_partner_alias'].message_type = common_dot_v1_dot_model__pb2._XIALIASJID
_SESSIONDETAILS.fields_by_name['session_end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SESSIONDETAILS.fields_by_name['session_expiry_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SESSIONDETAILS.fields_by_name['session_state'].enum_type = matching_dot_v1_dot_matching__common__pb2._CHATSESSIONSTATE
DESCRIPTOR.message_types_by_name['FindChatPartnerRequest'] = _FINDCHATPARTNERREQUEST
DESCRIPTOR.message_types_by_name['FindChatPartnerResponse'] = _FINDCHATPARTNERRESPONSE
DESCRIPTOR.message_types_by_name['CancelFindChatPartnerRequest'] = _CANCELFINDCHATPARTNERREQUEST
DESCRIPTOR.message_types_by_name['CancelFindChatPartnerResponse'] = _CANCELFINDCHATPARTNERRESPONSE
DESCRIPTOR.message_types_by_name['GetChatSessionRequest'] = _GETCHATSESSIONREQUEST
DESCRIPTOR.message_types_by_name['GetChatSessionResponse'] = _GETCHATSESSIONRESPONSE
DESCRIPTOR.message_types_by_name['EndChatSessionRequest'] = _ENDCHATSESSIONREQUEST
DESCRIPTOR.message_types_by_name['EndChatSessionResponse'] = _ENDCHATSESSIONRESPONSE
DESCRIPTOR.message_types_by_name['GetRemainingAnonChatsRequest'] = _GETREMAININGANONCHATSREQUEST
DESCRIPTOR.message_types_by_name['GetRemainingAnonChatsResponse'] = _GETREMAININGANONCHATSRESPONSE
DESCRIPTOR.message_types_by_name['ChatInterest'] = _CHATINTEREST
DESCRIPTOR.message_types_by_name['SessionDetails'] = _SESSIONDETAILS

FindChatPartnerRequest = _reflection.GeneratedProtocolMessageType('FindChatPartnerRequest', (_message.Message,), dict(
  DESCRIPTOR = _FINDCHATPARTNERREQUEST,
  __module__ = 'matching.v1.anon_matching_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.matching.v1.FindChatPartnerRequest)
  ))
_sym_db.RegisterMessage(FindChatPartnerRequest)

FindChatPartnerResponse = _reflection.GeneratedProtocolMessageType('FindChatPartnerResponse', (_message.Message,), dict(
  DESCRIPTOR = _FINDCHATPARTNERRESPONSE,
  __module__ = 'matching.v1.anon_matching_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.matching.v1.FindChatPartnerResponse)
  ))
_sym_db.RegisterMessage(FindChatPartnerResponse)

CancelFindChatPartnerRequest = _reflection.GeneratedProtocolMessageType('CancelFindChatPartnerRequest', (_message.Message,), dict(
  DESCRIPTOR = _CANCELFINDCHATPARTNERREQUEST,
  __module__ = 'matching.v1.anon_matching_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.matching.v1.CancelFindChatPartnerRequest)
  ))
_sym_db.RegisterMessage(CancelFindChatPartnerRequest)

CancelFindChatPartnerResponse = _reflection.GeneratedProtocolMessageType('CancelFindChatPartnerResponse', (_message.Message,), dict(
  DESCRIPTOR = _CANCELFINDCHATPARTNERRESPONSE,
  __module__ = 'matching.v1.anon_matching_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.matching.v1.CancelFindChatPartnerResponse)
  ))
_sym_db.RegisterMessage(CancelFindChatPartnerResponse)

GetChatSessionRequest = _reflection.GeneratedProtocolMessageType('GetChatSessionRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCHATSESSIONREQUEST,
  __module__ = 'matching.v1.anon_matching_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.matching.v1.GetChatSessionRequest)
  ))
_sym_db.RegisterMessage(GetChatSessionRequest)

GetChatSessionResponse = _reflection.GeneratedProtocolMessageType('GetChatSessionResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETCHATSESSIONRESPONSE,
  __module__ = 'matching.v1.anon_matching_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.matching.v1.GetChatSessionResponse)
  ))
_sym_db.RegisterMessage(GetChatSessionResponse)

EndChatSessionRequest = _reflection.GeneratedProtocolMessageType('EndChatSessionRequest', (_message.Message,), dict(
  DESCRIPTOR = _ENDCHATSESSIONREQUEST,
  __module__ = 'matching.v1.anon_matching_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.matching.v1.EndChatSessionRequest)
  ))
_sym_db.RegisterMessage(EndChatSessionRequest)

EndChatSessionResponse = _reflection.GeneratedProtocolMessageType('EndChatSessionResponse', (_message.Message,), dict(
  DESCRIPTOR = _ENDCHATSESSIONRESPONSE,
  __module__ = 'matching.v1.anon_matching_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.matching.v1.EndChatSessionResponse)
  ))
_sym_db.RegisterMessage(EndChatSessionResponse)

GetRemainingAnonChatsRequest = _reflection.GeneratedProtocolMessageType('GetRemainingAnonChatsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREMAININGANONCHATSREQUEST,
  __module__ = 'matching.v1.anon_matching_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.matching.v1.GetRemainingAnonChatsRequest)
  ))
_sym_db.RegisterMessage(GetRemainingAnonChatsRequest)

GetRemainingAnonChatsResponse = _reflection.GeneratedProtocolMessageType('GetRemainingAnonChatsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETREMAININGANONCHATSRESPONSE,
  __module__ = 'matching.v1.anon_matching_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.matching.v1.GetRemainingAnonChatsResponse)
  ))
_sym_db.RegisterMessage(GetRemainingAnonChatsResponse)

ChatInterest = _reflection.GeneratedProtocolMessageType('ChatInterest', (_message.Message,), dict(
  DESCRIPTOR = _CHATINTEREST,
  __module__ = 'matching.v1.anon_matching_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.matching.v1.ChatInterest)
  ))
_sym_db.RegisterMessage(ChatInterest)

SessionDetails = _reflection.GeneratedProtocolMessageType('SessionDetails', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONDETAILS,
  __module__ = 'matching.v1.anon_matching_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.matching.v1.SessionDetails)
  ))
_sym_db.RegisterMessage(SessionDetails)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\024com.kik.matching.rpcZNgithub.com/kikinteractive/xiphias-api-mobile/generated/go/matching/v1;matching'))
_FINDCHATPARTNERREQUEST.fields_by_name['interests'].has_options = True
_FINDCHATPARTNERREQUEST.fields_by_name['interests']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\003\200\001\005'))
_CANCELFINDCHATPARTNERREQUEST.fields_by_name['find_chat_request_id'].has_options = True
_CANCELFINDCHATPARTNERREQUEST.fields_by_name['find_chat_request_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_GETCHATSESSIONREQUEST.fields_by_name['session_key'].has_options = True
_GETCHATSESSIONREQUEST.fields_by_name['session_key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_ENDCHATSESSIONREQUEST.fields_by_name['session_key'].has_options = True
_ENDCHATSESSIONREQUEST.fields_by_name['session_key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_CHATINTEREST.fields_by_name['interest_id'].has_options = True
_CHATINTEREST.fields_by_name['interest_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001(\0010\377\001'))
_CHATINTEREST.fields_by_name['interest_name'].has_options = True
_CHATINTEREST.fields_by_name['interest_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001(\0010\377\001'))
_SESSIONDETAILS.fields_by_name['session_id'].has_options = True
_SESSIONDETAILS.fields_by_name['session_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_SESSIONDETAILS.fields_by_name['chat_partner_alias'].has_options = True
_SESSIONDETAILS.fields_by_name['chat_partner_alias']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
# @@protoc_insertion_point(module_scope)
