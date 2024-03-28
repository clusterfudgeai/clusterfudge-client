# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: launches/launches.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..resources import resources_pb2 as resources_dot_resources__pb2
from ..exec import exec_pb2 as exec_dot_exec__pb2
from ..logs import logs_pb2 as logs_dot_logs__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17launches/launches.proto\x12\x0c\x63lusterfudge\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19resources/resources.proto\x1a\x0f\x65xec/exec.proto\x1a\x0flogs/logs.proto\"\x16\n\x14ListResourcesRequest\"|\n\x15ListResourcesResponse\x12\x30\n\x08\x63lusters\x18\x01 \x03(\x0b\x32\x1e.clusterfudge.ClusterResources\x12\x31\n\x12resource_consumers\x18\x02 \x03(\x0b\x32\x15.clusterfudge.Command\"\x96\x05\n\x10\x43lusterResources\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x30\n\x0ftotal_resources\x18\x02 \x01(\x0b\x32\x17.clusterfudge.Resources\x12/\n\x0eused_resources\x18\x03 \x01(\x0b\x32\x17.clusterfudge.Resources\x12\x36\n\x15used_non_clusterfudge\x18\x07 \x01(\x0b\x32\x17.clusterfudge.Resources\x12\x34\n\x13\x61vailable_resources\x18\x04 \x01(\x0b\x32\x17.clusterfudge.Resources\x12\x33\n\x12\x63ordoned_resources\x18\x05 \x01(\x0b\x32\x17.clusterfudge.Resources\x12\x32\n\x11offline_resources\x18\x06 \x01(\x0b\x32\x17.clusterfudge.Resources\x12\x35\n\x0fshard_resources\x18\x08 \x03(\x0b\x32\x1c.clusterfudge.ShardResources\x12\x33\n\x0bgpu_rtx3090\x18\t \x01(\x0b\x32\x1e.clusterfudge.ResourceStatuses\x12\x35\n\rgpu_a100_40gb\x18\n \x01(\x0b\x32\x1e.clusterfudge.ResourceStatuses\x12\x35\n\rgpu_a100_80gb\x18\x0b \x01(\x0b\x32\x1e.clusterfudge.ResourceStatuses\x12\x30\n\x08gpu_h100\x18\x0c \x01(\x0b\x32\x1e.clusterfudge.ResourceStatuses\x12.\n\x06gpu_t4\x18\r \x01(\x0b\x32\x1e.clusterfudge.ResourceStatuses\"\xdd\x04\n\x0eShardResources\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x30\n\x0ftotal_resources\x18\x02 \x01(\x0b\x32\x17.clusterfudge.Resources\x12/\n\x0eused_resources\x18\x03 \x01(\x0b\x32\x17.clusterfudge.Resources\x12\x36\n\x15used_non_clusterfudge\x18\x07 \x01(\x0b\x32\x17.clusterfudge.Resources\x12\x34\n\x13\x61vailable_resources\x18\x04 \x01(\x0b\x32\x17.clusterfudge.Resources\x12\x33\n\x12\x63ordoned_resources\x18\x05 \x01(\x0b\x32\x17.clusterfudge.Resources\x12\x32\n\x11offline_resources\x18\x06 \x01(\x0b\x32\x17.clusterfudge.Resources\x12\x33\n\x0bgpu_rtx3090\x18\x08 \x01(\x0b\x32\x1e.clusterfudge.ResourceStatuses\x12\x35\n\rgpu_a100_40gb\x18\t \x01(\x0b\x32\x1e.clusterfudge.ResourceStatuses\x12\x35\n\rgpu_a100_80gb\x18\n \x01(\x0b\x32\x1e.clusterfudge.ResourceStatuses\x12\x30\n\x08gpu_h100\x18\x0b \x01(\x0b\x32\x1e.clusterfudge.ResourceStatuses\x12.\n\x06gpu_t4\x18\x0c \x01(\x0b\x32\x1e.clusterfudge.ResourceStatuses\"\x80\x03\n\x10ResourceStatuses\x12\x37\n\x05total\x18\x01 \x01(\x0b\x32(.clusterfudge.ResourceCountWithHostnames\x12\x36\n\x04used\x18\x02 \x01(\x0b\x32(.clusterfudge.ResourceCountWithHostnames\x12G\n\x15used_non_clusterfudge\x18\x03 \x01(\x0b\x32(.clusterfudge.ResourceCountWithHostnames\x12;\n\tavailable\x18\x04 \x01(\x0b\x32(.clusterfudge.ResourceCountWithHostnames\x12:\n\x08\x63ordoned\x18\x05 \x01(\x0b\x32(.clusterfudge.ResourceCountWithHostnames\x12\x39\n\x07offline\x18\x06 \x01(\x0b\x32(.clusterfudge.ResourceCountWithHostnames\">\n\x1aResourceCountWithHostnames\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12\x11\n\thostnames\x18\x02 \x03(\t\"\x1e\n\x10GetLaunchRequest\x12\n\n\x02id\x18\x01 \x01(\t\"%\n\x17GetLaunchDetailsRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x15\n\x13ListLaunchesRequest\">\n\x14ListLaunchesResponse\x12&\n\x08launches\x18\x01 \x03(\x0b\x32\x14.clusterfudge.Launch\"\x1f\n\x11StopLaunchRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x14\n\x12StopLaunchResponse\"\xb7\x05\n\x06Launch\x12\x11\n\tlaunch_id\x18\x01 \x01(\x05\x12\x13\n\x0blaunched_by\x18\x02 \x01(\t\x12\x30\n\x0csubmitted_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0e\x63ommand_to_run\x18\x04 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x08 \x03(\t\x12\x11\n\thostnames\x18\x05 \x03(\t\x12+\n\x06status\x18\x06 \x01(\x0e\x32\x1b.clusterfudge.Launch.Status\x12\n\n\x02id\x18\x07 \x01(\t\x12\r\n\x05title\x18\t \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\n \x01(\t\x12\x10\n\x08replicas\x18\x0b \x01(\x05\x12\x32\n\x11replica_resources\x18\x0c \x01(\x0b\x32\x17.clusterfudge.Resources\x12\x1a\n\x12launch_script_body\x18\r \x01(\t\x12\x16\n\x0escheduling_log\x18\x0e \x03(\t\x12\x0e\n\x06zip_id\x18\x0f \x01(\t\x12\x10\n\x08git_repo\x18\x10 \x01(\t\x12\x12\n\ngit_branch\x18\x11 \x01(\t\x12\r\n\x05shard\x18\x12 \x01(\t\x12\x0f\n\x07\x63luster\x18\x13 \x01(\t\x12\x1f\n\x04jobs\x18\x14 \x03(\x0b\x32\x11.clusterfudge.Job\"\xc8\x01\n\x06Status\x12\x19\n\x15LAUNCH_STATUS_UNKNOWN\x10\x00\x12\x19\n\x15LAUNCH_STATUS_PENDING\x10\x01\x12\x19\n\x15LAUNCH_STATUS_RUNNING\x10\x02\x12\x1b\n\x17LAUNCH_STATUS_COMPLETED\x10\x03\x12\x18\n\x14LAUNCH_STATUS_FAILED\x10\x04\x12\x1b\n\x17LAUNCH_STATUS_UNMANAGED\x10\x05\x12\x19\n\x15LAUNCH_STATUS_STOPPED\x10\x06\"d\n\'ListLaunchesWithCommandStatusesResponse\x12\x39\n\x08launches\x18\x01 \x03(\x0b\x32\'.clusterfudge.LaunchWithCommandStatuses\"\xed\x02\n\x19LaunchWithCommandStatuses\x12$\n\x06launch\x18\x01 \x01(\x0b\x32\x14.clusterfudge.Launch\x12\x1e\n\x16\x63ommands_unknown_count\x18\x02 \x01(\x03\x12%\n\x1d\x63ommands_unacknowledged_count\x18\x03 \x01(\x03\x12#\n\x1b\x63ommands_acknowledged_count\x18\x04 \x01(\x03\x12\x1e\n\x16\x63ommands_running_count\x18\x05 \x01(\x03\x12 \n\x18\x63ommands_succeeded_count\x18\x06 \x01(\x03\x12\x1d\n\x15\x63ommands_failed_count\x18\x07 \x01(\x03\x12\x1d\n\x15\x63ommands_killed_count\x18\x08 \x01(\x03\x12 \n\x18\x63ommands_cancelled_count\x18\t \x01(\x03\x12\x1c\n\x14\x63ommands_total_count\x18\n \x01(\x03\"\'\n\x12RerunLaunchRequest\x12\x11\n\tlaunch_id\x18\x01 \x01(\t\";\n\x13RerunLaunchResponse\x12$\n\x06launch\x18\x01 \x01(\x0b\x32\x14.clusterfudge.Launch\"\xd8\x01\n\rLaunchDetails\x12$\n\x06launch\x18\x01 \x01(\x0b\x32\x14.clusterfudge.Launch\x12\'\n\x08\x63ommands\x18\x02 \x03(\x0b\x32\x15.clusterfudge.Command\x12\x1f\n\x04xids\x18\x03 \x03(\x0b\x32\x11.clusterfudge.Xid\x12#\n\x04logs\x18\x04 \x03(\x0b\x32\x15.clusterfudge.log.Log\x12\x32\n\x0eimportant_logs\x18\x05 \x03(\x0b\x32\x1a.clusterfudge.ImportantLog\"\x9f\x01\n\x0cImportantLog\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12/\n\x0boccurred_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tlaunch_id\x18\x04 \x01(\t\x12\x17\n\x0f\x65xec_command_id\x18\x05 \x01(\t\x12\x14\n\x0ctext_payload\x18\x06 \x01(\t\"w\n\x03Xid\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x10\n\x08gpu_uuid\x18\x02 \x01(\t\x12\x0e\n\x06pci_id\x18\x03 \x01(\t\x12\x0b\n\x03xid\x18\x04 \x01(\x05\x12/\n\x0boccurred_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xee\x02\n\x13\x43reateLaunchRequest\x12\x13\n\x0blaunched_by\x18\x01 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x04 \x03(\t\x12\x16\n\x0e\x63ommand_to_run\x18\x02 \x01(\t\x12\x11\n\thostnames\x18\x03 \x03(\t\x12\x10\n\x08replicas\x18\x07 \x01(\x05\x12\x32\n\x11replica_resources\x18\x08 \x01(\x0b\x32\x17.clusterfudge.Resources\x12\r\n\x05title\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x1a\n\x12launch_script_body\x18\t \x01(\t\x12\x19\n\x11zip_file_contents\x18\n \x01(\x0c\x12\x10\n\x08git_repo\x18\x0b \x01(\t\x12\x12\n\ngit_branch\x18\x0c \x01(\t\x12\r\n\x05shard\x18\r \x01(\t\x12\x0f\n\x07\x63luster\x18\x0e \x01(\t\x12\x1f\n\x04jobs\x18\x0f \x03(\x0b\x32\x11.clusterfudge.Job\"U\n\x03Job\x12\x12\n\nshort_name\x18\x01 \x01(\t\x12\x10\n\x08replicas\x18\x02 \x01(\x05\x12(\n\tprocesses\x18\x03 \x03(\x0b\x32\x15.clusterfudge.Process\"R\n\x07Process\x12\x0f\n\x07\x63ommand\x18\x01 \x03(\t\x12\x36\n\x15resource_requirements\x18\x02 \x01(\x0b\x32\x17.clusterfudge.Resources\" \n\x12\x44ownloadZipRequest\x12\n\n\x02id\x18\x01 \x01(\t\"5\n\x13\x44ownloadZipResponse\x12\x1e\n\x03zip\x18\x01 \x01(\x0b\x32\x11.clusterfudge.Zip\"I\n\x03Zip\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x11\n\tlaunch_id\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08\x63ontents\x18\x04 \x01(\x0c\x32\xa7\x06\n\x08Launches\x12\x43\n\tGetLaunch\x12\x1e.clusterfudge.GetLaunchRequest\x1a\x14.clusterfudge.Launch\"\x00\x12X\n\x10GetLaunchDetails\x12%.clusterfudge.GetLaunchDetailsRequest\x1a\x1b.clusterfudge.LaunchDetails\"\x00\x12W\n\x0cListLaunches\x12!.clusterfudge.ListLaunchesRequest\x1a\".clusterfudge.ListLaunchesResponse\"\x00\x12}\n\x1fListLaunchesWithCommandStatuses\x12!.clusterfudge.ListLaunchesRequest\x1a\x35.clusterfudge.ListLaunchesWithCommandStatusesResponse\"\x00\x12I\n\x0c\x43reateLaunch\x12!.clusterfudge.CreateLaunchRequest\x1a\x14.clusterfudge.Launch\"\x00\x12Q\n\nStopLaunch\x12\x1f.clusterfudge.StopLaunchRequest\x1a .clusterfudge.StopLaunchResponse\"\x00\x12T\n\x0bRerunLaunch\x12 .clusterfudge.RerunLaunchRequest\x1a!.clusterfudge.RerunLaunchResponse\"\x00\x12Z\n\rListResources\x12\".clusterfudge.ListResourcesRequest\x1a#.clusterfudge.ListResourcesResponse\"\x00\x12T\n\x0b\x44ownloadZip\x12 .clusterfudge.DownloadZipRequest\x1a!.clusterfudge.DownloadZipResponse\"\x00\x42\x30Z.github.com/clusterfudgeai/fudge/proto/launchesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'launches.launches_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z.github.com/clusterfudgeai/fudge/proto/launches'
  _LISTRESOURCESREQUEST._serialized_start=135
  _LISTRESOURCESREQUEST._serialized_end=157
  _LISTRESOURCESRESPONSE._serialized_start=159
  _LISTRESOURCESRESPONSE._serialized_end=283
  _CLUSTERRESOURCES._serialized_start=286
  _CLUSTERRESOURCES._serialized_end=948
  _SHARDRESOURCES._serialized_start=951
  _SHARDRESOURCES._serialized_end=1556
  _RESOURCESTATUSES._serialized_start=1559
  _RESOURCESTATUSES._serialized_end=1943
  _RESOURCECOUNTWITHHOSTNAMES._serialized_start=1945
  _RESOURCECOUNTWITHHOSTNAMES._serialized_end=2007
  _GETLAUNCHREQUEST._serialized_start=2009
  _GETLAUNCHREQUEST._serialized_end=2039
  _GETLAUNCHDETAILSREQUEST._serialized_start=2041
  _GETLAUNCHDETAILSREQUEST._serialized_end=2078
  _LISTLAUNCHESREQUEST._serialized_start=2080
  _LISTLAUNCHESREQUEST._serialized_end=2101
  _LISTLAUNCHESRESPONSE._serialized_start=2103
  _LISTLAUNCHESRESPONSE._serialized_end=2165
  _STOPLAUNCHREQUEST._serialized_start=2167
  _STOPLAUNCHREQUEST._serialized_end=2198
  _STOPLAUNCHRESPONSE._serialized_start=2200
  _STOPLAUNCHRESPONSE._serialized_end=2220
  _LAUNCH._serialized_start=2223
  _LAUNCH._serialized_end=2918
  _LAUNCH_STATUS._serialized_start=2718
  _LAUNCH_STATUS._serialized_end=2918
  _LISTLAUNCHESWITHCOMMANDSTATUSESRESPONSE._serialized_start=2920
  _LISTLAUNCHESWITHCOMMANDSTATUSESRESPONSE._serialized_end=3020
  _LAUNCHWITHCOMMANDSTATUSES._serialized_start=3023
  _LAUNCHWITHCOMMANDSTATUSES._serialized_end=3388
  _RERUNLAUNCHREQUEST._serialized_start=3390
  _RERUNLAUNCHREQUEST._serialized_end=3429
  _RERUNLAUNCHRESPONSE._serialized_start=3431
  _RERUNLAUNCHRESPONSE._serialized_end=3490
  _LAUNCHDETAILS._serialized_start=3493
  _LAUNCHDETAILS._serialized_end=3709
  _IMPORTANTLOG._serialized_start=3712
  _IMPORTANTLOG._serialized_end=3871
  _XID._serialized_start=3873
  _XID._serialized_end=3992
  _CREATELAUNCHREQUEST._serialized_start=3995
  _CREATELAUNCHREQUEST._serialized_end=4361
  _JOB._serialized_start=4363
  _JOB._serialized_end=4448
  _PROCESS._serialized_start=4450
  _PROCESS._serialized_end=4532
  _DOWNLOADZIPREQUEST._serialized_start=4534
  _DOWNLOADZIPREQUEST._serialized_end=4566
  _DOWNLOADZIPRESPONSE._serialized_start=4568
  _DOWNLOADZIPRESPONSE._serialized_end=4621
  _ZIP._serialized_start=4623
  _ZIP._serialized_end=4696
  _LAUNCHES._serialized_start=4699
  _LAUNCHES._serialized_end=5506
# @@protoc_insertion_point(module_scope)
