from . import h1_pub as pub
from . import h1_sub as sub

from enum import IntEnum

class JointIndex(IntEnum):
    RightHipRoll = 0
    RightHipPitch = 1
    RightKnee = 2
    LeftHipRoll = 3
    LeftHipPitch = 4
    LeftKnee = 5

    WaistYaw = 6
    LeftHipYaw = 7
    RightHipYaw = 8
    # Reserved
    LeftAnkle = 10
    RightAnkle = 11
    RightShoulderPitch = 12
    RightShoulderRoll = 13
    RightShoulderYaw = 14
    RightElbow = 15
    LeftShoulderPitch = 16
    LeftShoulderRoll = 17
    LeftShoulderYaw = 18
    LeftElbow = 19

class LarmJointIndex(IntEnum):
    LeftShoulderPitch = 16
    LeftShoulderRoll = 17
    LeftShoulderYaw = 18
    LeftElbow = 19

class RarmJointIndex(IntEnum):
    RightShoulderPitch = 12
    RightShoulderRoll = 13
    RightShoulderYaw = 14
    RightElbow = 15

JointLists = [ # Joints in urdf
    "left_hip_yaw_joint",
    "left_hip_roll_joint",
    "left_hip_pitch_joint",
    "left_knee_joint",
    "left_ankle_joint",
    "right_hip_yaw_joint",
    "right_hip_roll_joint",
    "right_hip_pitch_joint",
    "right_knee_joint",
    "right_ankle_joint",

    "torso_joint",

    "left_shoulder_pitch_joint",
    "left_shoulder_roll_joint",
    "left_shoulder_yaw_joint",
    "left_elbow_joint",
    "right_shoulder_pitch_joint",
    "right_shoulder_roll_joint",
    "right_shoulder_yaw_joint",
    "right_elbow_joint",
]