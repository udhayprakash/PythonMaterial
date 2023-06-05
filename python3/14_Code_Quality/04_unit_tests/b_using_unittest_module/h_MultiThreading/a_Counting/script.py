import threading


def count_up_to_n(n):
    for i in range(n):
        print(i)


def multithreaded_counting(n, num_threads=2):
    threads = []
    chunk_size = n // num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i != num_threads - 1 else n
        thread = threading.Thread(target=count_up_to_n, args=(end - start,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
