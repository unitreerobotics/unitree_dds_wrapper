from unitree_dds_wrapper.robots.trihand.trihand_sub_state import UnitreeTrihand as trihand_sub
import time
sub = trihand_sub()
sub.wait_for_connection()
while True:
    left_ms, right_msg = sub.sub()
    print(f"left: {left_ms} \n right: {right_msg}")
    time.sleep(0.001)