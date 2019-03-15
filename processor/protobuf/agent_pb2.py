# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent.proto

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
  name='agent.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0b\x61gent.proto\"\xdc\x01\n\x05\x41gent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x12\n\npublic_key\x18\x03 \x01(\t\x12\x1e\n\x04type\x18\x04 \x01(\x0e\x32\x10.Agent.AgentType\x12\x12\n\nauthorizer\x18\x05 \x01(\t\x12\x0f\n\x07\x63ompany\x18\x06 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x07 \x01(\x08\x12\x11\n\ttimestamp\x18\x08 \x01(\x04\"<\n\tAgentType\x12\x12\n\x0e\x42USINESS_ADMIN\x10\x00\x12\r\n\tCERTIFIER\x10\x01\x12\x0c\n\x08OPERATOR\x10\x02\")\n\x0e\x41gentContainer\x12\x17\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x06.Agentb\x06proto3')
)



_AGENT_AGENTTYPE = _descriptor.EnumDescriptor(
  name='AgentType',
  full_name='Agent.AgentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUSINESS_ADMIN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CERTIFIER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATOR', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=176,
  serialized_end=236,
)
_sym_db.RegisterEnumDescriptor(_AGENT_AGENTTYPE)


_AGENT = _descriptor.Descriptor(
  name='Agent',
  full_name='Agent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Agent.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Agent.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='Agent.public_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Agent.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authorizer', full_name='Agent.authorizer', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='company', full_name='Agent.company', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='Agent.enabled', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Agent.timestamp', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AGENT_AGENTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=236,
)


_AGENTCONTAINER = _descriptor.Descriptor(
  name='AgentContainer',
  full_name='AgentContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='AgentContainer.entries', index=0,
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
  serialized_start=238,
  serialized_end=279,
)

_AGENT.fields_by_name['type'].enum_type = _AGENT_AGENTTYPE
_AGENT_AGENTTYPE.containing_type = _AGENT
_AGENTCONTAINER.fields_by_name['entries'].message_type = _AGENT
DESCRIPTOR.message_types_by_name['Agent'] = _AGENT
DESCRIPTOR.message_types_by_name['AgentContainer'] = _AGENTCONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Agent = _reflection.GeneratedProtocolMessageType('Agent', (_message.Message,), dict(
  DESCRIPTOR = _AGENT,
  __module__ = 'agent_pb2'
  # @@protoc_insertion_point(class_scope:Agent)
  ))
_sym_db.RegisterMessage(Agent)

AgentContainer = _reflection.GeneratedProtocolMessageType('AgentContainer', (_message.Message,), dict(
  DESCRIPTOR = _AGENTCONTAINER,
  __module__ = 'agent_pb2'
  # @@protoc_insertion_point(class_scope:AgentContainer)
  ))
_sym_db.RegisterMessage(AgentContainer)


# @@protoc_insertion_point(module_scope)
