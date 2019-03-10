# Import pandas
import pandas as pd

# Load csv
data = pd.read_csv("sampleCSVFile.csv")

# Preview the first 5 lines of the loaded data
print(data.head())

print(dir(data))
