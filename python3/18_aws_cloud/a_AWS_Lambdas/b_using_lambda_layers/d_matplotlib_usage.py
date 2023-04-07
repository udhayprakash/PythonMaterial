import matplotlib.pyplot as plt


def lambda_handler(event, context):
    x = [1, 2, 3]
    y = [2, 4, 6]
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Plot")
    plt.savefig("/tmp/plot.png")
    return {"statusCode": 200, "body": "Plot saved as /tmp/plot.png"}
