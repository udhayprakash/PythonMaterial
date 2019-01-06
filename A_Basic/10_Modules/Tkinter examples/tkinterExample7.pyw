from Tkinter import *


def Call():
        lab= Label(root, text = 'You pressed\nthe button')
        lab.pack()
        button['bg'] = 'blue'
        button['fg'] = 'white'

root = Tk()
root.geometry('100x110+350+70')
button = Button(root, text = 'Press me', command = Call)
button.pack()

root.mainloop()