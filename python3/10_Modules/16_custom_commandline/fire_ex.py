#!/usr/bin/env python
import fire

class Example(object):
  def hello(self, name='world'):
    """Says hello to the specified name."""
    return 'Hello {name}!'.format(name=name)

def main():
  fire.Fire(Example)

if __name__ == '__main__':
  main()
