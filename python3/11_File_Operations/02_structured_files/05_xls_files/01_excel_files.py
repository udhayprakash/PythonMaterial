import pandas as pd

movies = pd.read_excel("movies.xls")

print(movies.head())

movies_sheet1 = pd.read_excel("movies.xls", sheetname=0, index_col=0)
movies_sheet1.head()
