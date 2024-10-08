"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.11.0
  Module: unitree_go.msg.dds_
  IDL file: BmsCmd_.idl

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
class BmsCmd_(idl.IdlStruct, typename="unitree_go.msg.dds_.BmsCmd_"):
    off: types.uint8 = field(default_factory=lambda: 0)
    reserve: types.array[types.uint8, 3] = field(default_factory=lambda: [0, 0, 0])


