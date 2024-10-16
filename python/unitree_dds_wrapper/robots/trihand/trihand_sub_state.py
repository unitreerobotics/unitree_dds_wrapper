from unitree_dds_wrapper.idl.unitree_hand import unitree_hg
from unitree_dds_wrapper.subscription import Subscription
import numpy as np

class UnitreeTrihandLeftRight(Subscription):
    def __init__(self,topic="rt/lf/dex3/left/state"):
        super().__init__(unitree_hg.msg.dds_.HandState_, topic)
        self.q: np.array = np.zeros(7)
        self.dq: np.array = np.zeros(7)
        self.tau: np.array = np.zeros(7)
    def post_communication(self):
        for i in range(7):
            self.q[i] = self.msg.motor_state[i].q
            self.dq[i] = self.msg.motor_state[i].dq
            self.tau[i] = self.msg.motor_state[i].tau_est
    def get_qpose(self):
        with self.lock:
            temp_q = self.q.copy()
            return temp_q


class UnitreeTrihand:
    def __init__(self) -> None:
        self.left_hand = UnitreeTrihandLeftRight(topic="rt/dex3/left/state")
        self.right_hand = UnitreeTrihandLeftRight(topic="rt/dex3/right/state")
    def wait_for_connection(self):
        self.left_hand.wait_for_connection()
        self.right_hand.wait_for_connection()
    def sub(self):
        # print(f"sub:{self.left_hand.get_qpose()},sub2:{self.right_hand.get_qpose()}")
        return self.left_hand.get_qpose(), self.right_hand.get_qpose()
        # return np.full(7,0), self.right_hand.get_qpose()


