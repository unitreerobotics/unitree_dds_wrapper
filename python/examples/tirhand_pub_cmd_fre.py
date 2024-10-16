from unitree_dds_wrapper.robots.trihand.trihand_pub_cmd_freq import UnitreeTrihand as trihand_pub
import numpy as np
import time
import math
th_pub = trihand_pub()
lkp = np.array([2,2,2,2,2,2,2])
lkd = np.array([0.2,0.2,0.2,0.2,0.2,0.2,0.2])
lq = np.array([0,0,0,0,0,0,0])
ldq = np.array([0,0,0,0,0,0,0])
ltau = np.array([0,0,0,0,0,0,0])
count = 1
dir = 1
th_pub.left_hand.kp = lkp
th_pub.left_hand.kd = lkd
th_pub.left_hand.dq = ldq
th_pub.left_hand.tau = ltau

# th_pub.right_hand.kp = lkp
# th_pub.right_hand.kd = lkd
# th_pub.right_hand.dq = ldq
# th_pub.right_hand.tau = ltau

def joint_poses_interp(poses, ratio=1.0):
    """
    poses: 是一个[T, N]维度数据， T代表时刻, N代表关节数量
    ratio: 代表T维度上的插值倍数, 例如: T=2 表示插值后的数据是[2T, N]
    return: 返回一个在T维度上对关节位置进行线性插值后的数据。
    """
    steps = poses.shape[0]
    joints =  poses.shape[1]
    steps_new = math.ceil(steps*ratio)
    xp = np.linspace(0, steps, steps) 
    x = np.linspace(0, steps, steps_new) 

    poses_new = None
    for j in range(joints):
        fp = poses[:, j]
        y = np.interp(x, xp, fp)
        poses_new = y.reshape(steps_new,1) if j==0 else np.hstack((poses_new, y.reshape(steps_new,1)))

    return poses_new

while True:
    q = [1 / 10000.0 * count * 1 for _ in range(7)]
    th_pub.left_hand.update_target_q(q)
    # th_pub.right_hand.update_target_q(q)
    count = count + dir
    if (count == 10000):
        dir = -1
    if (count == 0):
        dir = 1
    time.sleep(0.1)


