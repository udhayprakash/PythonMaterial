#!/usr/bin/python

from Tkinter import *


def GetValue():
    password = ent.get()
    print type(ent)
    print dir(ent)
    if password == 'UdhayPrakash':
        button['bg'] = 'green'
    else:
        ent.insert(0,'wrong password ')
        button['bg'] = 'red'





root = Tk()


lab = Label(root, text = 'Password')
ent = Entry(root, bg = 'white')
button = Button(root, text = 'Enter Password', command = GetValue)


ent.focus()

lab.pack(anchor = W)
ent.pack(anchor = W)
button.pack(ancho = E)


root.mainloop()
