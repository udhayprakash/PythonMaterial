import matplotlib.pyplot as plt
import sklearn.datasets as datasets

X, y = datasets.make_regression(n_features=1, n_informative=1)
fig, axe = plt.subplots(dpi=300)
axe.scatter(X, y, marker="o")
axe.set_title("Data generated from make_regression")
fig.savefig("output/img.png")
plt.close(fig)
