from unitree_dds_wrapper.idl.unitree_go.msg import dds_
from unitree_dds_wrapper.publisher import Publisher
import struct
from unitree_dds_wrapper.utils.crc import crc32

class LowCmd(Publisher):
  def __init__(self, participant = None, topic = "rt/lowcmd",):
    super().__init__(dds_.LowCmd_, topic, participant)
    self.msg: dds_.LowCmd_
    self.__packCRCformat = '<4B4IH2x' \
      + 'B3x5f3I' * len(self.msg.motor_cmd) \
      + '4B' + '55Bx2I'

  def pre_communication(self):
    self.__pack_crc()

  def __pack_crc(self):
    rawdata = []
    rawdata.extend(self.msg.head)
    rawdata.append(self.msg.level_flag)
    rawdata.append(self.msg.frame_reserve)
    rawdata.extend(self.msg.sn)
    rawdata.extend(self.msg.version)
    rawdata.append(self.msg.bandwidth)
    for i in range(len(self.msg.motor_cmd)):
      rawdata.append(self.msg.motor_cmd[i].mode)
      rawdata.append(self.msg.motor_cmd[i].q)
      rawdata.append(self.msg.motor_cmd[i].dq)
      rawdata.append(self.msg.motor_cmd[i].tau)
      rawdata.append(self.msg.motor_cmd[i].kp)
      rawdata.append(self.msg.motor_cmd[i].kd)
      rawdata.extend(self.msg.motor_cmd[i].reserve)
    rawdata.append(self.msg.bms_cmd.off)
    rawdata.extend(self.msg.bms_cmd.reserve)
    rawdata.extend(self.msg.wireless_remote)
    rawdata.extend(self.msg.led)
    rawdata.extend(self.msg.fan)
    rawdata.append(self.msg.gpio)
    rawdata.append(self.msg.reserve)
    rawdata.append(self.msg.crc)

    packdata = struct.pack(self.__packCRCformat, *rawdata)
    calcdata = []
    calclen = (len(packdata)>>2)-1
    for i in range(calclen):
      d = ((packdata[i*4+3] << 24) | (packdata[i*4+2] << 16) | (packdata[i*4+1] << 8) | (packdata[i*4]))
      calcdata.append(d)

    self.msg.crc = crc32(calcdata)


class LowState(Publisher):
  def __init__(self, participant = None, topic = "rt/lowstate"):
    super().__init__(dds_.LowState_, topic, participant)
    self.msg: dds_.LowState_

class MotorStates(Publisher):
  def __init__(self, participant = None, topic = "rt/motorstates"):
    super().__init__(dds_.MotorStates_, topic, participant)
    self.msg: dds_.MotorStates_

class MotorCmds(Publisher):
  def __init__(self, participant = None, topic = "rt/motorcmds"):
    super().__init__(dds_.MotorCmds_, topic, participant)
    self.msg: dds_.MotorCmds_

class ImuState(Publisher):
  def __init__(self, participant = None, topic = "rt/imustate"):
    super().__init__(dds_.IMUState_, topic, participant)
    self.msg: dds_.IMUState_