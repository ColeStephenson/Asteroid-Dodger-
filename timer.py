import math
import time

class Timer:

  def __init__(self, initial):
    self.initial = initial
    self.start = math.floor(time.time())

  def is_finished(self):
    now = math.floor(time.time())
    if now-self.start >= self.initial:
      return True
    else:
      return False

  def get_text(self):
    now = math.floor(time.time())
    return str(self.initial - (now - self.start))

  def get_image(self, font):
    return font.render(self.get_text(), False, (255, 255, 255), (0, 0, 0))