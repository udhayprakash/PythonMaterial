import threading


def print_message(message, num_times):
    for i in range(num_times):
        print(message)


def multithreaded_printing(message, num_times, num_threads=2):
    threads = []
    chunk_size = num_times // num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i != num_threads - 1 else num_times
        thread = threading.Thread(target=print_message, args=(message, end - start))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
