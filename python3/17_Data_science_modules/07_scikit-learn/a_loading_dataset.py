from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names
print("Feature names:", feature_names) 
print("Target names:", target_names)
print("\nFirst 10 rows of X:\n", X[:10])