import numpy as np
import unitree_dds_wrapper.idl
from unitree_dds_wrapper.robots import h1
import time

class H1ArmController:
    def __init__(self, urdf_path = None):
        self.lowstate = h1.sub.LowState()
        self.lowstate.wait_for_connection()
        self.armsdk = h1.pub.ArmSdk()
        for id in h1.JointIndex:
            self.armsdk.msg.motor_cmd[id].q = self.lowstate.msg.motor_state[id].q

        if urdf_path is not None:
            import pinocchio as pin
            from unitree_dds_wrapper.utils.pin import BuildReducedModel
            model = pin.buildModelFromUrdf(urdf_path)
            LarmJointsToLock = list(set(h1.JointLists) - set([ # Lock all joints except the specified joints
                "left_shoulder_pitch_joint",
                "left_shoulder_roll_joint",
                "left_shoulder_yaw_joint",
                "left_elbow_joint",
            ]))
            self.larm_model = BuildReducedModel(model, LarmJointsToLock)
            RarmJointsToLock = list(set(h1.JointLists) - set([ # Lock all joints except the specified joints
                "right_shoulder_pitch_joint",
                "right_shoulder_roll_joint",
                "right_shoulder_yaw_joint",
                "right_elbow_joint",
            ]))
            self.rarm_model = BuildReducedModel(model, RarmJointsToLock)

    def LockWaist(self):
        self.armsdk.msg.motor_cmd[h1.JointIndex.WaistYaw].kp = 200
        self.armsdk.msg.motor_cmd[h1.JointIndex.WaistYaw].kd = 5

        init_q = self.lowstate.msg.motor_state[h1.JointIndex.WaistYaw].q
        target_q = 0.
        duration = 1000

        for i in range(duration):
            q = init_q + (target_q - init_q) * i / duration
            self.armsdk.msg.motor_cmd[h1.JointIndex.WaistYaw].q = q
            self.armsdk.write()
            time.sleep(0.001)

    def SetArmQWithGravity(self, lq, rq):
        assert hasattr(self, "larm_model") and hasattr(self, "rarm_model"), \
            "Please provide urdf_path when initializing H1ArmController"

        l_gravity = self.larm_model.gravity(lq)
        r_gravity = self.rarm_model.gravity(rq)

        for i, id in enumerate(h1.LarmJointIndex):
            self.armsdk.msg.motor_cmd[id].q = lq[i]
            self.armsdk.msg.motor_cmd[id].tau = l_gravity[i]
        for i, id in enumerate(h1.RarmJointIndex):
            self.armsdk.msg.motor_cmd[id].q = rq[i]
            self.armsdk.msg.motor_cmd[id].tau = r_gravity[i]