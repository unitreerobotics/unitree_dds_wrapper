"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.10.5
  Module: unitree_hg.msg.dds_
  IDL file: MotorState_.idl

"""

from enum import auto
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass ,field

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

# root module import for resolving types
from  unitree_dds_wrapper.idl.unitree_hand import unitree_hg


@dataclass
@annotate.final
@annotate.autoid("sequential")
class MotorState_(idl.IdlStruct, typename="unitree_dds_wrapper.idl.unitree_hand.unitree_hg.msg.dds_.MotorState_"):
    mode: types.uint8  = field(default_factory=lambda: 0)
    q: types.float32 = field(default_factory=lambda: 0)
    dq: types.float32 = field(default_factory=lambda: 0)
    ddq: types.float32 = field(default_factory=lambda: 0)
    tau_est: types.float32 = field(default_factory=lambda: 0)
    temperature: types.array[types.int16, 2] = field(default_factory=lambda: [0, 0])
    vol: types.float32  = field(default_factory=lambda: 0)
    sensor: types.array[types.uint32, 2] = field(default_factory=lambda: [0, 0])
    motorstate: types.uint32 = field(default_factory=lambda: 0)
    reserve: types.array[types.uint32, 4] = field(default_factory=lambda: [0, 0,0,0])


