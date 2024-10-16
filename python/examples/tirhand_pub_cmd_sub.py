from unitree_dds_wrapper.robots.trihand.trihand_pub_cmd import UnitreeTrihand as trihand_pub
import numpy as np
import time
from unitree_dds_wrapper.robots.trihand.trihand_sub_state import UnitreeTrihand as trihand_sub
import time
from multiprocessing import Process, shared_memory, Queue, Manager, Event, Lock
def hand_control_process():
    sub = trihand_sub()
    while True:
        left_ms, right_msg = sub.sub()
        print(f"hand_control_process: {left_ms}")
        time.sleep(0.01)

# hand_process = Process(target=hand_control_process)
# hand_process.start()
np.set_printoptions(linewidth=200, suppress=False, precision=6)
sub = trihand_sub()
sub.wait_for_connection()
th_pub = trihand_pub()
lkp = np.array([1.5,1.5,1.5,1.5,1.5,1.5,1.5])
lkd = np.array([0.06,0.06,0.06,0.06,0.06,0.06,0.06])
lq = np.array([0,0,0,0,0,0,0])
ldq = np.array([0,0,0,0,0,0,0])
ltau = np.array([0,0,0,0,0,0,0])
count = 1
dir = 1
while True:
    # q = [1 / 100.0 * count * 1 for _ in range(7)]
    # th_pub.left_hand.kp = lkp
    # th_pub.left_hand.kd = lkd
    # th_pub.left_hand.q = q 
    # th_pub.left_hand.dq = ldq
    # th_pub.left_hand.tau = ltau

    # th_pub.right_hand.kp = lkp
    # th_pub.right_hand.kd = lkd
    # th_pub.right_hand.q = q
    # th_pub.right_hand.dq = ldq
    # th_pub.right_hand.tau = ltau
    # th_pub.pub()

    print(f"push ok ")
    
    left_ms, right_msg = sub.sub()
    
    count = count + dir
    if (count == 100):
        dir = -1
    if (count == 0):
        dir = 1
    time.sleep(0.01)
    print(f"q:\t{np.array(0)} \nl:\t{left_ms} \nr:\t{right_msg}")