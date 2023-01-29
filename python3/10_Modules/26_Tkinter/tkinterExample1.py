from tkinter import *


class Application(Frame):
    def sayHi(self):
        print("Hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hiThere = Button(self)
        self.hiThere["text"] = ("Hello",)
        self.hiThere["command"] = self.sayHi

        self.hiThere.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
