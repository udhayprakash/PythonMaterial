import pandas as pd

csv_url = 'http://vincentarelbundock.github.io/Rdatasets/csv/carData/MplsStops.csv'
df = pd.read_csv(csv_url, index_col='idNum')
print(df.iloc[:, 0:6].head())
