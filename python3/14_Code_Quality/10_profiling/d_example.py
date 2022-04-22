import cProfile
import pstats

# Using cProfile.Profile example
import random


def print_msg():
    for i in range(10):
        print("Program completed")


def generate():
    data = [random.randint(0, 99) for p in range(0, 1000)]
    return data


def search_function(data):
    for i in data:
        if i in [100, 200, 300, 400, 500]:
            print("success")


def main():
    data = generate()
    search_function(data)
    print_msg()


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats("tottime")
    stats.print_stats()

    # Export profiler output to file
    stats = pstats.Stats(profiler)
    stats.dump_stats("/export-data")
