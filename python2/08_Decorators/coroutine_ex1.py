class Task(object):
    taskid = 0
    def __init__(self,target):
        Task.taskid += 1
        self.tid = Task.taskid # Task ID
        self.target = target # Target coroutine
        self.sendval = None # Value to send
    def run(self):
        return self.target.send(self.sendval)


# A very simple generator
def foo():
    """
    >>> t1 = Task(foo()) # Wrap in a Task
    >>> t1.run()
    Part 1
    >>> t1.run()
    Part 2
    >>>
    """
    print 'Part 1'
    yield
    print 'Part 2'
    yield


############################
class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}

    def new(self,target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def schedule(self,task):
        self.ready.put(task)

    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            result = task.run()
            self.schedule(task)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
