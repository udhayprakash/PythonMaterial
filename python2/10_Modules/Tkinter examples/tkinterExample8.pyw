from Tkinter import *           #This interface allow us to draw windows


def DrawList():
        plist = ['Liz','Tom','Chi']

        for item in plist:
                listbox.insert(END,item);
                
        
root = Tk()                     #This creates a window, but it won't show up

listbox = Listbox(root)
button = Button(root,text = "press me",command = DrawList)

button.pack()
listbox.pack()                  #this tells the listbox to come out
root.mainloop()                 #This command will tell the window come out