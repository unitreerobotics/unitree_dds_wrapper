"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.10.5
  Module: unitree_hg.msg.dds_
  IDL file: HandCmd_.idl

"""

from enum import auto
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass,field

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

# root module import for resolving types
from  unitree_dds_wrapper.idl.unitree_hand import unitree_hg


@dataclass
@annotate.final
@annotate.autoid("sequential")
class HandCmd_(idl.IdlStruct, typename="unitree_hg.msg.dds_.HandCmd_"):
    motor_cmd: types.sequence['unitree_dds_wrapper.idl.unitree_hand.unitree_hg.msg.dds_.MotorCmd_']=field(default_factory=lambda: [unitree_hg.msg.dds_.MotorCmd_() for _ in range(14)])
    reserve: types.array[types.uint32, 4] = field(default_factory=lambda: [0,0,0,0])


