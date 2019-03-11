class bol(object):
  def __init__(self, f):
    self.f = f
  def __call__(self):
    return "<b>{}</b>".format(self.f())

class ita(object):
  def __init__(self, f):
    self.f = f
  def __call__(self):
    return "<i>{}</i>".format(self.f())

@bol
@ita
def sayhi():
  return 'hi'

print(sayhi())