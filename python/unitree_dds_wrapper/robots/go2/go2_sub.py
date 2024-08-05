from unitree_dds_wrapper.idl.unitree_go.msg import dds_
from unitree_dds_wrapper.subscription import Subscription
from unitree_dds_wrapper.utils.joystick import Joystick
import struct

class LowCmd(Subscription):
  def __init__(self, participant = None, topic: str = "rt/lowcmd"):
    super().__init__(dds_.LowCmd_, topic=topic, participant=participant)
    self.msg: dds_.LowCmd_

class LowState(Subscription):
  def __init__(self, participant = None, topic: str = "rt/lowstate"):
    super().__init__(dds_.LowState_, topic=topic, participant=participant)
    self.msg: dds_.LowState_
    self.joystick = Joystick()

  def update(self):
    """
    The corresponding information is extracted based on the current lowstate    
    """
    if self.msg is None:
      return
    
    with self.lock:    
      self.joystick.extract(self.msg.wireless_remote)


class MotorStates(Subscription):
  def __init__(self, participant = None, topic: str = "rt/motor_states"):
    super().__init__(dds_.MotorStates_, topic=topic, participant=participant)
    self.msg: dds_.MotorStates_

class MotorCmds(Subscription):
  def __init__(self, participant = None, topic: str = "rt/motor_cmds"):
    super().__init__(dds_.MotorCmds_, topic=topic, participant=participant)
    self.msg: dds_.MotorCmds_
