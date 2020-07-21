import numpy as np
import pandas as pd

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))

# Use the `shape` property
print(df.shape)

# Or use the `len()` function with the `index` property
print(len(df.index))

# printing dataframe
print(df)

# Using `iloc[]`
print(df.iloc[0][0])

# Using `loc[]`
print(df.loc[0]['A'])

# Using `at[]`
print(df.at[0, 'A'])

# Using `iat[]`
print(df.iat[0, 0])

# Additional References
#  ref: https://github.com/justmarkham/pandas-videos
#  ref: https://www.youtube.com/watch?reload=9&v=RlIiVeig3hc
