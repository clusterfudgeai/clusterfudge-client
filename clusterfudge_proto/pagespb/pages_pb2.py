# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pagespb/pages.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13pagespb/pages.proto\x12\x0c\x63lusterfudge\x1a\x1egoogle/protobuf/wrappers.proto\"d\n\x04Page\x12\x30\n\x0bpage_number\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12*\n\x05limit\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\"\"\n\x0bPageDetails\x12\x13\n\x0btotal_pages\x18\x01 \x01(\x05\x42/Z-github.com/clusterfudgeai/fudge/proto/pagespbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pagespb.pages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/clusterfudgeai/fudge/proto/pagespb'
  _globals['_PAGE']._serialized_start=69
  _globals['_PAGE']._serialized_end=169
  _globals['_PAGEDETAILS']._serialized_start=171
  _globals['_PAGEDETAILS']._serialized_end=205
# @@protoc_insertion_point(module_scope)