#!/usr/bin/python
"""
Purpose: To display thread information
"""
import threading


def thread_info():
    t = threading.current_thread()
    print(
        f"""============================
	Thread Name
		{t.name         =}
		{t._name        =}
	"""
    )

    # ident - is thread identifier of current thread.
    # 	Thread identifiers may be recycled when a thread exits and another thread is created.
    print(
        f"""
		{t.ident  =}
		{t._ident =}
	"""
    )

    # native_id - thread ID assigned by OS(kernel)
    # 	This value may be used to uniquely identify this particular thread system-wide
    # 	(until the thread terminates, after which the value may be recycled by the OS).
    print(
        f"""
		{t._native_id	=}
	Thread Status
		{t._initialized	=}
		{t.is_alive()	=}
		{t._is_stopped	=}

		{t._args        =}
		{t._kwargs      =}
	"""
    )
    # Daemon threads are abruptly stopped at shutdown.
    # Their resources (such as open files, database transactions, etc.) may not be
    # released properly. If you want your threads to stop gracefully, make them
    # non-daemonic and use a suitable signalling mechanism such as an Event.
    print(
        f"""
		{t.daemon       =}
		{t._daemonic    =}
	"""
    )


# Initializing a thread
thread1 = threading.Thread(target=thread_info)
thread2 = threading.Thread(target=thread_info, name="my custom thread")

# Starting a thread
thread1.start()
thread2.start()


# TODO - thread attributes
# {t._bootstrap	}
# {t._bootstrap_inner}
# {t._invoke_excepthook}
# {t._set_tstate_lock}
# {t._tstate_lock	=}
# {t._wait_for_tstate_lock=}
# {t._reset_internal_locks=}
# {t._stop()		=}
# {t._target		=}
# {t._delete()	=}
