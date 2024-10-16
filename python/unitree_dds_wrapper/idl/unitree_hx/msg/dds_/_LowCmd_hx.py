"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.11.0
  Module: unitree_hx.msg.dds_
  IDL file: LowCmd_hx.idl

"""

from enum import auto
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass, field

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

from unitree_dds_wrapper.idl import unitree_hx

@dataclass
@annotate.final
@annotate.autoid("sequential")
class LowCmd_(idl.IdlStruct, typename="unitree_hx.msg.dds_.LowCmd_"):
    head: types.array[types.uint8, 2] = field(default_factory=lambda: [0xFE, 0xEF])
    version: types.array[types.uint32, 2] = field(default_factory=lambda: [0, 0])
    motor_cmd: types.array['unitree_dds_wrapper.idl.unitree_hx.msg.dds_.MotorCmd_', 30] = field(default_factory=lambda: [unitree_hx.msg.dds_.MotorCmd_() for _ in range(30)])
    bms_cmd: 'unitree_dds_wrapper.idl.unitree_hx.msg.dds_.BmsCmd_' = field(default_factory=lambda: unitree_hx.msg.dds_.BmsCmd_())
    led_cmd: types.array[types.uint8, 10] = field(default_factory=lambda: [0 for _ in range(10)])
    fan_cmd: types.array[types.uint8, 10] = field(default_factory=lambda: [0 for _ in range(10)])
    cmd: types.array[types.uint8, 20] = field(default_factory=lambda: [0 for _ in range(20)])
    data: types.array[types.uint8, 64] = field(default_factory=lambda: [0 for _ in range(64)])
    reserve: types.array[types.uint32, 2] = field(default_factory=lambda: [0, 0])
    crc: types.uint32 = field(default_factory=lambda: 0)


