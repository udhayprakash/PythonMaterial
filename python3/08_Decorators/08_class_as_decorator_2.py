class sty(object):
  def __init__(self, tag):
    self.tag = tag
  def __call__(self, f):
    def newf():
      return "<{tag}>{res}</{tag}>".format(res=f(), tag=self.tag)
    return newf

@sty('b')
@sty('i')
def sayhi():
  return 'hi'

print(sayhi())