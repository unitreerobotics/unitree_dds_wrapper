from unitree_dds_wrapper.idl.unitree_go.msg import dds_
from unitree_dds_wrapper.subscription import Subscription
from unitree_dds_wrapper.utils.joystick import Joystick
import struct
import numpy as np

class LowCmd(Subscription):
    def __init__(self, participant = None, topic: str = "rt/lowcmd"):
        super().__init__(dds_.LowCmd_, topic=topic, participant=participant)
        self.msg = dds_.LowCmd_()

class LowState(Subscription):
    def __init__(self, participant = None, topic: str = "rt/lowstate"):
        super().__init__(dds_.LowState_, topic=topic, participant=participant)
        self.msg: dds_.LowState_
        self.joystick = Joystick()

        class ArmData:
            def __init__(self):
                self.q: np.array = np.zeros(4)
                self.dq: np.array = np.zeros(4)
                self.tau: np.array = np.zeros(4)
        self.l = ArmData()
        self.r = ArmData()

    def update(self):
        with self.lock:            
            self.joystick.extract(self.msg.wireless_remote)

    
    def post_communication(self):
        # ----- Arm State ----- #
        for attr in ["q", "dq", "tau"]:
            setattr(self.r, attr, np.array([getattr(self.msg.motor_state[i+12], (attr if attr != "tau" else "tau_est")) for i in range(4)]))
            setattr(self.l, attr, np.array([getattr(self.msg.motor_state[i+16], (attr if attr != "tau" else "tau_est")) for i in range(4)]))