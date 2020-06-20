asyncio
========
- concurrency module introduced in Python 3.4. 
- asyncio is neither multiprocessing nor multithreading.
- It's a single thread, single process project
- It uses cooperative multi-tasking with PROACTOR pattern. 
- It’s designed to use coroutines and futures to simplify asynchronous 
    code and make it almost as readable as synchronous code simply 
    because there are no callbacks.
- Blocking Functions 
    1. CPU Bound 
    2. IO Bound

- fundamental advantages of async/await over threads are:
    - Cooperative multi-tasking is much lighter-weight than OS threads, so you can reasonably have millions of concurrent tasks, versus maybe a dozen or two threads at best.
    - Using await makes visible where the schedule points are. 
      This has two advantages:
        - It makes it easier to reason about data races
        - But if a task doesn’t yield then it can accidentally block all other tasks from running; if schedule points were invisible it would be more difficult to debug this issue.
        - Tasks can support cancellation. (Which also benefits from making await visible, because it makes it possible to reason about which points are cancellation points.)
- There are three types of "awaitables".
    a. Coroutines
        - coroutine function -> It has "async def" in syntax. 
        - coroutine object -> an object returned by calling  a coroutine function.
    b. Tasks
        - used to schedule coroutines concurrently.
        - asyncio.current_task
        - asyncio.all_tasks
    c. Futures
        - a low-level awaitable object that represents an eventual result of an asynchronous
          operation.
        - analogy: its like an empty postbox. At some point in future, the postman will 
          arrive and stick a letter into the postbox. 
        - loop.run_in_executor

- To run async code in REPL, 
     - command: python -m asyncio
     - Once the REPL has started you don’t need to use asyncio.run(), but just use the await statement directly.

        >>> import asyncio
        >>> async def hello():
        ...     await asyncio.sleep(3)
        ...     print('Hello world')
        ...
        >>> await hello()
        Hello world
        >>>


next 
    - http://hoad.io/blog/playing-with-asyncio/
    - http://sdiehl.github.io/gevent-tutorial/
