#!/usr/bin/python

__author__ = ''
"""
purpose: Menu-Driven Bank User Interface
usage: python scriptName.py
"""

import consoleColor as cons

def test():
  """Simple test for color_console."""
  default_colors = cons.get_text_attr()
  default_bg = default_colors & 0x0070

  windowLength = 80
  cons.set_text_attr(cons.FOREGROUND_BLUE | cons.BACKGROUND_GREY |
                     cons.FOREGROUND_INTENSITY | cons.BACKGROUND_INTENSITY)

  print "_" * windowLength
  print "|" * windowLength
  print "-" * windowLength
  cons.set_text_attr(cons.FOREGROUND_BLUE | cons.BACKGROUND_BLUE |
                     cons.FOREGROUND_INTENSITY | cons.BACKGROUND_INTENSITY)

  print "XYZ BANK".center(windowLength)
  cons.set_text_attr(cons.FOREGROUND_YELLOW | cons.BACKGROUND_BLUE |
                     cons.FOREGROUND_INTENSITY |cons.BACKGROUND_INTENSITY)

  print "FINANCIAL TRANSACTION INTERFACE ".center(windowLength)
  cons.set_text_attr(cons.FOREGROUND_YELLOW | cons.BACKGROUND_BLUE | cons.BACKGROUND_INTENSITY)

  print '@xyz company, interface version 0.0012'.rjust(windowLength)
  cons.set_text_attr(cons.BACKGROUND_GREY | cons.BACKGROUND_INTENSITY |
                     cons.FOREGROUND_INTENSITY | cons.FOREGROUND_BLACK)

  print  'FINANCIAL TRANSACTION MENU'  # \                             #Style.BRIGHT
  # + '_'*len('FINANCIAL TRANSACTION MENU')
  cons.set_text_attr(cons.BACKGROUND_BLACK | default_bg |
                     cons.FOREGROUND_INTENSITY | cons.FOREGROUND_YELLOW)

  print  '\n1. create an Account' \
         '\n2. Transact from existing Account' \
         '\n\ta. DEPOSIT ' \
         '\n\tb. WITHDRAW' \
         '\n\tc. BALANCE ENQUIRY' \
         '\n3. Delete an existing Account '
  choice = raw_input("Please Enter the interger, corresponding to your choice:")

  cons.set_text_attr(cons.FOREGROUND_BLUE | cons.BACKGROUND_GREY |
                     cons.FOREGROUND_INTENSITY | cons.BACKGROUND_INTENSITY)

  print "." * windowLength
  print "@" * windowLength
  print "-" * windowLength
  cons.set_text_attr( default_bg )
  cons.set_text_attr(default_colors)

if __name__ == "__main__":
  test()


'''
cons.set_text_attr(cons.FOREGROUND_BLUE | default_bg |
                     cons.FOREGROUND_INTENSITY)
  print '==========================================='
  cons.set_text_attr(cons.FOREGROUND_BLUE | cons.BACKGROUND_GREY |
                     cons.FOREGROUND_INTENSITY | cons.BACKGROUND_INTENSITY)
  print 'And Now for Something',
  cons.set_text_attr(cons.FOREGROUND_RED | cons.BACKGROUND_GREY |
                     cons.FOREGROUND_INTENSITY | cons.BACKGROUND_INTENSITY)
  print 'Completely Different!',
  cons.set_text_attr(default_colors)
  print
  cons.set_text_attr(cons.FOREGROUND_RED | default_bg |
                     cons.FOREGROUND_INTENSITY)
  print '==========================================='


'''