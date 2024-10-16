from enum import auto
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass, field

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

@dataclass
@annotate.final
@annotate.autoid("sequential")
class SetServoAngle_(idl.IdlStruct, typename="unitree_arm.msg.dds_.SetServoAngle_"):
    seq: types.int32 = field(default_factory=lambda: 0)
    id: types.uint8 = field(default_factory=lambda: 0)
    angle: types.float32 = field(default_factory=lambda: 0.0)
    delay_ms: types.int16 = field(default_factory=lambda: 0)