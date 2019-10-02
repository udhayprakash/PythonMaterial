import pandas as pd

url_csv = 'https://vincentarelbundock.github.io/Rdatasets/csv/boot/amis.csv'
df = pd.read_csv(url_csv)

df = pd.read_csv(url_csv, index_col=0)
print(df.head(10))

print(df.tail())

'''
when loading large dataset with python dataframe, the best practices are 
    a. To load in chucks
    b. filter out unwanted columns 
    c. optimizing the memory usage with using astype() for the columns
'''
