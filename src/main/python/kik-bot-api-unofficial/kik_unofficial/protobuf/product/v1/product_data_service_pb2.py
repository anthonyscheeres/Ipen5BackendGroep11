# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: product/v1/product_data_service.proto

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
from kik_unofficial.protobuf.asset.v1 import asset_common_pb2 as asset_dot_v1_dot_asset__common__pb2
from kik_unofficial.protobuf.kin.authentication.v1 import authentication_common_pb2 as kin_dot_authentication_dot_v1_dot_authentication__common__pb2
import kik_unofficial.protobuf.common_model_pb2 as common__model__pb2
from kik_unofficial.protobuf.product.v1 import product_data_common_pb2 as product_dot_v1_dot_product__data__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='product/v1/product_data_service.proto',
  package='mobile.product.v1',
  syntax='proto3',
  serialized_pb=_b('\n%product/v1/product_data_service.proto\x12\x11mobile.product.v1\x1a\x19protobuf_validation.proto\x1a\x1b\x61sset/v1/asset_common.proto\x1a\x31kin/authentication/v1/authentication_common.proto\x1a\x12\x63ommon_model.proto\x1a$product/v1/product_data_common.proto\"\xfd\x01\n\x1bGetProductCollectionRequest\x12\x17\n\x02id\x18\x01 \x01(\tB\x0b\xca\x9d%\x07\x08\x01(\x01\x30\xff\x01\x12\x34\n\rpixel_density\x18\x02 \x01(\x0e\x32\x1d.common.asset.v1.PixelDensity\x12 \n\tpage_size\x18\x03 \x01(\x05\x42\r\xca\x9d%\tA(\x00\x00\x00\x00\x00\x00\x00\x12<\n\x10pagination_token\x18\x04 \x01(\x0b\x32\".mobile.product.v1.PaginationToken\x12/\n\x08user_jid\x18\n \x01(\x0b\x32\x15.common.XiBareUserJidB\x06\xca\x9d%\x02\x08\x01\"\x96\x02\n\x1cGetProductCollectionResponse\x12\x46\n\x06result\x18\x01 \x01(\x0e\x32\x36.mobile.product.v1.GetProductCollectionResponse.Result\x12\x35\n\x08products\x18\x02 \x03(\x0b\x32\x1a.mobile.product.v1.ProductB\x07\xca\x9d%\x03\x80\x01(\x12\x18\n\x10internal_version\x18\x03 \x01(\x04\x12<\n\x10pagination_token\x18\x04 \x01(\x0b\x32\".mobile.product.v1.PaginationToken\"\x1f\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\r\n\tNOT_FOUND\x10\x01\"\xa3\x01\n\x12GetProductsRequest\x12&\n\x03ids\x18\x01 \x03(\x0b\x32\x0e.common.XiUuidB\t\xca\x9d%\x05x\x01\x80\x01\x14\x12\x34\n\rpixel_density\x18\x02 \x01(\x0e\x32\x1d.common.asset.v1.PixelDensity\x12/\n\x08user_jid\x18\n \x01(\x0b\x32\x15.common.XiBareUserJidB\x06\xca\x9d%\x02\x08\x01\")\n\x0fPaginationToken\x12\x16\n\x05token\x18\x01 \x01(\x0c\x42\x07\xca\x9d%\x03\x30\x80(\"\x96\x02\n\x13GetProductsResponse\x12=\n\x06result\x18\x01 \x01(\x0e\x32-.mobile.product.v1.GetProductsResponse.Result\x12\x35\n\x08products\x18\n \x03(\x0b\x32\x1a.mobile.product.v1.ProductB\x07\xca\x9d%\x03\x80\x01\x14\x12+\n\nfailed_ids\x18\x0b \x03(\x0b\x32\x0e.common.XiUuidB\x07\xca\x9d%\x03\x80\x01\x14\x12.\n\rnot_found_ids\x18\x0c \x03(\x0b\x32\x0e.common.XiUuidB\x07\xca\x9d%\x03\x80\x01\x14\",\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x0b\n\x07PARTIAL\x10\x01\x12\r\n\tNOT_FOUND\x10\x02\"]\n\x14GetProductJwtRequest\x12\x45\n\toffer_ids\x18\x01 \x03(\x0b\x32%.common.kin.authentication.v1.OfferIdB\x0b\xca\x9d%\x07\x08\x01x\x01\x80\x01\x14\"\\\n\x15GetProductJwtResponse\x12\x43\n\noffer_jwts\x18\x01 \x03(\x0b\x32&.common.kin.authentication.v1.OfferJwtB\x07\xca\x9d%\x03\x80\x01\x14\"\x95\x01\n\x14UnlockProductRequest\x12/\n\x08user_jid\x18\x01 \x01(\x0b\x32\x15.common.XiBareUserJidB\x06\xca\x9d%\x02\x08\x01\x12L\n\x14payment_confirmation\x18\x02 \x01(\x0b\x32&.common.product.v1.PaymentConfirmationB\x06\xca\x9d%\x02\x08\x01\"\xc4\x01\n\x15UnlockProductResponse\x12?\n\x06result\x18\x01 \x01(\x0e\x32/.mobile.product.v1.UnlockProductResponse.Result\x12J\n\x14jwt_rejection_reason\x18\x02 \x01(\x0b\x32,.mobile.product.v1.ProductJwtRejectionReason\"\x1e\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x0c\n\x08REJECTED\x10\x01\"\xd1\x01\n\x07Product\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x0e.common.XiUuidB\x06\xca\x9d%\x02\x08\x01\x12\x38\n\x0fproduct_content\x18\x02 \x01(\x0b\x32\x1f.common.asset.v1.ProductContent\x12\x30\n\nprice_data\x18\x03 \x01(\x0b\x32\x1c.common.product.v1.PriceData\x12\x36\n\rpurchase_data\x18\x04 \x01(\x0b\x32\x1f.common.product.v1.PurchaseData\"\xb5\x01\n\x19ProductJwtRejectionReason\x12?\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x31.mobile.product.v1.ProductJwtRejectionReason.Code\"W\n\x04\x43ode\x12\x0b\n\x07UNKNOWN\x10\x00\x12 \n\x1cREJECTED_PRODUCT_JWT_INVALID\x10\x01\x12 \n\x1cREJECTED_PRODUCT_JWT_EXPIRED\x10\x02\x32\xac\x03\n\x0bProductData\x12w\n\x14GetProductCollection\x12..mobile.product.v1.GetProductCollectionRequest\x1a/.mobile.product.v1.GetProductCollectionResponse\x12\\\n\x0bGetProducts\x12%.mobile.product.v1.GetProductsRequest\x1a&.mobile.product.v1.GetProductsResponse\x12\x62\n\rGetProductJwt\x12\'.mobile.product.v1.GetProductJwtRequest\x1a(.mobile.product.v1.GetProductJwtResponse\x12\x62\n\rUnlockProduct\x12\'.mobile.product.v1.UnlockProductRequest\x1a(.mobile.product.v1.UnlockProductResponseBc\n\x13\x63om.kik.product.rpcZLgithub.com/kikinteractive/xiphias-api-mobile/generated/go/product/v1;productb\x06proto3')
  ,
  dependencies=[protobuf__validation__pb2.DESCRIPTOR,asset_dot_v1_dot_asset__common__pb2.DESCRIPTOR,kin_dot_authentication_dot_v1_dot_authentication__common__pb2.DESCRIPTOR,common__model__pb2.DESCRIPTOR,product_dot_v1_dot_product__data__common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETPRODUCTCOLLECTIONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.product.v1.GetProductCollectionResponse.Result',
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
  serialized_start=729,
  serialized_end=760,
)
_sym_db.RegisterEnumDescriptor(_GETPRODUCTCOLLECTIONRESPONSE_RESULT)

_GETPRODUCTSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.product.v1.GetProductsResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTIAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1206,
  serialized_end=1250,
)
_sym_db.RegisterEnumDescriptor(_GETPRODUCTSRESPONSE_RESULT)

_UNLOCKPRODUCTRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mobile.product.v1.UnlockProductResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECTED', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1760,
  serialized_end=1790,
)
_sym_db.RegisterEnumDescriptor(_UNLOCKPRODUCTRESPONSE_RESULT)

_PRODUCTJWTREJECTIONREASON_CODE = _descriptor.EnumDescriptor(
  name='Code',
  full_name='mobile.product.v1.ProductJwtRejectionReason.Code',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECTED_PRODUCT_JWT_INVALID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECTED_PRODUCT_JWT_EXPIRED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2099,
  serialized_end=2186,
)
_sym_db.RegisterEnumDescriptor(_PRODUCTJWTREJECTIONREASON_CODE)


_GETPRODUCTCOLLECTIONREQUEST = _descriptor.Descriptor(
  name='GetProductCollectionRequest',
  full_name='mobile.product.v1.GetProductCollectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mobile.product.v1.GetProductCollectionRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001(\0010\377\001'))),
    _descriptor.FieldDescriptor(
      name='pixel_density', full_name='mobile.product.v1.GetProductCollectionRequest.pixel_density', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='mobile.product.v1.GetProductCollectionRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\tA(\000\000\000\000\000\000\000'))),
    _descriptor.FieldDescriptor(
      name='pagination_token', full_name='mobile.product.v1.GetProductCollectionRequest.pagination_token', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_jid', full_name='mobile.product.v1.GetProductCollectionRequest.user_jid', index=4,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=226,
  serialized_end=479,
)


_GETPRODUCTCOLLECTIONRESPONSE = _descriptor.Descriptor(
  name='GetProductCollectionResponse',
  full_name='mobile.product.v1.GetProductCollectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.product.v1.GetProductCollectionResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='products', full_name='mobile.product.v1.GetProductCollectionResponse.products', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\003\200\001('))),
    _descriptor.FieldDescriptor(
      name='internal_version', full_name='mobile.product.v1.GetProductCollectionResponse.internal_version', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pagination_token', full_name='mobile.product.v1.GetProductCollectionResponse.pagination_token', index=3,
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
    _GETPRODUCTCOLLECTIONRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=482,
  serialized_end=760,
)


_GETPRODUCTSREQUEST = _descriptor.Descriptor(
  name='GetProductsRequest',
  full_name='mobile.product.v1.GetProductsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='mobile.product.v1.GetProductsRequest.ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005x\001\200\001\024'))),
    _descriptor.FieldDescriptor(
      name='pixel_density', full_name='mobile.product.v1.GetProductsRequest.pixel_density', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_jid', full_name='mobile.product.v1.GetProductsRequest.user_jid', index=2,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=763,
  serialized_end=926,
)


_PAGINATIONTOKEN = _descriptor.Descriptor(
  name='PaginationToken',
  full_name='mobile.product.v1.PaginationToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='mobile.product.v1.PaginationToken.token', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\0030\200('))),
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
  serialized_start=928,
  serialized_end=969,
)


_GETPRODUCTSRESPONSE = _descriptor.Descriptor(
  name='GetProductsResponse',
  full_name='mobile.product.v1.GetProductsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.product.v1.GetProductsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='products', full_name='mobile.product.v1.GetProductsResponse.products', index=1,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\003\200\001\024'))),
    _descriptor.FieldDescriptor(
      name='failed_ids', full_name='mobile.product.v1.GetProductsResponse.failed_ids', index=2,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\003\200\001\024'))),
    _descriptor.FieldDescriptor(
      name='not_found_ids', full_name='mobile.product.v1.GetProductsResponse.not_found_ids', index=3,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\003\200\001\024'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETPRODUCTSRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=972,
  serialized_end=1250,
)


_GETPRODUCTJWTREQUEST = _descriptor.Descriptor(
  name='GetProductJwtRequest',
  full_name='mobile.product.v1.GetProductJwtRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offer_ids', full_name='mobile.product.v1.GetProductJwtRequest.offer_ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001x\001\200\001\024'))),
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
  serialized_start=1252,
  serialized_end=1345,
)


_GETPRODUCTJWTRESPONSE = _descriptor.Descriptor(
  name='GetProductJwtResponse',
  full_name='mobile.product.v1.GetProductJwtResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offer_jwts', full_name='mobile.product.v1.GetProductJwtResponse.offer_jwts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\003\200\001\024'))),
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
  serialized_start=1347,
  serialized_end=1439,
)


_UNLOCKPRODUCTREQUEST = _descriptor.Descriptor(
  name='UnlockProductRequest',
  full_name='mobile.product.v1.UnlockProductRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_jid', full_name='mobile.product.v1.UnlockProductRequest.user_jid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='payment_confirmation', full_name='mobile.product.v1.UnlockProductRequest.payment_confirmation', index=1,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1442,
  serialized_end=1591,
)


_UNLOCKPRODUCTRESPONSE = _descriptor.Descriptor(
  name='UnlockProductResponse',
  full_name='mobile.product.v1.UnlockProductResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mobile.product.v1.UnlockProductResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jwt_rejection_reason', full_name='mobile.product.v1.UnlockProductResponse.jwt_rejection_reason', index=1,
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
    _UNLOCKPRODUCTRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1594,
  serialized_end=1790,
)


_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='mobile.product.v1.Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mobile.product.v1.Product.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='product_content', full_name='mobile.product.v1.Product.product_content', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_data', full_name='mobile.product.v1.Product.price_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='purchase_data', full_name='mobile.product.v1.Product.purchase_data', index=3,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1793,
  serialized_end=2002,
)


_PRODUCTJWTREJECTIONREASON = _descriptor.Descriptor(
  name='ProductJwtRejectionReason',
  full_name='mobile.product.v1.ProductJwtRejectionReason',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='mobile.product.v1.ProductJwtRejectionReason.code', index=0,
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
    _PRODUCTJWTREJECTIONREASON_CODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2005,
  serialized_end=2186,
)

_GETPRODUCTCOLLECTIONREQUEST.fields_by_name['pixel_density'].enum_type = asset_dot_v1_dot_asset__common__pb2._PIXELDENSITY
_GETPRODUCTCOLLECTIONREQUEST.fields_by_name['pagination_token'].message_type = _PAGINATIONTOKEN
_GETPRODUCTCOLLECTIONREQUEST.fields_by_name['user_jid'].message_type = common__model__pb2._XIBAREUSERJID
_GETPRODUCTCOLLECTIONRESPONSE.fields_by_name['result'].enum_type = _GETPRODUCTCOLLECTIONRESPONSE_RESULT
_GETPRODUCTCOLLECTIONRESPONSE.fields_by_name['products'].message_type = _PRODUCT
_GETPRODUCTCOLLECTIONRESPONSE.fields_by_name['pagination_token'].message_type = _PAGINATIONTOKEN
_GETPRODUCTCOLLECTIONRESPONSE_RESULT.containing_type = _GETPRODUCTCOLLECTIONRESPONSE
_GETPRODUCTSREQUEST.fields_by_name['ids'].message_type = common__model__pb2._XIUUID
_GETPRODUCTSREQUEST.fields_by_name['pixel_density'].enum_type = asset_dot_v1_dot_asset__common__pb2._PIXELDENSITY
_GETPRODUCTSREQUEST.fields_by_name['user_jid'].message_type = common__model__pb2._XIBAREUSERJID
_GETPRODUCTSRESPONSE.fields_by_name['result'].enum_type = _GETPRODUCTSRESPONSE_RESULT
_GETPRODUCTSRESPONSE.fields_by_name['products'].message_type = _PRODUCT
_GETPRODUCTSRESPONSE.fields_by_name['failed_ids'].message_type = common__model__pb2._XIUUID
_GETPRODUCTSRESPONSE.fields_by_name['not_found_ids'].message_type = common__model__pb2._XIUUID
_GETPRODUCTSRESPONSE_RESULT.containing_type = _GETPRODUCTSRESPONSE
_GETPRODUCTJWTREQUEST.fields_by_name['offer_ids'].message_type = kin_dot_authentication_dot_v1_dot_authentication__common__pb2._OFFERID
_GETPRODUCTJWTRESPONSE.fields_by_name['offer_jwts'].message_type = kin_dot_authentication_dot_v1_dot_authentication__common__pb2._OFFERJWT
_UNLOCKPRODUCTREQUEST.fields_by_name['user_jid'].message_type = common__model__pb2._XIBAREUSERJID
_UNLOCKPRODUCTREQUEST.fields_by_name['payment_confirmation'].message_type = product_dot_v1_dot_product__data__common__pb2._PAYMENTCONFIRMATION
_UNLOCKPRODUCTRESPONSE.fields_by_name['result'].enum_type = _UNLOCKPRODUCTRESPONSE_RESULT
_UNLOCKPRODUCTRESPONSE.fields_by_name['jwt_rejection_reason'].message_type = _PRODUCTJWTREJECTIONREASON
_UNLOCKPRODUCTRESPONSE_RESULT.containing_type = _UNLOCKPRODUCTRESPONSE
_PRODUCT.fields_by_name['id'].message_type = common__model__pb2._XIUUID
_PRODUCT.fields_by_name['product_content'].message_type = asset_dot_v1_dot_asset__common__pb2._PRODUCTCONTENT
_PRODUCT.fields_by_name['price_data'].message_type = product_dot_v1_dot_product__data__common__pb2._PRICEDATA
_PRODUCT.fields_by_name['purchase_data'].message_type = product_dot_v1_dot_product__data__common__pb2._PURCHASEDATA
_PRODUCTJWTREJECTIONREASON.fields_by_name['code'].enum_type = _PRODUCTJWTREJECTIONREASON_CODE
_PRODUCTJWTREJECTIONREASON_CODE.containing_type = _PRODUCTJWTREJECTIONREASON
DESCRIPTOR.message_types_by_name['GetProductCollectionRequest'] = _GETPRODUCTCOLLECTIONREQUEST
DESCRIPTOR.message_types_by_name['GetProductCollectionResponse'] = _GETPRODUCTCOLLECTIONRESPONSE
DESCRIPTOR.message_types_by_name['GetProductsRequest'] = _GETPRODUCTSREQUEST
DESCRIPTOR.message_types_by_name['PaginationToken'] = _PAGINATIONTOKEN
DESCRIPTOR.message_types_by_name['GetProductsResponse'] = _GETPRODUCTSRESPONSE
DESCRIPTOR.message_types_by_name['GetProductJwtRequest'] = _GETPRODUCTJWTREQUEST
DESCRIPTOR.message_types_by_name['GetProductJwtResponse'] = _GETPRODUCTJWTRESPONSE
DESCRIPTOR.message_types_by_name['UnlockProductRequest'] = _UNLOCKPRODUCTREQUEST
DESCRIPTOR.message_types_by_name['UnlockProductResponse'] = _UNLOCKPRODUCTRESPONSE
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['ProductJwtRejectionReason'] = _PRODUCTJWTREJECTIONREASON

GetProductCollectionRequest = _reflection.GeneratedProtocolMessageType('GetProductCollectionRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPRODUCTCOLLECTIONREQUEST,
  __module__ = 'product.v1.product_data_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.product.v1.GetProductCollectionRequest)
  ))
_sym_db.RegisterMessage(GetProductCollectionRequest)

GetProductCollectionResponse = _reflection.GeneratedProtocolMessageType('GetProductCollectionResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPRODUCTCOLLECTIONRESPONSE,
  __module__ = 'product.v1.product_data_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.product.v1.GetProductCollectionResponse)
  ))
_sym_db.RegisterMessage(GetProductCollectionResponse)

GetProductsRequest = _reflection.GeneratedProtocolMessageType('GetProductsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPRODUCTSREQUEST,
  __module__ = 'product.v1.product_data_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.product.v1.GetProductsRequest)
  ))
_sym_db.RegisterMessage(GetProductsRequest)

PaginationToken = _reflection.GeneratedProtocolMessageType('PaginationToken', (_message.Message,), dict(
  DESCRIPTOR = _PAGINATIONTOKEN,
  __module__ = 'product.v1.product_data_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.product.v1.PaginationToken)
  ))
_sym_db.RegisterMessage(PaginationToken)

GetProductsResponse = _reflection.GeneratedProtocolMessageType('GetProductsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPRODUCTSRESPONSE,
  __module__ = 'product.v1.product_data_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.product.v1.GetProductsResponse)
  ))
_sym_db.RegisterMessage(GetProductsResponse)

GetProductJwtRequest = _reflection.GeneratedProtocolMessageType('GetProductJwtRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPRODUCTJWTREQUEST,
  __module__ = 'product.v1.product_data_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.product.v1.GetProductJwtRequest)
  ))
_sym_db.RegisterMessage(GetProductJwtRequest)

GetProductJwtResponse = _reflection.GeneratedProtocolMessageType('GetProductJwtResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPRODUCTJWTRESPONSE,
  __module__ = 'product.v1.product_data_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.product.v1.GetProductJwtResponse)
  ))
_sym_db.RegisterMessage(GetProductJwtResponse)

UnlockProductRequest = _reflection.GeneratedProtocolMessageType('UnlockProductRequest', (_message.Message,), dict(
  DESCRIPTOR = _UNLOCKPRODUCTREQUEST,
  __module__ = 'product.v1.product_data_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.product.v1.UnlockProductRequest)
  ))
_sym_db.RegisterMessage(UnlockProductRequest)

UnlockProductResponse = _reflection.GeneratedProtocolMessageType('UnlockProductResponse', (_message.Message,), dict(
  DESCRIPTOR = _UNLOCKPRODUCTRESPONSE,
  __module__ = 'product.v1.product_data_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.product.v1.UnlockProductResponse)
  ))
_sym_db.RegisterMessage(UnlockProductResponse)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCT,
  __module__ = 'product.v1.product_data_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.product.v1.Product)
  ))
_sym_db.RegisterMessage(Product)

ProductJwtRejectionReason = _reflection.GeneratedProtocolMessageType('ProductJwtRejectionReason', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCTJWTREJECTIONREASON,
  __module__ = 'product.v1.product_data_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.product.v1.ProductJwtRejectionReason)
  ))
_sym_db.RegisterMessage(ProductJwtRejectionReason)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.kik.product.rpcZLgithub.com/kikinteractive/xiphias-api-mobile/generated/go/product/v1;product'))
_GETPRODUCTCOLLECTIONREQUEST.fields_by_name['id'].has_options = True
_GETPRODUCTCOLLECTIONREQUEST.fields_by_name['id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001(\0010\377\001'))
_GETPRODUCTCOLLECTIONREQUEST.fields_by_name['page_size'].has_options = True
_GETPRODUCTCOLLECTIONREQUEST.fields_by_name['page_size']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\tA(\000\000\000\000\000\000\000'))
_GETPRODUCTCOLLECTIONREQUEST.fields_by_name['user_jid'].has_options = True
_GETPRODUCTCOLLECTIONREQUEST.fields_by_name['user_jid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_GETPRODUCTCOLLECTIONRESPONSE.fields_by_name['products'].has_options = True
_GETPRODUCTCOLLECTIONRESPONSE.fields_by_name['products']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\003\200\001('))
_GETPRODUCTSREQUEST.fields_by_name['ids'].has_options = True
_GETPRODUCTSREQUEST.fields_by_name['ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005x\001\200\001\024'))
_GETPRODUCTSREQUEST.fields_by_name['user_jid'].has_options = True
_GETPRODUCTSREQUEST.fields_by_name['user_jid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_PAGINATIONTOKEN.fields_by_name['token'].has_options = True
_PAGINATIONTOKEN.fields_by_name['token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\0030\200('))
_GETPRODUCTSRESPONSE.fields_by_name['products'].has_options = True
_GETPRODUCTSRESPONSE.fields_by_name['products']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\003\200\001\024'))
_GETPRODUCTSRESPONSE.fields_by_name['failed_ids'].has_options = True
_GETPRODUCTSRESPONSE.fields_by_name['failed_ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\003\200\001\024'))
_GETPRODUCTSRESPONSE.fields_by_name['not_found_ids'].has_options = True
_GETPRODUCTSRESPONSE.fields_by_name['not_found_ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\003\200\001\024'))
_GETPRODUCTJWTREQUEST.fields_by_name['offer_ids'].has_options = True
_GETPRODUCTJWTREQUEST.fields_by_name['offer_ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001x\001\200\001\024'))
_GETPRODUCTJWTRESPONSE.fields_by_name['offer_jwts'].has_options = True
_GETPRODUCTJWTRESPONSE.fields_by_name['offer_jwts']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\003\200\001\024'))
_UNLOCKPRODUCTREQUEST.fields_by_name['user_jid'].has_options = True
_UNLOCKPRODUCTREQUEST.fields_by_name['user_jid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_UNLOCKPRODUCTREQUEST.fields_by_name['payment_confirmation'].has_options = True
_UNLOCKPRODUCTREQUEST.fields_by_name['payment_confirmation']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_PRODUCT.fields_by_name['id'].has_options = True
_PRODUCT.fields_by_name['id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
# @@protoc_insertion_point(module_scope)
