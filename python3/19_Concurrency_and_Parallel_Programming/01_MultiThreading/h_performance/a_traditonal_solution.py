"""
Purpose: To read content from file,
    and replace it, traditionally
"""
from time import perf_counter


def replace(filename, substr, new_substr):
    print(f"Processing the file {filename}")
    # get the contents of the file
    with open(filename, "r") as f:
        content = f.read()

    # replace the substr by new_substr
    content = content.replace(substr, new_substr)

    # write data into the file
    with open(filename, "w") as f:
        f.write(content)


def main():
    filenames = [
        "c:/temp/test1.txt",
        "c:/temp/test2.txt",
        "c:/temp/test3.txt",
        "c:/temp/test4.txt",
        "c:/temp/test5.txt",
        "c:/temp/test6.txt",
        "c:/temp/test7.txt",
        "c:/temp/test8.txt",
        "c:/temp/test9.txt",
        "c:/temp/test10.txt",
    ]

    for filename in filenames:
        replace(filename, "ids", "id")


if __name__ == "__main__":
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f"It took {end_time- start_time :0.2f} second(s) to complete.")

# It took 0.16 second(s) to complete.