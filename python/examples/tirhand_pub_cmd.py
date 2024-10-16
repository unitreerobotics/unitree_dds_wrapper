from unitree_dds_wrapper.robots.trihand.trihand_pub_cmd import UnitreeTrihand as trihand_pub
import numpy as np
import time
th_pub = trihand_pub()
lkp = np.array([2,2,2,2,2,2,2])
lkd = np.array([0.2,0.2,0.2,0.2,0.2,0.2,0.2])
lq = np.array([0,0,0,0,0,0,0])
ldq = np.array([0,0,0,0,0,0,0])
ltau = np.array([1,1,1,1,1,1,1])
count = 1
dir = 1
while True:
    q = [1 / 100.0 * count * 1 for _ in range(7)]
    th_pub.left_hand.kp = lkp
    th_pub.left_hand.kd = lkd
    th_pub.left_hand.q = q 
    th_pub.left_hand.dq = ldq
    th_pub.left_hand.tau = ltau

    th_pub.right_hand.kp = lkp
    th_pub.right_hand.kd = lkd
    th_pub.right_hand.q = q
    th_pub.right_hand.dq = ldq
    th_pub.right_hand.tau = ltau
    th_pub.pub()

    print(f"push ok ")
    

    count = count + dir
    if (count == 100):
        dir = -1
    if (count == 0):
        dir = 1
    time.sleep(0.01)