from unitree_dds_wrapper.robots.trihand.trihand_pub_state import UnitreeTrihand as trihand_pub
import numpy as np
import time
th_pub = trihand_pub()
lkp = np.array([100,100,100,100,100,100,100])
lkd = np.array([100,100,100,100,100,100,100])
lq = np.array([100,100,100,100,100,100,100])
ldq = np.array([100,100,100,100,100,100,100])
ltau = np.array([100,100,100,100,100,100,100])

while True:
    th_pub.l.kp = lkp
    th_pub.l.kd = lkd
    th_pub.l.q = lq
    th_pub.l.dp = ldq
    th_pub.l.tau = ltau

    th_pub.r.kp = rkp
    th_pub.r.kd = rkd
    th_pub.r.q = rq
    th_pub.r.dp = rdq
    th_pub.r.tau = rtau
    th_pub.write()
    print(f"push ok ")
    time.sleep
