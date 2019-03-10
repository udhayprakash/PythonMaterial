import Tkinter as tk
import threading, Queue

#Globals
WIDE = 200         # image dimensions
HIGH = 200         #

REAL_FROM = -2     # bounds of fractal in the complex plane
REAL_TO   =  1     #
IMAG_FROM = -1.5   # imaginary coords => y-direction
IMAG_TO   =  1.5   #

N = 64

                
class MandelbrotWorker(threading.Thread):
    def __init__(self, aQueue, imgWidth, imgHeight, bounds, **kwargs):
        threading.Thread.__init__(self)
        self.setDaemon(1)
        self.imgWidth = imgWidth 
        self.imgHeight = imgHeight
        self.fwidth = float(imgWidth)
        self.fheight = float(imgHeight)
        self.mapLeft = bounds[0]
        self.mapTop = bounds[3]
        self.mapWidth = bounds[1] - bounds[0]
        self.mapHeight = bounds[3] - bounds[2]
        self.resultQueue = aQueue
        self.n = N
        self.start()
        
    def run(self):
        for x in xrange(self.imgWidth):
            for y in xrange(self.imgHeight):
                percx = x/self.fwidth
                percy = y/self.fheight
                xp = self.mapLeft + percx*self.mapWidth
                yp = self.mapTop - percy*self.mapHeight
                o = complex(0,0)
                z = complex(xp,yp)
                colorcode = 0
                for trials in xrange(self.n):
                    if abs(o) <= 2.0:
                        o = o**2 + z
                    else:
                        colorcode = trials
                        break
                self.resultQueue.put((x,y,colorcode))


class ThreadedFractal(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.on_close)        
        self.status = tk.Label(self)
        self.status.pack(fill='x')
        self.display = tk.Label(self)
        self.display.pack()
        self.img = tk.PhotoImage(width=WIDE, height=HIGH)
        self.display.config(image=self.img)
        self.count = 0
        self.totalPixels = WIDE*HIGH 
        self.queue = Queue.Queue()
        self.rgb = []
        self.make_colours()
        self.go()
        
    def make_colours(self):
        for i in xrange(N):
            r = i*7%200 + 55
            g = i*9%200 + 55
            b = i*11%200 + 55
            colour = '#%02x%02x%02x' %(r,g,b)
            self.rgb.append(colour)

    def scheduler(self):
        self.after(0, self.poll)
            
    def go(self):
        self.workerThread = MandelbrotWorker(self.queue, WIDE, HIGH,
                                    (REAL_FROM,REAL_TO,IMAG_FROM,IMAG_TO))
        self.after(500, self.poll)
                
    def poll(self):
        if self.count < self.totalPixels:
            try:
                x,y,code = self.queue.get_nowait()
            except Queue.Empty:
                pass
            else:
                colour = self.rgb[code]
                self.img.put(colour, to=(x,y))
                self.count += 1
                self.status.config(text='%s of %s pixels' %(self.count,
                                                            self.totalPixels))
            self.after_idle(self.scheduler)
            
    def on_close(self):
        self.master.destroy()


root = tk.Tk()
root.withdraw()
app = ThreadedFractal(root)
app.mainloop()