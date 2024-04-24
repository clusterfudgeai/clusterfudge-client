# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exec/exec.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from ..resources import resources_pb2 as resources_dot_resources__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x65xec/exec.proto\x12\x0c\x63lusterfudge\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x19resources/resources.proto\"\x91\x01\n\x0f\x43ommandResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x30\n\x0crequested_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x07\x63ommand\x18\x03 \x01(\x0e\x32\x19.clusterfudge.CommandType\x12\x14\n\x0creference_id\x18\x04 \x01(\t\"\x1f\n\x11GetCommandRequest\x12\n\n\x02id\x18\x01 \x01(\t\"j\n\x14\x43reateCommandRequest\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12*\n\x07\x63ommand\x18\x02 \x01(\x0e\x32\x19.clusterfudge.CommandType\x12\x14\n\x0creference_id\x18\x03 \x01(\t\"\x17\n\x15\x43reateCommandResponse\"Y\n\x18\x42ulkCreateCommandRequest\x12\x11\n\thostnames\x18\x01 \x03(\t\x12*\n\x07\x63ommand\x18\x02 \x01(\x0e\x32\x19.clusterfudge.CommandType\"\x1b\n\x19\x42ulkCreateCommandResponse\"\xe8\x01\n\x13ListCommandsRequest\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12)\n\x05state\x18\x02 \x01(\x0e\x32\x1a.clusterfudge.CommandState\x12\x11\n\thostnames\x18\x03 \x03(\t\x12*\n\x06states\x18\x04 \x03(\x0e\x32\x1a.clusterfudge.CommandState\x12(\n\x05types\x18\x05 \x03(\x0e\x32\x19.clusterfudge.CommandType\x12\x15\n\rreference_ids\x18\x06 \x03(\t\x12\x14\n\x0crequested_by\x18\x07 \x03(\t\"?\n\x14ListCommandsResponse\x12\'\n\x08\x63ommands\x18\x01 \x03(\x0b\x32\x15.clusterfudge.Command\">\n\x14UpdateCommandRequest\x12&\n\x07\x63ommand\x18\x01 \x01(\x0b\x32\x15.clusterfudge.Command\"\xe6\x05\n\x07\x43ommand\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x14\n\x0crequested_by\x18\x04 \x01(\t\x12\x30\n\x0crequested_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0f\x61\x63knowledged_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x07\x63ommand\x18\x07 \x01(\x0e\x32\x19.clusterfudge.CommandType\x12\x14\n\x0creference_id\x18\x08 \x01(\t\x12\x38\n\x14\x65xecution_started_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16\x65xecution_completed_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08\x65xec_err\x18\x0b \x01(\t\x12.\n\texit_code\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12)\n\x05state\x18\r \x01(\x0e\x32\x1a.clusterfudge.CommandState\x12\x0b\n\x03\x65nv\x18\x0e \x03(\t\x12(\n\x03pid\x18\x0f \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x10\n\x08\x63md_line\x18\x10 \x03(\t\x12\x31\n\x10resource_request\x18\x11 \x01(\x0b\x32\x17.clusterfudge.Resources\x12\x0e\n\x06zip_id\x18\x12 \x01(\t\x12\x10\n\x08git_repo\x18\x13 \x01(\t\x12\x12\n\ngit_branch\x18\x14 \x01(\t\x12\x10\n\x08job_name\x18\x15 \x01(\t\x12\x30\n\x0cserver_state\x18\x16 \x01(\x0e\x32\x1a.clusterfudge.CommandState\x12\x12\n\ngit_commit\x18\x17 \x01(\t*\x9a\x01\n\x0b\x43ommandType\x12\x18\n\x14\x43OMMAND_TYPE_UNKNOWN\x10\x00\x12\x1d\n\x19\x43OMMAND_TYPE_AGENT_UPDATE\x10\x01\x12\"\n\x1e\x43OMMAND_TYPE_NVIDIA_BUG_REPORT\x10\x02\x12\x17\n\x13\x43OMMAND_TYPE_LAUNCH\x10\x03\x12\x15\n\x11\x43OMMAND_TYPE_KILL\x10\x04*\x91\x02\n\x0c\x43ommandState\x12\x19\n\x15\x43OMMAND_STATE_UNKNOWN\x10\x00\x12 \n\x1c\x43OMMAND_STATE_UNACKNOWLEDGED\x10\x01\x12\x1e\n\x1a\x43OMMAND_STATE_ACKNOWLEDGED\x10\x02\x12\x19\n\x15\x43OMMAND_STATE_RUNNING\x10\x03\x12\x1b\n\x17\x43OMMAND_STATE_SUCCEEDED\x10\x04\x12\x18\n\x14\x43OMMAND_STATE_FAILED\x10\x05\x12\x18\n\x14\x43OMMAND_STATE_KILLED\x10\x06\x12\x1b\n\x17\x43OMMAND_STATE_CANCELLED\x10\x07\x12\x1b\n\x17\x43OMMAND_STATE_TIMED_OUT\x10\x08\x32\xab\x03\n\x04\x45xec\x12\x66\n\x11\x42ulkCreateCommand\x12&.clusterfudge.BulkCreateCommandRequest\x1a\'.clusterfudge.BulkCreateCommandResponse\"\x00\x12L\n\rCreateCommand\x12\".clusterfudge.CreateCommandRequest\x1a\x15.clusterfudge.Command\"\x00\x12\x46\n\nGetCommand\x12\x1f.clusterfudge.GetCommandRequest\x1a\x15.clusterfudge.Command\"\x00\x12W\n\x0cListCommands\x12!.clusterfudge.ListCommandsRequest\x1a\".clusterfudge.ListCommandsResponse\"\x00\x12L\n\rUpdateCommand\x12\".clusterfudge.UpdateCommandRequest\x1a\x15.clusterfudge.Command\"\x00\x42\x31Z/github.com/clusterfudgeai/fudge/proto/exec;execb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exec.exec_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/clusterfudgeai/fudge/proto/exec;exec'
  _COMMANDTYPE._serialized_start=1669
  _COMMANDTYPE._serialized_end=1823
  _COMMANDSTATE._serialized_start=1826
  _COMMANDSTATE._serialized_end=2099
  _COMMANDRESPONSE._serialized_start=126
  _COMMANDRESPONSE._serialized_end=271
  _GETCOMMANDREQUEST._serialized_start=273
  _GETCOMMANDREQUEST._serialized_end=304
  _CREATECOMMANDREQUEST._serialized_start=306
  _CREATECOMMANDREQUEST._serialized_end=412
  _CREATECOMMANDRESPONSE._serialized_start=414
  _CREATECOMMANDRESPONSE._serialized_end=437
  _BULKCREATECOMMANDREQUEST._serialized_start=439
  _BULKCREATECOMMANDREQUEST._serialized_end=528
  _BULKCREATECOMMANDRESPONSE._serialized_start=530
  _BULKCREATECOMMANDRESPONSE._serialized_end=557
  _LISTCOMMANDSREQUEST._serialized_start=560
  _LISTCOMMANDSREQUEST._serialized_end=792
  _LISTCOMMANDSRESPONSE._serialized_start=794
  _LISTCOMMANDSRESPONSE._serialized_end=857
  _UPDATECOMMANDREQUEST._serialized_start=859
  _UPDATECOMMANDREQUEST._serialized_end=921
  _COMMAND._serialized_start=924
  _COMMAND._serialized_end=1666
  _EXEC._serialized_start=2102
  _EXEC._serialized_end=2529
# @@protoc_insertion_point(module_scope)
