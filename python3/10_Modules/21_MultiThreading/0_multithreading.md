# Tasks

- I/O-bound tasks
  – the time spending on I/O significantly more than the time spending on computation

  - Ex: reading files from a network or database

- CPU-bound tasks
  – the time spending on computation is significantly higher than the time waiting for I/O.
  - Ex: computationally heavy tasks since it will benefit from having multiple processors;
- Python threading is optimized for I/O bound tasks. For example, requesting remote resources, connecting a database server, or reading and writing files.

## Threads

- Threads share memory and don’t need to create a new virtual memory space when they are created and thus don’t require a MMU (memory management unit) context switch
- Communication between threads is simpler as they have a shared memory while processes requires various modes of IPC (Inter-Process Communications) like semaphores, message queues, pipes etc.
- Threading can allow concurrency and reduces time consumption, increase performance.

## Daemon Threads

- Mainly useful for background tasks execution
- Ex: sending keepalive packets, or performing periodic garbage collection, etc
- Its like fire and forget. Daemon threads will be killed automatically, once
  main thread is closed.

- when main returns, your process will not exit if there are non-daemon threads still running.
- Simply to avoid it, we use daemon threads whenever possible.

## Thread Synchronization in Python

- Synchronization in a multithreaded program means serialised access to a critical resource.
- A critical resource is typically a variable in a program that is shared across multiple threads.
- The need for Synchronization of a critical resource arises from the fact various combinations of read and write sequences will lead to data anomalies due to premature overwriting of values by threads followed by reading of wrong values by the threads.
- When multiple threads try to access a resource a race condition arises. Race conditions in a multi threaded program leads to inconsistent reads and writes resulting in data anomalies and erroneous behaviour of programs due to data inconsistencies.
- Synchronization is one of the mechanisms to handle race conditions in multithreaded programs.
  In Python, the following Synchronization primitives are provided for the multithreaded programs.

- Synchronization Primitives
  - Locks, RLocks, Semaphores, Events, Conditions and Barriers

## Lock Objects

- In Python, the Lock class of threading module implements the primitive lock.
- Lock has only TWO states - locked and unlocked
- It is created in unlocked state and has two methods:
  - acquire()
  - release()
- The acquire() method locks the Lock and blocks execution until the release() method
  in some other coroutine sets it to unlocked.
  Then it locks the Lock again and returns True.
  The release() method should only be called in the locked state, it sets the state
  to unlocked and returns immediately.
  If release() is called in the unlocked state, a RunTimeError is raised.

## RLock Objects

- RLock is the reentrant lock provided by python.
- standard Lock doesn’t know which thread is currently holding the lock.
  If the lock is held, any thread that attempts to acquire it will block, even if
  the same thread itself is already holding the lock.
- A reentrant lock or simply RLock allows itself to be locked several times.
- The RLock is released only after equal number release() calls as the acquire() calls made to it.
- Unlike the primitive lock given by the Lock class the RLock can only be released by the thread holding the RLock.
- One good use case for RLocks is recursion, when a parent call of a function would otherwise block its nested call. Thus, the main use for RLocks is nested access to shared resources.

## Semaphores

- Semaphores are simply advanced counters.
- An acquire() call to a semaphore will block only after a number of threads have
  acquire()ed it.
- The associated counter decreases per acquire() call, and increases per release() call.
- A ValueError will occur if release() calls try to increment the counter beyond
  it's assigned maximum value (which is the number of threads that can acquire()
  the semaphore before blocking occurs).
- Semaphores are typically used for limiting a resource, like limiting a server to
  handle only 10 clients at a time. In such a case, multiple thread connections compete
  for a limited resource.
- Semaphores are used when the resources to be shared among the threads are limited in number.
- A Semaphore can be acquired 'n' number of times without waiting where 'n' is number of resources managed by the Semaphore. The resources can be sessions, number of threads in a thread pool and so on.
- In python Semaphore is implemented by the Semaphore class of the Threading Module. Each call to the acquire() of Semaphore object method decreases the counter in the Semaphore, till it becomes zero. Once the count becomes zero, any further calls to acquire() will be blocked.

## Event

- The Event synchronization primitive acts as a simple communicator between threads.
- They are based on an internal flag which threads can set() or clear().
- Other threads can wait() for the internal flag to be set().
- The wait() method blocks until the flag becomes true.

## Condition

- A Condition object is simply a more advanced version of the Event object.
- It too acts as a communicator between threads and can be used to notify()
  other threads about a change in the state of the program.
- Ex: it can be used to signal the availability of a resource for consumption.
- Other threads must also acquire() the condition (and thus its related lock)
  before wait()ing for the condition to be satisfied.
- Also, a thread should release() a Condition once it has completed the related
  actions, so that other threads can acquire the condition for their purposes.
- UseCase: when developing a streaming API which notifies a waiting client once
  a piece of data is available.

## Barriers

- A barrier is a simple synchronization primitive which can be used by different
  threads to wait for each other.
- Each thread tries to pass a barrier by calling the wait() method, which will
  block until all of threads have made that call.
- As soon as that happens, the threads are released simultaneously.
- UseCase: synchronizing a server and a client
  — as the server has to wait for the client after initializing itself.
