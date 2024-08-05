from unitree_dds_wrapper.publisher import Publisher
from unitree_dds_wrapper.utils.crc import crc32
from unitree_dds_wrapper.utils.joystick import Joystick
import numpy as np
import struct
from unitree_dds_wrapper.idl import unitree_hg
from unitree_dds_wrapper.robots import hg

class LowCmd(Publisher):
    def __init__(self, participant = None, topic = "rt/lowcmd_hx"):
        super().__init__(unitree_hg.msg.dds_.LowCmd_, topic, participant)
        self.msg: unitree_hg.msg.dds_.LowCmd_

    def pre_communication(self):
        self.__pack_crc()

    def __pack_crc(self):
        rawdata = []
        #TODO: Implement crc check


class ArmSdk(Publisher):
    def __init__(self):
        super().__init__(message=unitree_hg.msg.dds_.LowCmd_, topic="rt/arm_sdk")
        self.msg: unitree_hg.msg.dds_.LowCmd_
        self.msg.motor_cmd[9].q = 1 # weight

    def SetQ(self, lq, rq):
        for i, id in enumerate(hg.LarmJointIndex):
            self.msg.motor_cmd[id].q = lq[i]
        for i, id in enumerate(hg.RarmJointIndex):
            self.msg.motor_cmd[id].q = rq[i]

    def MoveJ(self, lq, rq):
        init_lq = np.array([self.msg.motor_cmd[id].q for id in hg.LarmJointIndex])
        init_rq = np.array([self.msg.motor_cmd[id].q for id in hg.RarmJointIndex])

        duration = 1000
        for i in range(duration):
            lq_t = init_lq + (lq - init_lq) * i / duration
            rq_t = init_rq + (rq - init_rq) * i / duration

            self.SetQ(lq_t, rq_t)
            self.write()

    def SetDefaultGain(self):
        for i, id in enumerate(hg.LarmJointIndex):
            self.msg.motor_cmd[id].kp = [90, 60, 60, 60][i]
            self.msg.motor_cmd[id].kd = [2, 1, 1, 1][i]
        for i, id in enumerate(hg.RarmJointIndex):
            self.msg.motor_cmd[id].kp = [90, 60, 60, 60][i]
            self.msg.motor_cmd[id].kd = [2, 1, 1, 1][i]


class LowState(Publisher):
    def __init__(self, participant = None, topic = "rt/lowstate_hx"):
        super().__init__(unitree_hg.msg.dds_.LowState_, topic, participant)
        self.msg: unitree_hg.msg.dds_.LowState_