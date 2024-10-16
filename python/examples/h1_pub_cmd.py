from unitree_dds_wrapper.robots.hg.hg_pub import LowCmd as pub
import numpy as np
import time
lowpub = pub()
lowpub.msg.mode_machine = 4
lowpub.msg.mode_pr = 3
while True:
    for i in  range(35):
        lowpub.msg.motor_cmd[i].mode = 1
        lowpub.msg.motor_cmd[i].q = i+10
        lowpub.msg.motor_cmd[i].dq = i+10
        lowpub.msg.motor_cmd[i].tau = i+10
        lowpub.msg.motor_cmd[i].kp = i+10
        lowpub.msg.motor_cmd[i].kd = i+10
    lowpub.write()
    print(f"push ok ")
    time.sleep
