import sys
import pandas as pd

month = sys.argv[1]

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df['month'] = month
print(df.head())

print(month)