"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.11.0
  Module: geometry_msgs.msg.dds_
  IDL file: TwistStamped_.idl

"""

from enum import auto
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass, field

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

from unitree_dds_wrapper.idl import std_msgs, geometry_msgs

@dataclass
@annotate.final
@annotate.autoid("sequential")
class TwistStamped_(idl.IdlStruct, typename="geometry_msgs.msg.dds_.TwistStamped_"):
    header: 'unitree_dds_wrapper.idl.std_msgs.msg.dds_.Header_' = field(default_factory=lambda: std_msgs.msg.dds_.Header_())
    twist: 'unitree_dds_wrapper.idl.geometry_msgs.msg.dds_.Twist_' = field(default_factory=lambda: geometry_msgs.msg.dds_.Twist_())


