import cProfile
import pstats

# Function performing linear regression on diabetes dataset


def regression():
    import numpy as np
    from sklearn import datasets, linear_model
    from sklearn.metrics import mean_squared_error, r2_score

    # Load the diabetes dataset
    diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

    # Use only one feature
    diabetes_X = diabetes_X[:, np.newaxis, 2]

    # Split the data into training/testing sets
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    # Split the targets into training/testing sets
    diabetes_y_train = diabetes_y[:-20]
    diabetes_y_test = diabetes_y[-20:]

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(diabetes_X_train, diabetes_y_train)

    # Make predictions using the testing set
    diabetes_y_pred = regr.predict(diabetes_X_test)


# Initialize profile class and call regression() function
profiler = cProfile.Profile()
profiler.enable()
regression()
profiler.disable()
stats = pstats.Stats(profiler).sort_stats("tottime")

# Print the stats report
stats.print_stats()


# # Load the extension for visualizer.
# %load_ext snakeviz
# %snakeviz regression()
