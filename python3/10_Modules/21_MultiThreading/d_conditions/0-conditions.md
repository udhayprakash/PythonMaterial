## ITC - Inter-Thread Communication

- process of communication between threads, even some data need
  to shared among themselves
- condition object has Five states:

  - acquire()
  - notify()
  - notifyAll()
  - wait()
  - release()

- acquire() Method:

  - When we want to obtain or takeover any condition object for inter-threading communication then we always used acquire() method.
  - The acquire() method is compulsory when we want to implement inter-thread communication using condition class.
  - When we use this method suddenly threads obtain the internal lock system.
  - Syntax: condition_object.acquire()

- notify() Method:

  - When we want to send a notification to only one thread that is in waiting state then we always use notify() method.
  - Here if one thread wants to be condition object up-gradation then notify() is used.
  - Syntax :condition_object.notify()

- notifyAll() Method:

  - Here the notifyAll() method is used to send notifications for all waiting threads.
  - If all threads are waiting for condition object updating then notifyAll() will use.
  - Syntax: condition_object.notifyAll()

- wait(time) Method:
  - The wait() method can be used to make a thread wait till the notification got and also till the given time will end.
  - In simple words we can say that thread is to wait until the execution of the notify() method is not done.
  - We can use time in it if we set a certain time then the execution will stop until time overs after that it will execute still the instructions are remaining.
  - Syntax: condition_object.wait()
    Parameter:Time
- release() Method:
  - When the need of the condition object is fulfilled by threads then we will use the release() method which helps us to free the condition object from their tasks and suddenly releases the internal lock which was obtained by the threads.
  - Syntax: condition_object.release()
