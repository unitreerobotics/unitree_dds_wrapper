from unitree_dds_wrapper.publisher import Publisher
from unitree_dds_wrapper.idl import unitree_hg, unitree_go
import numpy as np
import struct
from unitree_dds_wrapper.utils.crc import crc32

class LowCmd(Publisher):
    def __init__(self, participant = None, topic = "rt/lowcmd_hx"):
        super().__init__(unitree_hg.msg.dds_.LowCmd_, topic, participant)
        self.msg: unitree_hg.msg.dds_.LowCmd_
        self.__packCRCformat = '<2B2x2I' \
         + 'B3x5f3I' * len(self.msg.motor_cmd) \
         + '41B104B3x3I'

    def pre_communication(self):
        self.__pack_crc()

    def __pack_crc(self):
        rawdata = []
        rawdata.extend(self.msg.head)
        rawdata.extend(self.msg.version)
        for i in range(len(self.msg.motor_cmd)):
            rawdata.append(self.msg.motor_cmd[i].mode)
            rawdata.append(self.msg.motor_cmd[i].q)
            rawdata.append(self.msg.motor_cmd[i].dq)
            rawdata.append(self.msg.motor_cmd[i].tau)
            rawdata.append(self.msg.motor_cmd[i].kp)
            rawdata.append(self.msg.motor_cmd[i].kd)
            rawdata.extend(self.msg.motor_cmd[i].reserve)
        rawdata.append(self.msg.bms_cmd.cmd)
        rawdata.extend(self.msg.bms_cmd.reserve)
        rawdata.extend(self.msg.led_cmd)
        rawdata.extend(self.msg.fan_cmd)
        rawdata.extend(self.msg.cmd)
        rawdata.extend(self.msg.data)
        rawdata.extend(self.msg.reserve)
        rawdata.append(self.msg.crc)

        packdata = struct.pack(self.__packCRCformat, *rawdata)
        calcdata = []
        calclen = (len(packdata)>>2)-1
        for i in range(calclen):
            d = ((packdata[i*4+3] << 24) | (packdata[i*4+2] << 16) | (packdata[i*4+1] << 8) | (packdata[i*4]))
            calcdata.append(d)

        self.msg.crc = crc32(calcdata)

class LowState(Publisher):
    def __init__(self, participant = None, topic = "rt/lowstate_hx"):
        super().__init__(unitree_hg.msg.dds_.LowState_, topic, participant)
        self.msg: unitree_hg.msg.dds_.LowState_

class ArmSdk(Publisher):
    def __init__(self):
        super().__init__(message=unitree_hg.msg.dds_.LowCmd_, topic="rt/arm_sdk")
        self.msg: unitree_hg.msg.dds_.LowCmd_
        self.msg.motor_cmd[23].q = 1

        class ArmData:
            def __init__(self):
                self.kp: np.array = np.zeros(5)
                self.kd: np.array = np.zeros(5)
                self.q: np.array = np.zeros(5)
                self.dq: np.array = np.zeros(5)
                self.tau: np.array = np.zeros(5)

        self.l = ArmData()
        self.r = ArmData()
        self.waist = self.msg.motor_cmd[12]

    def setGain(self, kp, kd):
        self.l.kp = kp.copy()
        self.l.kd = kd.copy()
    
    def pre_communication(self):
        for i in range(5):
            self.msg.motor_cmd[i + 13].kp = self.l.kp[i]
            self.msg.motor_cmd[i + 13].kd = self.l.kd[i]
            self.msg.motor_cmd[i + 13].q = self.l.q[i]
            self.msg.motor_cmd[i + 13].dq = self.l.dq[i]
            self.msg.motor_cmd[i + 13].tau = self.l.tau[i]
            self.msg.motor_cmd[i + 18].kp = self.r.kp[i]
            self.msg.motor_cmd[i + 18].kd = self.r.kd[i]
            self.msg.motor_cmd[i + 18].q = self.r.q[i]
            self.msg.motor_cmd[i + 18].dq = self.r.dq[i]
            self.msg.motor_cmd[i + 18].tau = self.r.tau[i]

class UnitreeHand(Publisher):
    def __init__(self):
        super().__init__(unitree_go.msg.dds_.MotorCmds_, "rt/hand/cmd")
        self.msg: unitree_go.msg.dds_.MotorCmds_
        self.msg.cmds  = [unitree_go.msg.dds_.MotorCmd_() for _ in range(2 * 7)]

        class HandData:
            def __init__(self):
                self.kp: np.array = np.zeros(7)
                self.kd: np.array = np.zeros(7)
                self.q: np.array = np.zeros(7)
                self.dq: np.array = np.zeros(7)
                self.tau: np.array = np.zeros(7)
        self.l = HandData()
        self.r = HandData()
    
    def pre_communication(self):
        for i in range(7):
            self.msg.cmds[i].kp = self.l.kp[i]
            self.msg.cmds[i].kd = self.l.kd[i]
            self.msg.cmds[i].q = self.l.q[i]
            self.msg.cmds[i].dq = self.l.dq[i]
            self.msg.cmds[i].tau = self.l.tau[i]
            self.msg.cmds[i+7].kp = self.r.kp[i]
            self.msg.cmds[i+7].kd = self.r.kd[i]
            self.msg.cmds[i+7].q = self.r.q[i]
            self.msg.cmds[i+7].dq = self.r.dq[i]
            self.msg.cmds[i+7].tau = self.r.tau[i]