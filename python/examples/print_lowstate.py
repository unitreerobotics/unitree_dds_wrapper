from unitree_dds_wrapper.robots import go2
import time

lowstate = go2.sub.LowState()
lowstate.wait_for_connection()

while True:
  lowstate.update()
  print(f"Motor 0 : q {lowstate.msg.motor_state[0].q}")
  print(f"Joystick A: ", "pressed" if lowstate.joystick.A.pressed else "released")
  time.sleep(0.5)