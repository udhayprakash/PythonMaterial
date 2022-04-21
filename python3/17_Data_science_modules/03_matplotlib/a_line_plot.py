import matplotlib.pyplot as plt


def line_plot(numbers):
    plt.plot(numbers)
    plt.ylabel("Random numbers")
    plt.show()


if __name__ == "__main__":
    numbers = [2, 1, 4, 6]
    line_plot(numbers)
