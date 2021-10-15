#!/usr/bin/python3
"""
Purpose: Data preprocessing
    No Dataset is perfect
    There can be extraneous data points, reporting errors, ...
    To prevent manual cleansing, normalizing and scaling data, 
        Two standardizing functions
            1. MinMax
            2. Standard
    If your data instead follows standard deviation, you can use 
    the StandardScaler instead. 
    This scaler fits a passed data set to be a standard scale 
    along with the standard deviation.

        x_transform = (x - meanVal)/ std_dev

"""
import sklearn.preprocessing as preprocessing
import numpy as np

X = np.random.randint(2, 10, size=(4, 2))
X2 = np.random.randint(100, 10000, size=(4, 2))
X = np.concatenate((X, X2), axis=1)
print("The original matrix")
print(X)

std = preprocessing.StandardScaler()
std.fit(X)
X_std = std.transform(X)
print("The transform data using Standard scaler")
print(X_std)
