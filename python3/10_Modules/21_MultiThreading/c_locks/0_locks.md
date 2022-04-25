# Locks

- There are two states of a lock i.e locked and unlocked.
- A lock is a class in the threading module whose object generated in the unlocked state and has two primary methods i.e acquire() and release().
- When the acquire() method is called, it locks the execution of the Lock and blocks it’s execution until the release() method is called in some other thread which sets it to unlock state.
- Locks help us in efficiently accessing a shared resource in a program in order to prevent corruption of data, it follows mutual exclusion as only one thread can access a particular resource at a time.

# Locks vs RLocks

- A Lock object can not be acquired again by any thread unless it is released by the thread which which is accessing the shared resource.
  An RLock object can be acquired numerous times by any thread.
- A Lock object can be released by any thread.
  An RLock object can only be released by the thread which acquired it.
- A Lock object can be owned by none
  An RLock object can be owned by many threads
- Execution of a Lock object is faster.
  Execution of an RLock object is slower than a Lock object
