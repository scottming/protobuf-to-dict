# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sample.proto',
  package='tests',
  syntax='proto3',
  serialized_pb=_b('\n\x0csample.proto\x12\x05tests\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/protobuf/descriptor.proto\"\xd4\x05\n\x0eMessageOfTypes\x12\x0c\n\x04\x64ubl\x18\x01 \x01(\x01\x12\x0c\n\x04\x66lot\x18\x02 \x01(\x02\x12\x0b\n\x03i32\x18\x03 \x01(\x05\x12\x0b\n\x03i64\x18\x04 \x01(\x03\x12\x0c\n\x04ui32\x18\x05 \x01(\r\x12\x0c\n\x04ui64\x18\x06 \x01(\x04\x12\x0c\n\x04si32\x18\x07 \x01(\x11\x12\x0c\n\x04si64\x18\x08 \x01(\x12\x12\x0b\n\x03\x66\x33\x32\x18\t \x01(\x07\x12\x0b\n\x03\x66\x36\x34\x18\n \x01(\x06\x12\x0c\n\x04sf32\x18\x0b \x01(\x0f\x12\x0c\n\x04sf64\x18\x0c \x01(\x10\x12\x0b\n\x03\x62ol\x18\r \x01(\x08\x12\r\n\x05strng\x18\x0e \x01(\t\x12\x0c\n\x04\x62yts\x18\x0f \x01(\x0c\x12\x30\n\x06nested\x18\x10 \x01(\x0b\x32 .tests.MessageOfTypes.NestedType\x12\'\n\x03\x65nm\x18\x11 \x01(\x0e\x32\x1a.tests.MessageOfTypes.Enum\x12\x38\n\x0enestedRepeated\x18\x12 \x03(\x0b\x32 .tests.MessageOfTypes.NestedType\x12/\n\x0b\x65nmRepeated\x18\x13 \x03(\x0e\x32\x1a.tests.MessageOfTypes.Enum\x12\x37\n\tsimpleMap\x18\x14 \x03(\x0b\x32$.tests.MessageOfTypes.SimpleMapEntry\x12\x37\n\tnestedMap\x18\x15 \x03(\x0b\x32$.tests.MessageOfTypes.NestedMapEntry\x1a\x30\n\x0eSimpleMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1aR\n\x0eNestedMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .tests.MessageOfTypes.NestedType:\x02\x38\x01\x1a\x19\n\nNestedType\x12\x0b\n\x03req\x18\x01 \x01(\t\"\x1b\n\x04\x45num\x12\x05\n\x01\x41\x10\x00\x12\x05\n\x01\x42\x10\x01\x12\x05\n\x01\x43\x10\x02\"z\n\x03Obj\x12\x10\n\x02id\x18\x01 \x01(\x05\x42\x04\xa0\xb5\x18\x01\x12\x0f\n\x07item_id\x18\x02 \x01(\t\x12\x31\n\rtransacted_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1d\n\x06status\x18\x05 \x01(\x0e\x32\r.tests.Status\"#\n\x04Objs\x12\x1b\n\x07objects\x18\x01 \x03(\x0b\x32\n.tests.Obj*\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01:4\n\x0bis_optional\x12\x1d.google.protobuf.FieldOptions\x18\xd4\x86\x03 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='tests.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=978,
  serialized_end=1005,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
OK = 0
ERROR = 1

IS_OPTIONAL_FIELD_NUMBER = 50004
is_optional = _descriptor.FieldDescriptor(
  name='is_optional', full_name='tests.is_optional', index=0,
  number=50004, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)

_MESSAGEOFTYPES_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='tests.MessageOfTypes.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='A', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=788,
  serialized_end=815,
)
_sym_db.RegisterEnumDescriptor(_MESSAGEOFTYPES_ENUM)


_MESSAGEOFTYPES_SIMPLEMAPENTRY = _descriptor.Descriptor(
  name='SimpleMapEntry',
  full_name='tests.MessageOfTypes.SimpleMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tests.MessageOfTypes.SimpleMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='tests.MessageOfTypes.SimpleMapEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=627,
  serialized_end=675,
)

_MESSAGEOFTYPES_NESTEDMAPENTRY = _descriptor.Descriptor(
  name='NestedMapEntry',
  full_name='tests.MessageOfTypes.NestedMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tests.MessageOfTypes.NestedMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='tests.MessageOfTypes.NestedMapEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=677,
  serialized_end=759,
)

_MESSAGEOFTYPES_NESTEDTYPE = _descriptor.Descriptor(
  name='NestedType',
  full_name='tests.MessageOfTypes.NestedType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req', full_name='tests.MessageOfTypes.NestedType.req', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=761,
  serialized_end=786,
)

_MESSAGEOFTYPES = _descriptor.Descriptor(
  name='MessageOfTypes',
  full_name='tests.MessageOfTypes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dubl', full_name='tests.MessageOfTypes.dubl', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flot', full_name='tests.MessageOfTypes.flot', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i32', full_name='tests.MessageOfTypes.i32', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i64', full_name='tests.MessageOfTypes.i64', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ui32', full_name='tests.MessageOfTypes.ui32', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ui64', full_name='tests.MessageOfTypes.ui64', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='si32', full_name='tests.MessageOfTypes.si32', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='si64', full_name='tests.MessageOfTypes.si64', index=7,
      number=8, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f32', full_name='tests.MessageOfTypes.f32', index=8,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f64', full_name='tests.MessageOfTypes.f64', index=9,
      number=10, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sf32', full_name='tests.MessageOfTypes.sf32', index=10,
      number=11, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sf64', full_name='tests.MessageOfTypes.sf64', index=11,
      number=12, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bol', full_name='tests.MessageOfTypes.bol', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strng', full_name='tests.MessageOfTypes.strng', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='byts', full_name='tests.MessageOfTypes.byts', index=14,
      number=15, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nested', full_name='tests.MessageOfTypes.nested', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enm', full_name='tests.MessageOfTypes.enm', index=16,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nestedRepeated', full_name='tests.MessageOfTypes.nestedRepeated', index=17,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enmRepeated', full_name='tests.MessageOfTypes.enmRepeated', index=18,
      number=19, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simpleMap', full_name='tests.MessageOfTypes.simpleMap', index=19,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nestedMap', full_name='tests.MessageOfTypes.nestedMap', index=20,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MESSAGEOFTYPES_SIMPLEMAPENTRY, _MESSAGEOFTYPES_NESTEDMAPENTRY, _MESSAGEOFTYPES_NESTEDTYPE, ],
  enum_types=[
    _MESSAGEOFTYPES_ENUM,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=815,
)


_OBJ = _descriptor.Descriptor(
  name='Obj',
  full_name='tests.Obj',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tests.Obj.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\240\265\030\001'))),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='tests.Obj.item_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transacted_at', full_name='tests.Obj.transacted_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='tests.Obj.status', index=3,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=817,
  serialized_end=939,
)


_OBJS = _descriptor.Descriptor(
  name='Objs',
  full_name='tests.Objs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objects', full_name='tests.Objs.objects', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=941,
  serialized_end=976,
)

_MESSAGEOFTYPES_SIMPLEMAPENTRY.containing_type = _MESSAGEOFTYPES
_MESSAGEOFTYPES_NESTEDMAPENTRY.fields_by_name['value'].message_type = _MESSAGEOFTYPES_NESTEDTYPE
_MESSAGEOFTYPES_NESTEDMAPENTRY.containing_type = _MESSAGEOFTYPES
_MESSAGEOFTYPES_NESTEDTYPE.containing_type = _MESSAGEOFTYPES
_MESSAGEOFTYPES.fields_by_name['nested'].message_type = _MESSAGEOFTYPES_NESTEDTYPE
_MESSAGEOFTYPES.fields_by_name['enm'].enum_type = _MESSAGEOFTYPES_ENUM
_MESSAGEOFTYPES.fields_by_name['nestedRepeated'].message_type = _MESSAGEOFTYPES_NESTEDTYPE
_MESSAGEOFTYPES.fields_by_name['enmRepeated'].enum_type = _MESSAGEOFTYPES_ENUM
_MESSAGEOFTYPES.fields_by_name['simpleMap'].message_type = _MESSAGEOFTYPES_SIMPLEMAPENTRY
_MESSAGEOFTYPES.fields_by_name['nestedMap'].message_type = _MESSAGEOFTYPES_NESTEDMAPENTRY
_MESSAGEOFTYPES_ENUM.containing_type = _MESSAGEOFTYPES
_OBJ.fields_by_name['transacted_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OBJ.fields_by_name['status'].enum_type = _STATUS
_OBJS.fields_by_name['objects'].message_type = _OBJ
DESCRIPTOR.message_types_by_name['MessageOfTypes'] = _MESSAGEOFTYPES
DESCRIPTOR.message_types_by_name['Obj'] = _OBJ
DESCRIPTOR.message_types_by_name['Objs'] = _OBJS
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
DESCRIPTOR.extensions_by_name['is_optional'] = is_optional
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageOfTypes = _reflection.GeneratedProtocolMessageType('MessageOfTypes', (_message.Message,), dict(

  SimpleMapEntry = _reflection.GeneratedProtocolMessageType('SimpleMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _MESSAGEOFTYPES_SIMPLEMAPENTRY,
    __module__ = 'sample_pb2'
    # @@protoc_insertion_point(class_scope:tests.MessageOfTypes.SimpleMapEntry)
    ))
  ,

  NestedMapEntry = _reflection.GeneratedProtocolMessageType('NestedMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _MESSAGEOFTYPES_NESTEDMAPENTRY,
    __module__ = 'sample_pb2'
    # @@protoc_insertion_point(class_scope:tests.MessageOfTypes.NestedMapEntry)
    ))
  ,

  NestedType = _reflection.GeneratedProtocolMessageType('NestedType', (_message.Message,), dict(
    DESCRIPTOR = _MESSAGEOFTYPES_NESTEDTYPE,
    __module__ = 'sample_pb2'
    # @@protoc_insertion_point(class_scope:tests.MessageOfTypes.NestedType)
    ))
  ,
  DESCRIPTOR = _MESSAGEOFTYPES,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:tests.MessageOfTypes)
  ))
_sym_db.RegisterMessage(MessageOfTypes)
_sym_db.RegisterMessage(MessageOfTypes.SimpleMapEntry)
_sym_db.RegisterMessage(MessageOfTypes.NestedMapEntry)
_sym_db.RegisterMessage(MessageOfTypes.NestedType)

Obj = _reflection.GeneratedProtocolMessageType('Obj', (_message.Message,), dict(
  DESCRIPTOR = _OBJ,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:tests.Obj)
  ))
_sym_db.RegisterMessage(Obj)

Objs = _reflection.GeneratedProtocolMessageType('Objs', (_message.Message,), dict(
  DESCRIPTOR = _OBJS,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:tests.Objs)
  ))
_sym_db.RegisterMessage(Objs)

google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(is_optional)

_MESSAGEOFTYPES_SIMPLEMAPENTRY.has_options = True
_MESSAGEOFTYPES_SIMPLEMAPENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_MESSAGEOFTYPES_NESTEDMAPENTRY.has_options = True
_MESSAGEOFTYPES_NESTEDMAPENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_OBJ.fields_by_name['id'].has_options = True
_OBJ.fields_by_name['id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\240\265\030\001'))
# @@protoc_insertion_point(module_scope)
