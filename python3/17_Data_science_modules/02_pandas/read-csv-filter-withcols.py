# https://stackoverflow.com/questions/15017072/pandas-read-csv-and-filter-columns-with-usecols

import pandas as pd
from StringIO import StringIO

csv = r"""dummy,date,loc,x
bar,20090101,a,1
bar,20090102,a,3
bar,20090103,a,5
bar,20090101,b,1
bar,20090102,b,3
bar,20090103,b,5"""

df = pd.read_csv(
    StringIO(csv),
    header=0,
    index_col=["date", "loc"],
    usecols=["date", "loc", "x"],
    parse_dates=["date"],
)
