from unitree_dds_wrapper.publisher import Publisher
from unitree_dds_wrapper.subscription import Subscription
from unitree_dds_wrapper.idl import unitree_go
import time

msg_type = unitree_go.msg.dds_.LowState_
pub = Publisher(message=msg_type, topic="rt/test_dds")
sub = Subscription(message=msg_type, topic="rt/test_dds")

while True:
  pub.msg.level_flag = 1 - pub.msg.level_flag
  pub.write()
  time.sleep(0.5)

  print("send: ", pub.msg.level_flag)

  if sub.msg:
    print("receive: ", sub.msg.level_flag)