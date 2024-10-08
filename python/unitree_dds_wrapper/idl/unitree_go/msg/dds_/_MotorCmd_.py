"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.11.0
  Module: unitree_go.msg.dds_
  IDL file: MotorCmd_.idl

"""

from enum import auto
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass, field

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

@dataclass
@annotate.final
@annotate.autoid("sequential")
class MotorCmd_(idl.IdlStruct, typename="unitree_go.msg.dds_.MotorCmd_"):
    mode: types.uint8 = field(default_factory=lambda: 1)
    q: types.float32 = field(default_factory=lambda: 0.)
    dq: types.float32 = field(default_factory=lambda: 0.)
    tau: types.float32 = field(default_factory=lambda: 0.)
    kp: types.float32 = field(default_factory=lambda: 0.)
    kd: types.float32 = field(default_factory=lambda: 0.)
    reserve: types.array[types.uint32, 3] = field(default_factory=lambda: [0, 0, 0])


