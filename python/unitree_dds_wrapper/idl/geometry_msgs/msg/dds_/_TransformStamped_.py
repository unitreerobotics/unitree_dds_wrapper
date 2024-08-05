from enum import auto
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass, field

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

from unitree_dds_wrapper.idl import geometry_msgs, std_msgs
import unitree_dds_wrapper

@dataclass
@annotate.final
@annotate.autoid("sequential")
class TransformStamped_(idl.IdlStruct, typename="geometry_msgs.msg.dds_.TransformStamped_"):
    header: 'unitree_dds_wrapper.idl.std_msgs.msg.dds_.Header_' = field(default_factory=lambda: std_msgs.msg.dds_.Header_())
    child_frame_id: str = field(default_factory=lambda: "")
    transform: 'unitree_dds_wrapper.idl.geometry_msgs.msg.dds_.Transform_' = field(default_factory=lambda: geometry_msgs.msg.dds_.Transform_())