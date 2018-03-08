# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hotelService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hotelService.proto',
  package='com.example.demo',
  syntax='proto3',
  serialized_pb=_b('\n\x12hotelService.proto\x12\x10\x63om.example.demo\"-\n\x0cHotelRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\thotelName\x18\x02 \x01(\t\"\"\n\rHotelResponse\x12\x11\n\thotelText\x18\x01 \x01(\t2[\n\x0cHotelService\x12K\n\x08getHotel\x12\x1e.com.example.demo.HotelRequest\x1a\x1f.com.example.demo.HotelResponseB\x02P\x01\x62\x06proto3')
)




_HOTELREQUEST = _descriptor.Descriptor(
  name='HotelRequest',
  full_name='com.example.demo.HotelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.example.demo.HotelRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotelName', full_name='com.example.demo.HotelRequest.hotelName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=40,
  serialized_end=85,
)


_HOTELRESPONSE = _descriptor.Descriptor(
  name='HotelResponse',
  full_name='com.example.demo.HotelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hotelText', full_name='com.example.demo.HotelResponse.hotelText', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=87,
  serialized_end=121,
)

DESCRIPTOR.message_types_by_name['HotelRequest'] = _HOTELREQUEST
DESCRIPTOR.message_types_by_name['HotelResponse'] = _HOTELRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HotelRequest = _reflection.GeneratedProtocolMessageType('HotelRequest', (_message.Message,), dict(
  DESCRIPTOR = _HOTELREQUEST,
  __module__ = 'hotelService_pb2'
  # @@protoc_insertion_point(class_scope:com.example.demo.HotelRequest)
  ))
_sym_db.RegisterMessage(HotelRequest)

HotelResponse = _reflection.GeneratedProtocolMessageType('HotelResponse', (_message.Message,), dict(
  DESCRIPTOR = _HOTELRESPONSE,
  __module__ = 'hotelService_pb2'
  # @@protoc_insertion_point(class_scope:com.example.demo.HotelResponse)
  ))
_sym_db.RegisterMessage(HotelResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))

_HOTELSERVICE = _descriptor.ServiceDescriptor(
  name='HotelService',
  full_name='com.example.demo.HotelService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=123,
  serialized_end=214,
  methods=[
  _descriptor.MethodDescriptor(
    name='getHotel',
    full_name='com.example.demo.HotelService.getHotel',
    index=0,
    containing_service=None,
    input_type=_HOTELREQUEST,
    output_type=_HOTELRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HOTELSERVICE)

DESCRIPTOR.services_by_name['HotelService'] = _HOTELSERVICE

# @@protoc_insertion_point(module_scope)
