"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.11.0
  Module: unitree_go.msg.dds_
  IDL file: Error_.idl

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
class Error_(idl.IdlStruct, typename="unitree_go.msg.dds_.Error_"):
    source: types.uint32 = field(default_factory=lambda: 0)
    state: types.uint32 = field(default_factory=lambda: 0)


