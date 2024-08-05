
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
class Transform_(idl.IdlStruct, typename="geometry_msgs.msg.dds_.Transform_"):
    translation: 'unitree_dds_wrapper.idl.geometry_msgs.msg.dds_.Vector3_' = field(default_factory=lambda: geometry_msgs.msg.dds_.Vector3_())
    rotation: 'unitree_dds_wrapper.idl.geometry_msgs.msg.dds_.Quaternion_' = field(default_factory=lambda: geometry_msgs.msg.dds_.Quaternion_())