#!/usr/bin/python3
"""
Purpose: Data preprocessing
    No Dataset is perfect
    There can be extraneous data points, reporting errors, ...
    To prevent manual cleansing, normalizing and scaling data,
        Two standardizing functions
            1. MinMax
            2. Standard
    MinMax shrinks the range of each figure to be between 0 and 1.

        x_transform = (x - minVal)/ (maxVal - minVal)
"""
import sklearn.preprocessing as preprocessing
import numpy as np

X = np.random.randint(2, 10, size=(4, 2))
X2 = np.random.randint(100, 10000, size=(4, 2))
X = np.concatenate((X, X2), axis=1)
print("The original matrix")
print(X)

# min-max scaler

minmax = preprocessing.MinMaxScaler()
minmax.fit(X)
X_minmax = minmax.transform(X)
print("The transform data using min-max scaler")
print(X_minmax)
