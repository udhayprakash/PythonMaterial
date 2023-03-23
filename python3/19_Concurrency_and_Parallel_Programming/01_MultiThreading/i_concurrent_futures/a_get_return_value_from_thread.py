import concurrent.futures


def foo(bar):
    return "hello {}".format(bar)


with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(foo, "world!")
    return_value = future.result()
    print(f"{return_value =}")


def hello_world(name, age):
    return f"hello_{name} and age is {age}"


with concurrent.futures.ThreadPoolExecutor() as exc:
    future = exc.submit(hello_world, "Anoop", 30)
    return_val = future.result()
    print(f"{return_val =}")
