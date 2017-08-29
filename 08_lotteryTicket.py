#!/usr/bin/python
"""
Purpose:
lottery ticket
  winning ticket = 'Ajvhvj87689'
  ask the user to input the ticket number in run-time and evaluate
"""
winningTicket = 'Ajvhvj87689'

userTicket = raw_input('Enter the ticket number:');

if userTicket == winningTicket:
    print 'Congratulation!You won the lottery!'
else:
    print 'Sorry! Try again.'
