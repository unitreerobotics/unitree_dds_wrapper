from unitree_dds_wrapper.publisher import Publisher
from unitree_dds_wrapper.idl.unitree_hand import unitree_hg
import numpy as np


class UnitreeTrihand(Publisher):
    def __init__(self):
        super().__init__(unitree_hg.msg.dds_.HandState_, "rt/hand/state")
        self.msg: unitree_hg.msg.dds_.HandState_
        self.msg.motor_state  = [unitree_hg.msg.dds_.MotorState_() for _ in range(2 * 7)]

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
            self.msg.motor_state[i].kp = self.l.kp[i]
            self.msg.motor_state[i].kd = self.l.kd[i]
            self.msg.motor_state[i].q = self.l.q[i]
            self.msg.motor_state[i].dq = self.l.dq[i]
            self.msg.motor_state[i].tau = self.l.tau[i]
            self.msg.motor_state[i+7].kp = self.r.kp[i]
            self.msg.motor_state[i+7].kd = self.r.kd[i]
            self.msg.motor_state[i+7].q = self.r.q[i]
            self.msg.motor_state[i+7].dq = self.r.dq[i]
            self.msg.motor_state[i+7].tau = self.r.tau[i]