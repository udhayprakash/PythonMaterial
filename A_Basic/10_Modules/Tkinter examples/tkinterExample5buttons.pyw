from Tkinter import *

def Pressed():                          #function
        print 'buttons are cool'

root = Tk()                             #main window
button = Button(root, text = 'Press', command = Pressed)
button.pack(pady=20, padx = 20)
Pressed()
root.mainloop()