# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/run.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import fab_pb2 as flwr_dot_proto_dot_fab__pb2
from flwr.proto import node_pb2 as flwr_dot_proto_dot_node__pb2
from flwr.proto import recordset_pb2 as flwr_dot_proto_dot_recordset__pb2
from flwr.proto import transport_pb2 as flwr_dot_proto_dot_transport__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x66lwr/proto/run.proto\x12\nflwr.proto\x1a\x14\x66lwr/proto/fab.proto\x1a\x15\x66lwr/proto/node.proto\x1a\x1a\x66lwr/proto/recordset.proto\x1a\x1a\x66lwr/proto/transport.proto\"\xd5\x01\n\x03Run\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\x12\x0e\n\x06\x66\x61\x62_id\x18\x02 \x01(\t\x12\x13\n\x0b\x66\x61\x62_version\x18\x03 \x01(\t\x12<\n\x0foverride_config\x18\x04 \x03(\x0b\x32#.flwr.proto.Run.OverrideConfigEntry\x12\x10\n\x08\x66\x61\x62_hash\x18\x05 \x01(\t\x1aI\n\x13OverrideConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.flwr.proto.Scalar:\x02\x38\x01\"@\n\tRunStatus\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x12\n\nsub_status\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65tails\x18\x03 \x01(\t\"\xeb\x01\n\x10\x43reateRunRequest\x12\x0e\n\x06\x66\x61\x62_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66\x61\x62_version\x18\x02 \x01(\t\x12I\n\x0foverride_config\x18\x03 \x03(\x0b\x32\x30.flwr.proto.CreateRunRequest.OverrideConfigEntry\x12\x1c\n\x03\x66\x61\x62\x18\x04 \x01(\x0b\x32\x0f.flwr.proto.Fab\x1aI\n\x13OverrideConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.flwr.proto.Scalar:\x02\x38\x01\"#\n\x11\x43reateRunResponse\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\"?\n\rGetRunRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12\x0e\n\x06run_id\x18\x02 \x01(\x04\".\n\x0eGetRunResponse\x12\x1c\n\x03run\x18\x01 \x01(\x0b\x32\x0f.flwr.proto.Run\"S\n\x16UpdateRunStatusRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\x12)\n\nrun_status\x18\x02 \x01(\x0b\x32\x15.flwr.proto.RunStatus\"\x19\n\x17UpdateRunStatusResponse\"F\n\x13GetRunStatusRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12\x0f\n\x07run_ids\x18\x02 \x03(\x04\"\xb1\x01\n\x14GetRunStatusResponse\x12L\n\x0frun_status_dict\x18\x01 \x03(\x0b\x32\x33.flwr.proto.GetRunStatusResponse.RunStatusDictEntry\x1aK\n\x12RunStatusDictEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.flwr.proto.RunStatus:\x02\x38\x01\"-\n\x1bGetFederationOptionsRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\"U\n\x1cGetFederationOptionsResponse\x12\x35\n\x12\x66\x65\x64\x65ration_options\x18\x01 \x01(\x0b\x32\x19.flwr.proto.ConfigsRecordb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.run_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_RUN_OVERRIDECONFIGENTRY']._options = None
  _globals['_RUN_OVERRIDECONFIGENTRY']._serialized_options = b'8\001'
  _globals['_CREATERUNREQUEST_OVERRIDECONFIGENTRY']._options = None
  _globals['_CREATERUNREQUEST_OVERRIDECONFIGENTRY']._serialized_options = b'8\001'
  _globals['_GETRUNSTATUSRESPONSE_RUNSTATUSDICTENTRY']._options = None
  _globals['_GETRUNSTATUSRESPONSE_RUNSTATUSDICTENTRY']._serialized_options = b'8\001'
  _globals['_RUN']._serialized_start=138
  _globals['_RUN']._serialized_end=351
  _globals['_RUN_OVERRIDECONFIGENTRY']._serialized_start=278
  _globals['_RUN_OVERRIDECONFIGENTRY']._serialized_end=351
  _globals['_RUNSTATUS']._serialized_start=353
  _globals['_RUNSTATUS']._serialized_end=417
  _globals['_CREATERUNREQUEST']._serialized_start=420
  _globals['_CREATERUNREQUEST']._serialized_end=655
  _globals['_CREATERUNREQUEST_OVERRIDECONFIGENTRY']._serialized_start=278
  _globals['_CREATERUNREQUEST_OVERRIDECONFIGENTRY']._serialized_end=351
  _globals['_CREATERUNRESPONSE']._serialized_start=657
  _globals['_CREATERUNRESPONSE']._serialized_end=692
  _globals['_GETRUNREQUEST']._serialized_start=694
  _globals['_GETRUNREQUEST']._serialized_end=757
  _globals['_GETRUNRESPONSE']._serialized_start=759
  _globals['_GETRUNRESPONSE']._serialized_end=805
  _globals['_UPDATERUNSTATUSREQUEST']._serialized_start=807
  _globals['_UPDATERUNSTATUSREQUEST']._serialized_end=890
  _globals['_UPDATERUNSTATUSRESPONSE']._serialized_start=892
  _globals['_UPDATERUNSTATUSRESPONSE']._serialized_end=917
  _globals['_GETRUNSTATUSREQUEST']._serialized_start=919
  _globals['_GETRUNSTATUSREQUEST']._serialized_end=989
  _globals['_GETRUNSTATUSRESPONSE']._serialized_start=992
  _globals['_GETRUNSTATUSRESPONSE']._serialized_end=1169
  _globals['_GETRUNSTATUSRESPONSE_RUNSTATUSDICTENTRY']._serialized_start=1094
  _globals['_GETRUNSTATUSRESPONSE_RUNSTATUSDICTENTRY']._serialized_end=1169
  _globals['_GETFEDERATIONOPTIONSREQUEST']._serialized_start=1171
  _globals['_GETFEDERATIONOPTIONSREQUEST']._serialized_end=1216
  _globals['_GETFEDERATIONOPTIONSRESPONSE']._serialized_start=1218
  _globals['_GETFEDERATIONOPTIONSRESPONSE']._serialized_end=1303
# @@protoc_insertion_point(module_scope)
