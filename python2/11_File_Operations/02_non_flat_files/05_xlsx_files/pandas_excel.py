import pandas as pd
Column1 = [1,2,3,4]
Column2 = [5,6,7,8]
df = pd.DataFrame.from_dict({'Column1':Column1,'Column2':Column2})
df.to_excel('test.xlsx', header=True, index=False)