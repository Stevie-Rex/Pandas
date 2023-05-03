import pandas as pd

data = pd.read_csv('bmidata.csv')

data2 = data.head(7)

dupdata = data2.append(data2)

print(dupdata.shape)

dupdata = dupdata.drop_duplicates()
print(dupdata.shape)