from unitree_dds_wrapper.publisher import Publisher
from unitree_dds_wrapper.idl.unitree_hand import unitree_hg
from unitree_dds_wrapper.robots.trihand.trihand_sub_state import UnitreeTrihandLeftRight as  UnitreeTrihandLeftRightSub
import numpy as np
import time
import threading
import copy
class RIS_Mode:
    def __init__(self, id=0, status=0, timeout=0):
        self.motor_mode =0
        self.id = id & 0x0F  # 4 bits for id
        self.status = status & 0x07  # 3 bits for status
        self.timeout = timeout & 0x01  # 1 bit for timeout

    def mode_to_uint8(self):
        self.motor_mode|= (self.id & 0x0F)  # 低 4 位 id
        self.motor_mode |= (self.status & 0x07) << 4  # 高 3 位 status 左移 4 位
        self.motor_mode |= (self.timeout & 0x01) << 7  # 高 1 位 timeout 左移 7 位
        return self.motor_mode
class UnitreeTrihandLeftRight(Publisher):
    def __init__(self, pubtopic="rt/dex3/left", subtopic="rt/lf/dex3/left/state"):
        super().__init__(unitree_hg.msg.dds_.HandCmd_, pubtopic)
        self.msg: unitree_hg.msg.dds_.HandCmd_
        self.msg.motor_cmd = [unitree_hg.msg.dds_.MotorCmd_() for _ in range(7)]
        self.sub = UnitreeTrihandLeftRightSub(subtopic)
        
        for i in range(7):
            ris_mode = RIS_Mode(id=i, status=0x01)  # Initialize RIS_Mode
            motor_mode = ris_mode.mode_to_uint8()  # Get combined mode value
            self.msg.motor_cmd[i].mode = motor_mode
        
        # Initialize motor control arrays
        self.kp: np.array = np.zeros(7)  # Fixed kp value
        self.kd: np.array = np.zeros(7)   # Fixed kd value
        self.q: np.array = np.zeros(7)        # Current position q
        self.dq: np.array = np.zeros(7)       # Fixed dq value (if no velocity control)
        self.tau: np.array = np.zeros(7)      # Fixed tau value
        
        # Store the target positions
        self.target_q: np.array = np.zeros(7)
        self.current_q: np.array = np.zeros(7)
        # Start threads
        self.sub.wait_for_connection()
        self.sub_thread = threading.Thread(target=self.subscribe_position, daemon=True)
        self.pub_thread = threading.Thread(target=self.run_control_loop, daemon=True)
        
        self.sub_thread.start()
        self.pub_thread.start()
        
    def update_target_q(self, target_q):
        """Update the target positions for q only."""
        self.target_q = np.array(target_q)
        print(f"self.target_q:{self.target_q}")
        
    def compute_q_command(self):
        """Compute q command based on current position and target, using vectorized operations."""
        # Calculate the difference between the target and current position for each joint
        delta_q = self.target_q - self.q  # Shape: (7,)
        sign_delta_q = np.sign(delta_q)
        delta_q = np.clip(delta_q, -0.02, 0.02)
        self.q  = self.q + delta_q*sign_delta_q
        self.q = np.clip(self.q, 0.0, 2.0)
        """
        # Parameters for step size adjustment
        max_step_size = 0.05  # Maximum step size for large errors
        min_step_size = 0.001  # Minimum step size for small errors
        
        # Compute the absolute differences and the signs for each joint
        abs_delta_q = np.abs(delta_q)  # Shape: (7,)
        sign_delta_q = np.sign(delta_q)  # Get the sign of delta_q for each joint
        
        # For each joint, normalize its delta_q to adjust the step size between min and max
        # This normalizes each joint independently, no need to use the maximum across joints
        step_sizes = min_step_size + (max_step_size - min_step_size) * (abs_delta_q / (abs_delta_q + 1e-6))
        
        # Update q with the computed step sizes, preserving the direction of delta_q
        self.q += step_sizes * sign_delta_q  # Use sign_delta_q to preserve the direction
        
        # Ensure q is constrained to the range [0, 2] for all joints
        self.q = np.clip(self.q, 0.0, 2.0)
        """


    def pre_communication(self):
        """Prepare and send the motor commands, only updating q."""
        motor_cmd = self.msg.motor_cmd
        for i in range(7):
            motor_cmd[i].kp = self.kp[i]  # kp is fixed
            motor_cmd[i].kd = self.kd[i]  # kd is fixed
            motor_cmd[i].q = self.q[i]    # Update q
            motor_cmd[i].dq = self.dq[i]  # dq is fixed
            motor_cmd[i].tau = self.tau[i]  # tau is fixed

    def subscribe_position(self):
        """Thread function to subscribe to current position."""
        while True:
            # Assuming self.sub.q is being updated by UnitreeTrihandLeftRightSub
            self.q = self.sub.q  # Update current position q from the subscription
            self.current_q = self.sub.q
            time.sleep(0.01)  # Adjust the sleep time based on subscription rate

    def run_control_loop(self, freq=100):
        """Thread function to run the control loop at a fixed frequency."""
        interval = 1.0 / freq  # Calculate the time interval based on frequency

        while True:
            self.compute_q_command()  # Compute new q command
            print(f"self.q:{self.q}")
            self.pre_communication()  # Prepare the message
            self.write()      # Publish the message
            time.sleep(interval)      # Sleep to maintain the loop at the given frequency



class UnitreeTrihand:
    def __init__(self) -> None:
        self.left_hand = UnitreeTrihandLeftRight(pubtopic="rt/dex3/left/cmd",subtopic="rt/lf/dex3/left/state")
        # self.right_hand = UnitreeTrihandLeftRight(pubtopic="rt/dex3/right/cmd",subtopic="rt/lf/dex3/right/state")
    
    def getqpose(self):
        left_q = copy.deepcopy(self.left_hand.current_q)
        # right_q = copy.deepcopy(self.right_hand.current_q)
        # return np.concatenate((left_q, right_q))