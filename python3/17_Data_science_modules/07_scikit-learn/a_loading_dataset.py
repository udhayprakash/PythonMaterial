from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

print(f'iris dataset is {iris.DESCR}')
print(f'iris data size is {iris.data.shape}')
print(f'iris target size is {iris.target.shape}')
print(
    f'iris data has {iris.data.shape[1]} features, the feature names are {iris.feature_names}')
print(
    'iris data has {iris.data.shape[1]} samples, the target label names {iris.target_names}')

print('Feature names:', feature_names)
print('Target names:', target_names)
print('\nFirst 10 rows of X:\n', X[:10])
