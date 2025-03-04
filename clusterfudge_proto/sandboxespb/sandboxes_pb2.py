# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sandboxespb/sandboxes.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bsandboxespb/sandboxes.proto\x12\x0bsandboxespb\x1a\x1fgoogle/protobuf/timestamp.proto\"J\n\x14\x43reateSandboxRequest\x12\x11\n\timage_tag\x18\x01 \x01(\t\x12\x1f\n\x17sidecar_pod_definitions\x18\x02 \x03(\t\">\n\x15\x43reateSandboxResponse\x12%\n\x07sandbox\x18\x01 \x01(\x0b\x32\x14.sandboxespb.Sandbox\"\x16\n\x14ListSandboxesRequest\"@\n\x15ListSandboxesResponse\x12\'\n\tsandboxes\x18\x01 \x03(\x0b\x32\x14.sandboxespb.Sandbox\"*\n\x14\x44\x65leteSandboxRequest\x12\x12\n\nmachine_id\x18\x01 \x01(\t\"\x17\n\x15\x44\x65leteSandboxResponse\"\xd7\x01\n\x07Sandbox\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x05state\x18\x03 \x01(\x0e\x32\x1a.sandboxespb.Sandbox.State\"e\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x11\n\rSTATE_PENDING\x10\x01\x12\x19\n\x15STATE_RUNNING_HAPPILY\x10\x02\x12\x17\n\x13STATE_RUNNING_SADLY\x10\x03\"X\n\x18\x43laudeComputerUseRequest\x12\x12\n\nmachine_id\x18\x01 \x01(\t\x12(\n raw_anthropic_beta_content_block\x18\x02 \x01(\x0c\"I\n\x19\x43laudeComputerUseResponse\x12,\n$raw_anthropic_beta_tool_result_block\x18\x01 \x01(\x0c\"\xa1\x02\n ClaudeComputerUseRequestResponse\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x12\n\nmachine_id\x18\x03 \x01(\t\x12\x35\n\x11request_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n raw_anthropic_beta_content_block\x18\x05 \x01(\x0c\x12\x36\n\x12response_timestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n$raw_anthropic_beta_tool_result_block\x18\x07 \x01(\x0c\x32\xff\x02\n\tSandboxes\x12X\n\rCreateSandbox\x12!.sandboxespb.CreateSandboxRequest\x1a\".sandboxespb.CreateSandboxResponse\"\x00\x12X\n\rListSandboxes\x12!.sandboxespb.ListSandboxesRequest\x1a\".sandboxespb.ListSandboxesResponse\"\x00\x12X\n\rDeleteSandbox\x12!.sandboxespb.DeleteSandboxRequest\x1a\".sandboxespb.DeleteSandboxResponse\"\x00\x12\x64\n\x11\x43laudeComputerUse\x12%.sandboxespb.ClaudeComputerUseRequest\x1a&.sandboxespb.ClaudeComputerUseResponse\"\x00\x42\x33Z1github.com/clusterfudgeai/fudge/proto/sandboxespbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sandboxespb.sandboxes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/clusterfudgeai/fudge/proto/sandboxespb'
  _globals['_CREATESANDBOXREQUEST']._serialized_start=77
  _globals['_CREATESANDBOXREQUEST']._serialized_end=151
  _globals['_CREATESANDBOXRESPONSE']._serialized_start=153
  _globals['_CREATESANDBOXRESPONSE']._serialized_end=215
  _globals['_LISTSANDBOXESREQUEST']._serialized_start=217
  _globals['_LISTSANDBOXESREQUEST']._serialized_end=239
  _globals['_LISTSANDBOXESRESPONSE']._serialized_start=241
  _globals['_LISTSANDBOXESRESPONSE']._serialized_end=305
  _globals['_DELETESANDBOXREQUEST']._serialized_start=307
  _globals['_DELETESANDBOXREQUEST']._serialized_end=349
  _globals['_DELETESANDBOXRESPONSE']._serialized_start=351
  _globals['_DELETESANDBOXRESPONSE']._serialized_end=374
  _globals['_SANDBOX']._serialized_start=377
  _globals['_SANDBOX']._serialized_end=592
  _globals['_SANDBOX_STATE']._serialized_start=491
  _globals['_SANDBOX_STATE']._serialized_end=592
  _globals['_CLAUDECOMPUTERUSEREQUEST']._serialized_start=594
  _globals['_CLAUDECOMPUTERUSEREQUEST']._serialized_end=682
  _globals['_CLAUDECOMPUTERUSERESPONSE']._serialized_start=684
  _globals['_CLAUDECOMPUTERUSERESPONSE']._serialized_end=757
  _globals['_CLAUDECOMPUTERUSEREQUESTRESPONSE']._serialized_start=760
  _globals['_CLAUDECOMPUTERUSEREQUESTRESPONSE']._serialized_end=1049
  _globals['_SANDBOXES']._serialized_start=1052
  _globals['_SANDBOXES']._serialized_end=1435
# @@protoc_insertion_point(module_scope)
