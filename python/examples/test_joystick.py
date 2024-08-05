from unitree_dds_wrapper.utils.joystick import LogicJoystick
import time
from unitree_dds_wrapper.idl import unitree_go

joy = LogicJoystick()
joy1 = LogicJoystick()
lowstate = unitree_go.msg.dds_.LowState_()

while True:
    joy.update()
    print("lx: ", joy.lx.data)

    lowstate.wireless_remote = joy.combine()
    joy1.extract(lowstate.wireless_remote)
    print("lx in dds: ", joy1.lx.data)

    time.sleep(0.1)