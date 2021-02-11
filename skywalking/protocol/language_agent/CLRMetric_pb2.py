# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: language-agent/CLRMetric.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Common_pb2 as common_dot_Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='language-agent/CLRMetric.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n3org.apache.skywalking.apm.network.language.agent.v3P\001Z$skywalking/network/language/agent/v3\252\002\032SkyWalking.NetworkProtocol',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1elanguage-agent/CLRMetric.proto\x1a\x13\x63ommon/Common.proto\"\\\n\x13\x43LRMetricCollection\x12\x1b\n\x07metrics\x18\x01 \x03(\x0b\x32\n.CLRMetric\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x17\n\x0fserviceInstance\x18\x03 \x01(\t\"\\\n\tCLRMetric\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x11\n\x03\x63pu\x18\x02 \x01(\x0b\x32\x04.CPU\x12\x12\n\x02gc\x18\x03 \x01(\x0b\x32\x06.ClrGC\x12\x1a\n\x06thread\x18\x04 \x01(\x0b\x32\n.ClrThread\"i\n\x05\x43lrGC\x12\x18\n\x10Gen0CollectCount\x18\x01 \x01(\x03\x12\x18\n\x10Gen1CollectCount\x18\x02 \x01(\x03\x12\x18\n\x10Gen2CollectCount\x18\x03 \x01(\x03\x12\x12\n\nHeapMemory\x18\x04 \x01(\x03\"\x8f\x01\n\tClrThread\x12&\n\x1e\x41vailableCompletionPortThreads\x18\x01 \x01(\x05\x12\x1e\n\x16\x41vailableWorkerThreads\x18\x02 \x01(\x05\x12 \n\x18MaxCompletionPortThreads\x18\x03 \x01(\x05\x12\x18\n\x10MaxWorkerThreads\x18\x04 \x01(\x05\x32\x46\n\x16\x43LRMetricReportService\x12,\n\x07\x63ollect\x12\x14.CLRMetricCollection\x1a\t.Commands\"\x00\x42z\n3org.apache.skywalking.apm.network.language.agent.v3P\x01Z$skywalking/network/language/agent/v3\xaa\x02\x1aSkyWalking.NetworkProtocolb\x06proto3'
  ,
  dependencies=[common_dot_Common__pb2.DESCRIPTOR,])




_CLRMETRICCOLLECTION = _descriptor.Descriptor(
  name='CLRMetricCollection',
  full_name='CLRMetricCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='CLRMetricCollection.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service', full_name='CLRMetricCollection.service', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceInstance', full_name='CLRMetricCollection.serviceInstance', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=55,
  serialized_end=147,
)


_CLRMETRIC = _descriptor.Descriptor(
  name='CLRMetric',
  full_name='CLRMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='CLRMetric.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpu', full_name='CLRMetric.cpu', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gc', full_name='CLRMetric.gc', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='thread', full_name='CLRMetric.thread', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=149,
  serialized_end=241,
)


_CLRGC = _descriptor.Descriptor(
  name='ClrGC',
  full_name='ClrGC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Gen0CollectCount', full_name='ClrGC.Gen0CollectCount', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Gen1CollectCount', full_name='ClrGC.Gen1CollectCount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Gen2CollectCount', full_name='ClrGC.Gen2CollectCount', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='HeapMemory', full_name='ClrGC.HeapMemory', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=243,
  serialized_end=348,
)


_CLRTHREAD = _descriptor.Descriptor(
  name='ClrThread',
  full_name='ClrThread',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='AvailableCompletionPortThreads', full_name='ClrThread.AvailableCompletionPortThreads', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='AvailableWorkerThreads', full_name='ClrThread.AvailableWorkerThreads', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MaxCompletionPortThreads', full_name='ClrThread.MaxCompletionPortThreads', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MaxWorkerThreads', full_name='ClrThread.MaxWorkerThreads', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=351,
  serialized_end=494,
)

_CLRMETRICCOLLECTION.fields_by_name['metrics'].message_type = _CLRMETRIC
_CLRMETRIC.fields_by_name['cpu'].message_type = common_dot_Common__pb2._CPU
_CLRMETRIC.fields_by_name['gc'].message_type = _CLRGC
_CLRMETRIC.fields_by_name['thread'].message_type = _CLRTHREAD
DESCRIPTOR.message_types_by_name['CLRMetricCollection'] = _CLRMETRICCOLLECTION
DESCRIPTOR.message_types_by_name['CLRMetric'] = _CLRMETRIC
DESCRIPTOR.message_types_by_name['ClrGC'] = _CLRGC
DESCRIPTOR.message_types_by_name['ClrThread'] = _CLRTHREAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CLRMetricCollection = _reflection.GeneratedProtocolMessageType('CLRMetricCollection', (_message.Message,), {
  'DESCRIPTOR' : _CLRMETRICCOLLECTION,
  '__module__' : 'language_agent.CLRMetric_pb2'
  # @@protoc_insertion_point(class_scope:CLRMetricCollection)
  })
_sym_db.RegisterMessage(CLRMetricCollection)

CLRMetric = _reflection.GeneratedProtocolMessageType('CLRMetric', (_message.Message,), {
  'DESCRIPTOR' : _CLRMETRIC,
  '__module__' : 'language_agent.CLRMetric_pb2'
  # @@protoc_insertion_point(class_scope:CLRMetric)
  })
_sym_db.RegisterMessage(CLRMetric)

ClrGC = _reflection.GeneratedProtocolMessageType('ClrGC', (_message.Message,), {
  'DESCRIPTOR' : _CLRGC,
  '__module__' : 'language_agent.CLRMetric_pb2'
  # @@protoc_insertion_point(class_scope:ClrGC)
  })
_sym_db.RegisterMessage(ClrGC)

ClrThread = _reflection.GeneratedProtocolMessageType('ClrThread', (_message.Message,), {
  'DESCRIPTOR' : _CLRTHREAD,
  '__module__' : 'language_agent.CLRMetric_pb2'
  # @@protoc_insertion_point(class_scope:ClrThread)
  })
_sym_db.RegisterMessage(ClrThread)


DESCRIPTOR._options = None

_CLRMETRICREPORTSERVICE = _descriptor.ServiceDescriptor(
  name='CLRMetricReportService',
  full_name='CLRMetricReportService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=496,
  serialized_end=566,
  methods=[
  _descriptor.MethodDescriptor(
    name='collect',
    full_name='CLRMetricReportService.collect',
    index=0,
    containing_service=None,
    input_type=_CLRMETRICCOLLECTION,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLRMETRICREPORTSERVICE)

DESCRIPTOR.services_by_name['CLRMetricReportService'] = _CLRMETRICREPORTSERVICE

# @@protoc_insertion_point(module_scope)
