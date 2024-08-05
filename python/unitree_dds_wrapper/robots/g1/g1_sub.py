from unitree_dds_wrapper.idl import unitree_hg, unitree_go
from unitree_dds_wrapper.subscription import Subscription
from unitree_dds_wrapper.utils.joystick import Joystick
import struct
import numpy as np

class LowCmd(Subscription):
    def __init__(self, participant = None, topic: str = "rt/lowcmd_hx"):
        super().__init__(unitree_hg.msg.dds_.LowCmd_, topic=topic, participant=participant)
        self.msg: unitree_hg.msg.dds_.LowCmd_

        class ArmData:
            def __init__(self):
                self.q: np.array = np.zeros(5)
                self.dq: np.array = np.zeros(5)
                self.tau: np.array = np.zeros(5)

        self.l = ArmData()
        self.r = ArmData()

        class LegData:
            def __init__(self):
                class SingleData:
                    def __init__(self):
                        self.q: np.array = np.zeros(6)
                        self.dq: np.array = np.zeros(6)
                        self.tau: np.array = np.zeros(6)
                self.l = SingleData()
                self.r = SingleData()
        self.leg = LegData()


    def post_communication(self):
        # ----- Arm Cmd ----- #
        for i in range(5):
            self.l.q[i] = self.msg.motor_cmd[i + 13].q
            self.l.dq[i] = self.msg.motor_cmd[i + 13].dq
            self.l.tau[i] = self.msg.motor_cmd[i + 13].tau
            self.r.q[i] = self.msg.motor_cmd[i + 18].q
            self.r.dq[i] = self.msg.motor_cmd[i + 18].dq
            self.r.tau[i] = self.msg.motor_cmd[i + 18].tau


class LowState(Subscription):
    def __init__(self, participant = None, topic: str = "rt/lowstate_hx"):
        super().__init__(unitree_hg.msg.dds_.LowState_, topic=topic, participant=participant)
        self.msg: unitree_hg.msg.dds_.LowState_
        self.joystick = Joystick()

        class ArmData:
            def __init__(self):
                self.q: np.array = np.zeros(5)
                self.dq: np.array = np.zeros(5)
                self.tau: np.array = np.zeros(5)
        self.l = ArmData()
        self.r = ArmData()


        class SinglegData:
            def __init__(self):
                self.q: np.array = np.zeros(6)
                self.dq: np.array = np.zeros(6)
                self.tau: np.array = np.zeros(6)
        class LegData:
            def __init__(self):
                self.l = SinglegData()
                self.r = SinglegData()
        self.leg = LegData()

    def update(self):
        if self.msg is None:
            return

        with self.lock:    
            self.joystick.extract(self.msg.wireless_remote)

    
    def post_communication(self):
        # ----- Arm State ----- #
        for i in range(5):
            self.l.q[i] = self.msg.motor_state[i + 13].q
            self.l.dq[i] = self.msg.motor_state[i + 13].dq
            self.l.tau[i] = self.msg.motor_state[i + 13].tau_est
            self.r.q[i] = self.msg.motor_state[i + 18].q
            self.r.dq[i] = self.msg.motor_state[i + 18].dq
            self.r.tau[i] = self.msg.motor_state[i + 18].tau_est
        
        # ----- Leg State ----- #
        for i in range(6):
            self.leg.l.q[i] = self.msg.motor_state[i].q
            self.leg.l.dq[i] = self.msg.motor_state[i].dq
            self.leg.l.tau[i] = self.msg.motor_state[i].tau_est
            self.leg.r.q[i] = self.msg.motor_state[i + 6].q
            self.leg.r.dq[i] = self.msg.motor_state[i + 6].dq
            self.leg.r.tau[i] = self.msg.motor_state[i + 6].tau_est

class UnitreeHand(Subscription):
    def __init__(self):
        super().__init__(unitree_go.msg.dds_.MotorStates_, "rt/hand/state")
        # self.msg.states = [unitree_go.msg.dds_.MotorState_() for _ in range(2 * 7)]

        class HandData:
            def __init__(self):
                self.q: np.array = np.zeros(7)
                self.dq: np.array = np.zeros(7)
                self.tau: np.array = np.zeros(7)
        self.l = HandData()
        self.r = HandData()

    def post_communication(self):
        for i in range(7):
            self.l.q[i] = self.msg.states[i].q
            self.l.dq[i] = self.msg.states[i].dq
            self.l.tau[i] = self.msg.states[i].tau_est
            self.r.q[i] = self.msg.states[i + 7].q
            self.r.dq[i] = self.msg.states[i + 7].dq
            self.r.tau[i] = self.msg.states[i + 7].tau_est