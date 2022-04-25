# Tasks

- I/O-bound tasks
  – the time spending on I/O significantly more than the time spending on computation
- CPU-bound tasks
  – the time spending on computation is significantly higher than the time waiting for I/O.

- Python threading is optimized for I/O bound tasks. For example, requesting remote resources, connecting a database server, or reading and writing files.

## Threads

- Threads share memory and don’t need to create a new virtual memory space when they are created and thus don’t require a MMU (memory management unit) context switch
- Communication between threads is simpler as they have a shared memory while processes requires various modes of IPC (Inter-Process Communications) like semaphores, message queues, pipes etc.
- Threading can allow concurrency and reduces time consumption, increase performance.

## Thread Synchronization in Python

- Synchronization in a multithreaded program means serialised access to a critical resource.
- A critical resource is typically a variable in a program that is shared across multiple threads.
- The need for Synchronization of a critical resource arises from the fact various combinations of read and write sequences will lead to data anomalies due to premature overwriting of values by threads followed by reading of wrong values by the threads.
- When multiple threads try to access a resource a race condition arises. Race conditions in a multi threaded program leads to inconsistent reads and writes resulting in data anomalies and erroneous behaviour of programs due to data inconsistencies.
- Synchronization is one of the mechanisms to handle race conditions in multithreaded programs.
  In Python, the following Synchronization primitives are provided for the multithreaded programs.

## Lock Objects

- In Python, the Lock class of threading module implements the primitive lock.
- The Lock can be acquired and released. When the lock is in locked state other threads wait for the lock to be released by the thread. Any thread can release the lock.

## RLock Objects

- RLock is the reentrant lock provided by python.
- A reentrant lock or simply RLock allows itself to be locked several times.
- The RLock is released only after equal number release() calls as the acquire() calls made to it.
- Unlike the primitive lock given by the Lock class the RLock can only be released by the thread holding the RLock.

## Semaphores

- Semaphores are used when the resources to be shared among the threads are limited in number.
- A Semaphore can be acquired 'n' number of times without waiting where 'n' is number of resources managed by the Semaphore. The resources can be sessions, number of threads in a thread pool and so on.
- In python Semaphore is implemented by the Semaphore class of the Threading Module. Each call to the acquire() of Semaphore object method decreases the counter in the Semaphore, till it becomes zero. Once the count becomes zero, any further calls to acquire() will be blocked.
