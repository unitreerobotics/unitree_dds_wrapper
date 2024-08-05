from enum import auto
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass, field

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

from unitree_dds_wrapper.idl import geometry_msgs

@dataclass
@annotate.final
@annotate.autoid("sequential")
class TFMessage_(idl.IdlStruct, typename="tf2_msgs.msg.dds_.TFMessage_"):
    transforms: types.sequence['unitree_dds_wrapper.idl.geometry_msgs.msg.dds_.TransformStamped_'] = field(default_factory=lambda: [])
    