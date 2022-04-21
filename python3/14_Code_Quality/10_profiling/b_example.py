import cProfile

# Code containing multiple dunctions
def create_array():
    arr = []
    for i in range(0, 400000):
        arr.append(i)


def print_statement():
    print("Array created successfully")


def main():
    create_array()
    print_statement()


if __name__ == "__main__":
    cProfile.run("main()")
