from numpy.random import randn

import matplotlib as mpl
import matplotlib.pyplot as plt

# http://en.wikipedia.org/wiki/Histogram

dataset1 = randn(100)
# print dataset1

plt.hist(dataset1)
plt.show()

dataset2 = randn(80)
plt.hist(dataset2, color='indianred')
plt.show()

plt.hist(dataset1, density=True, color='indianred', alpha=0.5, bins=20)
plt.hist(dataset2, density=True, alpha=0.5, bins=20)
plt.show()

data1 = randn(1000)
data2 = randn(1000)

# import seaborn
# seaborn.jointplot(data1, data2)
# seaborn.jointplot(data1, data2, kind='hex')


# For futher reference, https://python-graph-gallery.com/
