from unitree_dds_wrapper.publisher import Publisher
from unitree_dds_wrapper.idl.unitree_hand import unitree_hg
import numpy as np
import time
class RIS_Mode:
    def __init__(self, id=0, status=0x01, timeout=0):
        self.motor_mode = 0
        self.id = id & 0x0F  # 4 bits for id
        self.status = status & 0x07  # 3 bits for status
        self.timeout = timeout & 0x01  # 1 bit for timeout

    def mode_to_uint8(self):
        self.motor_mode |= (self.id & 0x0F)  # 低 4 位 id
        self.motor_mode |= (self.status & 0x07) << 4  # 高 3 位 status 左移 4 位
        self.motor_mode |= (self.timeout & 0x01) << 7  # 高 1 位 timeout 左移 7 位
        return self.motor_mode
    
class UnitreeTrihandLeft_Right(Publisher):
    def __init__(self,topic="rt/dex3/left"):
        super().__init__(unitree_hg.msg.dds_.HandCmd_, topic)
        self.msg: unitree_hg.msg.dds_.HandCmd_
        self.msg.motor_cmd  = [unitree_hg.msg.dds_.MotorCmd_() for _ in range(7)]
        # self.set_static_tau()
        for i in range(7):
            ris_mode = RIS_Mode(id=i, status=0x01)  # 初始化 RIS_Mode
            motor_mode = ris_mode.mode_to_uint8()  # 获取组合后的 mode 值
            # print(f"motor mode:{motor_mode}")
            self.msg.motor_cmd[i].mode = motor_mode
        self.kp: np.array = np.zeros(7)
        self.kd: np.array = np.zeros(7)
        self.q: np.array = np.zeros(7)
        self.dq: np.array = np.zeros(7)
        self.tau: np.array = np.zeros(7)
    
    def pre_communication(self):
        motor_cmd = self.msg.motor_cmd
        kp, kd, q, dq, tau = self.kp, self.kd, self.q, self.dq, self.tau
        for i in range(7):
            motor_cmd[i].kp = kp[i]
            motor_cmd[i].kd = kd[i]
            motor_cmd[i].q = q[i]
            motor_cmd[i].dq = dq[i]
            motor_cmd[i].tau = tau[i]
    def set_static_tau(self):
        for i in range(7):
            ris_mode = RIS_Mode(id=i, status=0x06)  # 初始化 RIS_Mode
            motor_mode = ris_mode.mode_to_uint8()  # 获取组合后的 mode 值
            self.msg.motor_cmd[i].mode = motor_mode
        self.kp: np.array = np.zeros(7)
        self.kd: np.array = np.zeros(7)
        self.q: np.array = np.zeros(7)
        self.dq: np.array = np.full(7,1.5)
        self.tau: np.array = np.zeros(7)
        self.write()



class UnitreeTrihand:
    def __init__(self) -> None:
        self.left_hand = UnitreeTrihandLeft_Right(topic="rt/dex3/left/cmd")
        self.right_hand = UnitreeTrihandLeft_Right(topic="rt/dex3/right/cmd")
    def pub(self):
        self.left_hand.write()
        self.right_hand.write()
