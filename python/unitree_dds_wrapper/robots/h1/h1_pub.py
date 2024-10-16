from unitree_dds_wrapper.publisher import Publisher
from unitree_dds_wrapper.idl import unitree_go
from unitree_dds_wrapper.robots import h1
import numpy as np
import time
import struct
from unitree_dds_wrapper.utils.crc import crc32
class LowCmd(Publisher):
    def __init__(self, participant = None, topic = "rt/lowcmd"):
        super().__init__(unitree_go.msg.dds_.LowCmd_, topic, participant)
        self.msg: unitree_go.msg.dds_.LowCmd_
        self.__packFmtHGLowCmd = '<4B4IH2x' + 'B3x5f3I' * 20 + '4B' + '55Bx2I'
    def pre_communication(self):
        self.__pack_crc()

    def __pack_crc(self):
        origData = []
        origData.append(self.msg.mode_pr)
        origData.append(self.msg.mode_machine)

        for i in range(35):
            origData.append(self.msg.motor_cmd[i].mode)
            origData.append(self.msg.motor_cmd[i].q)
            origData.append(self.msg.motor_cmd[i].dq)
            origData.append(self.msg.motor_cmd[i].tau)
            origData.append(self.msg.motor_cmd[i].kp)
            origData.append(self.msg.motor_cmd[i].kd)
            origData.append(self.msg.motor_cmd[i].reserve)

        origData.extend(self.msg.reserve)
        origData.append(self.msg.crc)
        calcdata = struct.pack(self.__packFmtHGLowCmd, *origData)
        calcdata =  self.__Trans(calcdata)
        self.msg.crc = crc32(calcdata)
    def __Trans(self, packData):
        calcData = []
        calcLen = ((len(packData)>>2)-1)

        for i in range(calcLen):
            d = ((packData[i*4+3] << 24) | (packData[i*4+2] << 16) | (packData[i*4+1] << 8) | (packData[i*4]))
            calcData.append(d)

        return calcData

class ArmSdk(Publisher):
    def __init__(self, topic = "rt/arm_sdk"):
        super().__init__(message=unitree_go.msg.dds_.LowCmd_, topic=topic)
        self.msg: unitree_go.msg.dds_.LowCmd_
        self.msg.motor_cmd[9].q = 1 # weight

    def SetQ(self, lq, rq):
        for i, id in enumerate(h1.LarmJointIndex):
            self.msg.motor_cmd[id].q = lq[i]
        for i, id in enumerate(h1.RarmJointIndex):
            self.msg.motor_cmd[id].q = rq[i]

    def MoveJ(self, lq, rq, duration = 1000):
        init_lq = np.array([self.msg.motor_cmd[id].q for id in h1.LarmJointIndex])
        init_rq = np.array([self.msg.motor_cmd[id].q for id in h1.RarmJointIndex])

        for i in range(duration):
            lq_t = init_lq + (lq - init_lq) * i / duration
            rq_t = init_rq + (rq - init_rq) * i / duration

            self.SetQ(lq_t, rq_t)
            self.write()
            time.sleep(0.001)

    def SetDefaultGain(self, kp = [100, 100, 100, 100], kd = [4, 4, 4, 4]):
        for i, id in enumerate(h1.LarmJointIndex):
            self.msg.motor_cmd[id].kp = kp[i]
            self.msg.motor_cmd[id].kd = kd[i]
        for i, id in enumerate(h1.RarmJointIndex):
            self.msg.motor_cmd[id].kp = kp[i]
            self.msg.motor_cmd[id].kd = kd[i]

class InspireHand(Publisher):
    def __init__(self):
        super().__init__(unitree_go.msg.dds_.MotorCmds_, "rt/inspire/cmd")
        self.msg.cmds  = [unitree_go.msg.dds_.MotorCmd_() for _ in range(12)]

        self.labels = {}
        self.labels["open"] = np.ones(6)
        self.labels["close"] = np.zeros(6)

        self.lq = np.zeros(6)
        self.rq = np.zeros(6)

    def pre_communication(self):
        for i in range(6):
            self.msg.cmds[i].q = self.lq[i]
            self.msg.cmds[i+6].q = self.rq[i]

    def ctrl(self, label):
        try:
            self.lq = self.labels[label]
            self.rq = self.labels[label]
            self.write()
        except :
            print(f"label {label} not found")