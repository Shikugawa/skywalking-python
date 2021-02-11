# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: language-agent/Tracing.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Common_pb2 as common_dot_Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='language-agent/Tracing.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n3org.apache.skywalking.apm.network.language.agent.v3P\001Z$skywalking/network/language/agent/v3\252\002\032SkyWalking.NetworkProtocol',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1clanguage-agent/Tracing.proto\x1a\x13\x63ommon/Common.proto\"\x95\x01\n\rSegmentObject\x12\x0f\n\x07traceId\x18\x01 \x01(\t\x12\x16\n\x0etraceSegmentId\x18\x02 \x01(\t\x12\x1a\n\x05spans\x18\x03 \x03(\x0b\x32\x0b.SpanObject\x12\x0f\n\x07service\x18\x04 \x01(\t\x12\x17\n\x0fserviceInstance\x18\x05 \x01(\t\x12\x15\n\risSizeLimited\x18\x06 \x01(\x08\"\xe2\x01\n\x10SegmentReference\x12\x19\n\x07refType\x18\x01 \x01(\x0e\x32\x08.RefType\x12\x0f\n\x07traceId\x18\x02 \x01(\t\x12\x1c\n\x14parentTraceSegmentId\x18\x03 \x01(\t\x12\x14\n\x0cparentSpanId\x18\x04 \x01(\x05\x12\x15\n\rparentService\x18\x05 \x01(\t\x12\x1d\n\x15parentServiceInstance\x18\x06 \x01(\t\x12\x16\n\x0eparentEndpoint\x18\x07 \x01(\t\x12 \n\x18networkAddressUsedAtPeer\x18\x08 \x01(\t\"\xcb\x02\n\nSpanObject\x12\x0e\n\x06spanId\x18\x01 \x01(\x05\x12\x14\n\x0cparentSpanId\x18\x02 \x01(\x05\x12\x11\n\tstartTime\x18\x03 \x01(\x03\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x03\x12\x1f\n\x04refs\x18\x05 \x03(\x0b\x32\x11.SegmentReference\x12\x15\n\roperationName\x18\x06 \x01(\t\x12\x0c\n\x04peer\x18\x07 \x01(\t\x12\x1b\n\x08spanType\x18\x08 \x01(\x0e\x32\t.SpanType\x12\x1d\n\tspanLayer\x18\t \x01(\x0e\x32\n.SpanLayer\x12\x13\n\x0b\x63omponentId\x18\n \x01(\x05\x12\x0f\n\x07isError\x18\x0b \x01(\x08\x12!\n\x04tags\x18\x0c \x03(\x0b\x32\x13.KeyStringValuePair\x12\x12\n\x04logs\x18\r \x03(\x0b\x32\x04.Log\x12\x14\n\x0cskipAnalysis\x18\x0e \x01(\x08\"6\n\x03Log\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12!\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x13.KeyStringValuePair\"\x10\n\x02ID\x12\n\n\x02id\x18\x01 \x03(\t**\n\x08SpanType\x12\t\n\x05\x45ntry\x10\x00\x12\x08\n\x04\x45xit\x10\x01\x12\t\n\x05Local\x10\x02*,\n\x07RefType\x12\x10\n\x0c\x43rossProcess\x10\x00\x12\x0f\n\x0b\x43rossThread\x10\x01*U\n\tSpanLayer\x12\x0b\n\x07Unknown\x10\x00\x12\x0c\n\x08\x44\x61tabase\x10\x01\x12\x10\n\x0cRPCFramework\x10\x02\x12\x08\n\x04Http\x10\x03\x12\x06\n\x02MQ\x10\x04\x12\t\n\x05\x43\x61\x63he\x10\x05\x32\x45\n\x19TraceSegmentReportService\x12(\n\x07\x63ollect\x12\x0e.SegmentObject\x1a\t.Commands\"\x00(\x01\x42z\n3org.apache.skywalking.apm.network.language.agent.v3P\x01Z$skywalking/network/language/agent/v3\xaa\x02\x1aSkyWalking.NetworkProtocolb\x06proto3'
  ,
  dependencies=[common_dot_Common__pb2.DESCRIPTOR,])

_SPANTYPE = _descriptor.EnumDescriptor(
  name='SpanType',
  full_name='SpanType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Entry', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Exit', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Local', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=842,
  serialized_end=884,
)
_sym_db.RegisterEnumDescriptor(_SPANTYPE)

SpanType = enum_type_wrapper.EnumTypeWrapper(_SPANTYPE)
_REFTYPE = _descriptor.EnumDescriptor(
  name='RefType',
  full_name='RefType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CrossProcess', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CrossThread', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=886,
  serialized_end=930,
)
_sym_db.RegisterEnumDescriptor(_REFTYPE)

RefType = enum_type_wrapper.EnumTypeWrapper(_REFTYPE)
_SPANLAYER = _descriptor.EnumDescriptor(
  name='SpanLayer',
  full_name='SpanLayer',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Database', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RPCFramework', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Http', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MQ', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Cache', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=932,
  serialized_end=1017,
)
_sym_db.RegisterEnumDescriptor(_SPANLAYER)

SpanLayer = enum_type_wrapper.EnumTypeWrapper(_SPANLAYER)
Entry = 0
Exit = 1
Local = 2
CrossProcess = 0
CrossThread = 1
Unknown = 0
Database = 1
RPCFramework = 2
Http = 3
MQ = 4
Cache = 5



_SEGMENTOBJECT = _descriptor.Descriptor(
  name='SegmentObject',
  full_name='SegmentObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='traceId', full_name='SegmentObject.traceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='traceSegmentId', full_name='SegmentObject.traceSegmentId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spans', full_name='SegmentObject.spans', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service', full_name='SegmentObject.service', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceInstance', full_name='SegmentObject.serviceInstance', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isSizeLimited', full_name='SegmentObject.isSizeLimited', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=203,
)


_SEGMENTREFERENCE = _descriptor.Descriptor(
  name='SegmentReference',
  full_name='SegmentReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='refType', full_name='SegmentReference.refType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='traceId', full_name='SegmentReference.traceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parentTraceSegmentId', full_name='SegmentReference.parentTraceSegmentId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parentSpanId', full_name='SegmentReference.parentSpanId', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parentService', full_name='SegmentReference.parentService', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parentServiceInstance', full_name='SegmentReference.parentServiceInstance', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parentEndpoint', full_name='SegmentReference.parentEndpoint', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='networkAddressUsedAtPeer', full_name='SegmentReference.networkAddressUsedAtPeer', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=432,
)


_SPANOBJECT = _descriptor.Descriptor(
  name='SpanObject',
  full_name='SpanObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='spanId', full_name='SpanObject.spanId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parentSpanId', full_name='SpanObject.parentSpanId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='SpanObject.startTime', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='SpanObject.endTime', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='refs', full_name='SpanObject.refs', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operationName', full_name='SpanObject.operationName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peer', full_name='SpanObject.peer', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spanType', full_name='SpanObject.spanType', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spanLayer', full_name='SpanObject.spanLayer', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='componentId', full_name='SpanObject.componentId', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isError', full_name='SpanObject.isError', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='SpanObject.tags', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logs', full_name='SpanObject.logs', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='skipAnalysis', full_name='SpanObject.skipAnalysis', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=766,
)


_LOG = _descriptor.Descriptor(
  name='Log',
  full_name='Log',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='Log.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='Log.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=768,
  serialized_end=822,
)


_ID = _descriptor.Descriptor(
  name='ID',
  full_name='ID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ID.id', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=824,
  serialized_end=840,
)

_SEGMENTOBJECT.fields_by_name['spans'].message_type = _SPANOBJECT
_SEGMENTREFERENCE.fields_by_name['refType'].enum_type = _REFTYPE
_SPANOBJECT.fields_by_name['refs'].message_type = _SEGMENTREFERENCE
_SPANOBJECT.fields_by_name['spanType'].enum_type = _SPANTYPE
_SPANOBJECT.fields_by_name['spanLayer'].enum_type = _SPANLAYER
_SPANOBJECT.fields_by_name['tags'].message_type = common_dot_Common__pb2._KEYSTRINGVALUEPAIR
_SPANOBJECT.fields_by_name['logs'].message_type = _LOG
_LOG.fields_by_name['data'].message_type = common_dot_Common__pb2._KEYSTRINGVALUEPAIR
DESCRIPTOR.message_types_by_name['SegmentObject'] = _SEGMENTOBJECT
DESCRIPTOR.message_types_by_name['SegmentReference'] = _SEGMENTREFERENCE
DESCRIPTOR.message_types_by_name['SpanObject'] = _SPANOBJECT
DESCRIPTOR.message_types_by_name['Log'] = _LOG
DESCRIPTOR.message_types_by_name['ID'] = _ID
DESCRIPTOR.enum_types_by_name['SpanType'] = _SPANTYPE
DESCRIPTOR.enum_types_by_name['RefType'] = _REFTYPE
DESCRIPTOR.enum_types_by_name['SpanLayer'] = _SPANLAYER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SegmentObject = _reflection.GeneratedProtocolMessageType('SegmentObject', (_message.Message,), {
  'DESCRIPTOR' : _SEGMENTOBJECT,
  '__module__' : 'language_agent.Tracing_pb2'
  # @@protoc_insertion_point(class_scope:SegmentObject)
  })
_sym_db.RegisterMessage(SegmentObject)

SegmentReference = _reflection.GeneratedProtocolMessageType('SegmentReference', (_message.Message,), {
  'DESCRIPTOR' : _SEGMENTREFERENCE,
  '__module__' : 'language_agent.Tracing_pb2'
  # @@protoc_insertion_point(class_scope:SegmentReference)
  })
_sym_db.RegisterMessage(SegmentReference)

SpanObject = _reflection.GeneratedProtocolMessageType('SpanObject', (_message.Message,), {
  'DESCRIPTOR' : _SPANOBJECT,
  '__module__' : 'language_agent.Tracing_pb2'
  # @@protoc_insertion_point(class_scope:SpanObject)
  })
_sym_db.RegisterMessage(SpanObject)

Log = _reflection.GeneratedProtocolMessageType('Log', (_message.Message,), {
  'DESCRIPTOR' : _LOG,
  '__module__' : 'language_agent.Tracing_pb2'
  # @@protoc_insertion_point(class_scope:Log)
  })
_sym_db.RegisterMessage(Log)

ID = _reflection.GeneratedProtocolMessageType('ID', (_message.Message,), {
  'DESCRIPTOR' : _ID,
  '__module__' : 'language_agent.Tracing_pb2'
  # @@protoc_insertion_point(class_scope:ID)
  })
_sym_db.RegisterMessage(ID)


DESCRIPTOR._options = None

_TRACESEGMENTREPORTSERVICE = _descriptor.ServiceDescriptor(
  name='TraceSegmentReportService',
  full_name='TraceSegmentReportService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1019,
  serialized_end=1088,
  methods=[
  _descriptor.MethodDescriptor(
    name='collect',
    full_name='TraceSegmentReportService.collect',
    index=0,
    containing_service=None,
    input_type=_SEGMENTOBJECT,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRACESEGMENTREPORTSERVICE)

DESCRIPTOR.services_by_name['TraceSegmentReportService'] = _TRACESEGMENTREPORTSERVICE

# @@protoc_insertion_point(module_scope)
