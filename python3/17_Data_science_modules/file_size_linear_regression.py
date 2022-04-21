import random
import gzip
import shutil
import os
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

destination = "./samples/"

text_file_sizes = []
compression_sizes = []
number_of_files = 100


def generateTextFiles():
    for i in range(number_of_files):
        size = random.randrange(0, 1000)
        contents = ""
        for j in range(size):
            character = chr(ord('a') + random.randrange(0, 26))
            contents += character
        file_name = "text_file" + str(i) + ".txt"
        file = open(destination + file_name, "w")
        file.write(contents)
        file.close()


def generateZips():
    for i in range(number_of_files):
        file_name = "text_file" + str(i) + ".txt"
        f_in = open(destination + file_name, "rb")
        f_out = gzip.open(destination + file_name + ".gz", "wb")
        shutil.copyfileobj(f_in, f_out)
        f_in.close()
        f_out.close()

def generateData():
    for i in range(number_of_files):
        file_name = "text_file" + str(i) + ".txt"
        text_file_sizes.append([os.path.getsize(destination + file_name)])
        compression_sizes.append(os.path.getsize(destination + file_name + ".gz"))

def generateRegression():
    text_train = text_file_sizes[:-20]
    text_test = text_file_sizes[-20:]
    zipped_train = compression_sizes[:-20]
    zipped_test = compression_sizes[-20:]
    regr = linear_model.LinearRegression()
    regr.fit(text_train, zipped_train)
    # The coefficients
    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    print("Mean squared error: %.2f"
      % np.mean((regr.predict(text_test) - zipped_test) ** 2))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % regr.score(text_test, zipped_test))
    plt.scatter(text_test, zipped_test,  color='black')
    plt.plot(text_test, regr.predict(text_test), color='blue',
             linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()


generateTextFiles()
generateZips()
generateData()
generateRegression()