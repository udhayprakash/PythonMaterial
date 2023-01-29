import psutil


def kill(process_name):
    """Kill Running Process by using it's name
    - Generate list of processes currently running
    - Iterate through each process
        - Check if process name or cmdline matches the input process_name
        - Kill if match is found
    Parameters
    ----------
    process_name: str
        Name of the process to kill (ex: HD-Player.exe)
    Returns
    -------
    None
    """
    try:
        print(f"Killing processes {process_name}")
        processes = psutil.process_iter()
        for process in processes:
            try:
                print(f"Process: {process}")
                print(f"id: {process.pid}")
                print(f"name: {process.name()}")
                print(f"cmdline: {process.cmdline()}")
                if process_name == process.name() or process_name in process.cmdline():
                    print(f"found {process.name()} | {process.cmdline()}")
                    process.terminate()
            except Exception:
                print(f"{traceback.format_exc()}")

    except Exception:
        print(f"{traceback.format_exc()}")
