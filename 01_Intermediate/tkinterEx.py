import tkinter as tk
from queue import Queue
from threading import Thread, Event
from time import sleep
import random 

def generate_data(my_queue, event):
    while not event.is_set():
        data ={}
        data['value_sensor_1'] = random()
        data['value_sensor_2'] = random()
        my_queue.put(data)        
        sleep(0.7)
      

class Application(tk.Frame):
    def __init__(self, my_queue, thread_kill_event, master=None):
        super().__init__(master)
        self.my_queue = my_queue        
        self.thread_kill_event = thread_kill_event
        self.pack()
        self.create_widgets()
        self.update_labels()

    def create_widgets(self):
        self.label_sensor_1 = tk.Label(self, bg='purple', height=5, width=10, 
                                       text='Sensor 1')
        self.label_sensor_1.pack(side='left')
        self.label_sensor_2 = tk.Label(self, bg='yellow', height=5, width=10,
                                       text='Sensor 2')
        self.label_sensor_2.pack(side='right')
        self.quit = tk.Button(self, text='QUIT', fg='red',
                              command=self.exit_cleanup)
        self.quit.pack(side='bottom')

    def update_labels(self):
        self.master.after(500, self.update_labels)
        if not self.my_queue.empty():
            data = self.my_queue.get()
            if data['value_sensor_1'] < 0.5:
                self.label_sensor_1['bg'] = 'purple'
            else:
                self.label_sensor_1['bg'] = 'pink'
            if data['value_sensor_2'] < 0.5:
                self.label_sensor_2['bg'] = 'yellow'
            else:
                self.label_sensor_2['bg'] = 'blue'

    def exit_cleanup(self):
        self.thread_kill_event.set()
        self.master.destroy()

def main():
    my_queue = Queue()
    my_event = Event()
    my_thread = Thread(target=generate_data, args=(my_queue, my_event, ))
    my_thread.start()
    root = tk.Tk()
    app = Application(my_queue, my_event, master=root)
    app.master.title('TKinter Thread Demo')
    app.mainloop()

if __name__ == '__main__':
    main()