from unitree_dds_wrapper.robots import go2
from cyclonedds.domain import DomainParticipant
import time

participant0 = DomainParticipant(domain_id=0)
participant1 = DomainParticipant(domain_id=1)

lowstate0 = go2.pub.LowState(participant=participant0)
lowstate1 = go2.pub.LowState(participant=participant1)

while True:
    lowstate0.msg.crc = 1- lowstate0.msg.crc
    lowstate0.write()

    lowstate1.msg.level_flag = 1- lowstate1.msg.level_flag
    lowstate1.write()
    time.sleep(1)