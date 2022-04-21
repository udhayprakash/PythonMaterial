import pandas as pd

url_csv = 'https://vincentarelbundock.github.io/Rdatasets/csv/boot/amis.csv'
df = pd.read_csv(url_csv)

df = pd.read_csv(url_csv, index_col=0)
print df.head()
