from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.pub import DataWriter

class Publisher:
  """
  message: Message type
  topic: Topic name
  """
  def __init__(self, message, topic, participant = None):
    self._participant = participant if participant else DomainParticipant()
    self._topic = Topic(self._participant, topic, message)
    self._writer = DataWriter(self._participant, self._topic)
    self.msg = message()

  def write(self):
    self.pre_communication()
    self._writer.write(self.msg)
    self.post_communication()

  def post_communication(self):
    pass

  def pre_communication(self):
    pass