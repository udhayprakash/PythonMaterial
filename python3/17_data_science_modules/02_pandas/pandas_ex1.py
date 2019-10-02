import numpy as np
import pandas as pd

# Creating a pandas dataframe
data = np.array([['', 'Col1', 'Col2'],
                 ['Row1', 1, 2],
                 ['Row2', 3, 4]])

print(pd.DataFrame(data=data[1:, 1:],
                   index=data[1:, 0],
                   columns=data[0, 1:]))
print('-' * 50)

# Take a 2D array as input to your DataFrame
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(pd.DataFrame(my_2darray))
print('-' * 50)

# Take a dictionary as input to your DataFrame
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
print(pd.DataFrame(my_dict))
print('-' * 50)

# Take a DataFrame as input to your DataFrame
my_df = pd.DataFrame(data=[4, 5, 6, 7], index=range(0, 4), columns=['A'])
print(pd.DataFrame(my_df))
print('-' * 50)

# Take a Series as input to your DataFrame
my_series = pd.Series(
    {"United Kingdom": "London", "India": "New Delhi", "United States": "Washington", "Belgium": "Brussels"})
print(pd.DataFrame(my_series))
print('-' * 50)
