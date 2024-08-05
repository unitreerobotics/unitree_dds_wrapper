"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.11.0
  Module: nav_msgs.msg.dds_
  IDL file: MapMetaData_.idl

"""

from enum import auto
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass, field

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

from unitree_dds_wrapper.idl import builtin_interfaces, geometry_msgs

@dataclass
@annotate.final
@annotate.autoid("sequential")
class MapMetaData_(idl.IdlStruct, typename="nav_msgs.msg.dds_.MapMetaData_"):
    map_load_time: 'unitree_dds_wrapper.idl.builtin_interfaces.msg.dds_.Time_' = field(default_factory=lambda: builtin_interfaces.msg.dds_.Time_())
    resolution: types.float32 = field(default_factory=lambda: 0.0)
    width: types.uint32 = field(default_factory=lambda: 0)
    height: types.uint32 = field(default_factory=lambda: 0)
    origin: 'unitree_dds_wrapper.idl.geometry_msgs.msg.dds_.Pose_' = field(default_factory=lambda: geometry_msgs.msg.dds_.Pose_())

