from unitree_dds_wrapper.robots.h1.h1_sub import LowState as sub

h1_lowstatesub = sub()
h1_lowstatesub.wait_for_connection()
while True:
    print(h1_lowstatesub.msg)