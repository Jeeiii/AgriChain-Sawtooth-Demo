# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: property.proto

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
  name='property.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0eproperty.proto\"\x98\x01\n\x08Property\x12\x10\n\x08\x62\x61tch_id\x18\x01 \x01(\t\x12$\n\x04type\x18\x02 \x01(\x0e\x32\x16.Property.PropertyType\x12\x14\n\x0c\x63urrent_page\x18\x03 \x01(\r\x12\x0f\n\x07wrapped\x18\x04 \x01(\x08\"-\n\x0cPropertyType\x12\x0c\n\x08LOCATION\x10\x00\x12\x0f\n\x0bTEMPERATURE\x10\x01\"/\n\x11PropertyContainer\x12\x1a\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\t.Property\"\xa1\x02\n\x0cPropertyPage\x12$\n\x04type\x18\x01 \x01(\x0e\x32\x16.Property.PropertyType\x12\x10\n\x08\x62\x61tch_id\x18\x02 \x01(\t\x12\x34\n\x0freported_values\x18\x03 \x03(\x0b\x32\x1b.PropertyPage.ReportedValue\x1ar\n\rReportedValue\x12\x0f\n\x07pub_key\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12(\n\x08position\x18\x03 \x01(\x0b\x32\x16.PropertyPage.Location\x12\x13\n\x0btemperature\x18\x04 \x01(\x02\x1a/\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x12\x12\x11\n\tlongitude\x18\x02 \x01(\x12\"7\n\x15PropertyPageContainer\x12\x1e\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\r.PropertyPageb\x06proto3')
)



_PROPERTY_PROPERTYTYPE = _descriptor.EnumDescriptor(
  name='PropertyType',
  full_name='Property.PropertyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOCATION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPERATURE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=126,
  serialized_end=171,
)
_sym_db.RegisterEnumDescriptor(_PROPERTY_PROPERTYTYPE)


_PROPERTY = _descriptor.Descriptor(
  name='Property',
  full_name='Property',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_id', full_name='Property.batch_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Property.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_page', full_name='Property.current_page', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wrapped', full_name='Property.wrapped', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROPERTY_PROPERTYTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=171,
)


_PROPERTYCONTAINER = _descriptor.Descriptor(
  name='PropertyContainer',
  full_name='PropertyContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='PropertyContainer.entries', index=0,
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
  serialized_start=173,
  serialized_end=220,
)


_PROPERTYPAGE_REPORTEDVALUE = _descriptor.Descriptor(
  name='ReportedValue',
  full_name='PropertyPage.ReportedValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='PropertyPage.ReportedValue.pub_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='PropertyPage.ReportedValue.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='PropertyPage.ReportedValue.position', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='PropertyPage.ReportedValue.temperature', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=463,
)

_PROPERTYPAGE_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='PropertyPage.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='PropertyPage.Location.latitude', index=0,
      number=1, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='PropertyPage.Location.longitude', index=1,
      number=2, type=18, cpp_type=2, label=1,
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
  serialized_start=465,
  serialized_end=512,
)

_PROPERTYPAGE = _descriptor.Descriptor(
  name='PropertyPage',
  full_name='PropertyPage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='PropertyPage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch_id', full_name='PropertyPage.batch_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reported_values', full_name='PropertyPage.reported_values', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PROPERTYPAGE_REPORTEDVALUE, _PROPERTYPAGE_LOCATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=512,
)


_PROPERTYPAGECONTAINER = _descriptor.Descriptor(
  name='PropertyPageContainer',
  full_name='PropertyPageContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='PropertyPageContainer.entries', index=0,
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
  serialized_start=514,
  serialized_end=569,
)

_PROPERTY.fields_by_name['type'].enum_type = _PROPERTY_PROPERTYTYPE
_PROPERTY_PROPERTYTYPE.containing_type = _PROPERTY
_PROPERTYCONTAINER.fields_by_name['entries'].message_type = _PROPERTY
_PROPERTYPAGE_REPORTEDVALUE.fields_by_name['position'].message_type = _PROPERTYPAGE_LOCATION
_PROPERTYPAGE_REPORTEDVALUE.containing_type = _PROPERTYPAGE
_PROPERTYPAGE_LOCATION.containing_type = _PROPERTYPAGE
_PROPERTYPAGE.fields_by_name['type'].enum_type = _PROPERTY_PROPERTYTYPE
_PROPERTYPAGE.fields_by_name['reported_values'].message_type = _PROPERTYPAGE_REPORTEDVALUE
_PROPERTYPAGECONTAINER.fields_by_name['entries'].message_type = _PROPERTYPAGE
DESCRIPTOR.message_types_by_name['Property'] = _PROPERTY
DESCRIPTOR.message_types_by_name['PropertyContainer'] = _PROPERTYCONTAINER
DESCRIPTOR.message_types_by_name['PropertyPage'] = _PROPERTYPAGE
DESCRIPTOR.message_types_by_name['PropertyPageContainer'] = _PROPERTYPAGECONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Property = _reflection.GeneratedProtocolMessageType('Property', (_message.Message,), dict(
  DESCRIPTOR = _PROPERTY,
  __module__ = 'property_pb2'
  # @@protoc_insertion_point(class_scope:Property)
  ))
_sym_db.RegisterMessage(Property)

PropertyContainer = _reflection.GeneratedProtocolMessageType('PropertyContainer', (_message.Message,), dict(
  DESCRIPTOR = _PROPERTYCONTAINER,
  __module__ = 'property_pb2'
  # @@protoc_insertion_point(class_scope:PropertyContainer)
  ))
_sym_db.RegisterMessage(PropertyContainer)

PropertyPage = _reflection.GeneratedProtocolMessageType('PropertyPage', (_message.Message,), dict(

  ReportedValue = _reflection.GeneratedProtocolMessageType('ReportedValue', (_message.Message,), dict(
    DESCRIPTOR = _PROPERTYPAGE_REPORTEDVALUE,
    __module__ = 'property_pb2'
    # @@protoc_insertion_point(class_scope:PropertyPage.ReportedValue)
    ))
  ,

  Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
    DESCRIPTOR = _PROPERTYPAGE_LOCATION,
    __module__ = 'property_pb2'
    # @@protoc_insertion_point(class_scope:PropertyPage.Location)
    ))
  ,
  DESCRIPTOR = _PROPERTYPAGE,
  __module__ = 'property_pb2'
  # @@protoc_insertion_point(class_scope:PropertyPage)
  ))
_sym_db.RegisterMessage(PropertyPage)
_sym_db.RegisterMessage(PropertyPage.ReportedValue)
_sym_db.RegisterMessage(PropertyPage.Location)

PropertyPageContainer = _reflection.GeneratedProtocolMessageType('PropertyPageContainer', (_message.Message,), dict(
  DESCRIPTOR = _PROPERTYPAGECONTAINER,
  __module__ = 'property_pb2'
  # @@protoc_insertion_point(class_scope:PropertyPageContainer)
  ))
_sym_db.RegisterMessage(PropertyPageContainer)


# @@protoc_insertion_point(module_scope)
