import pandas as pd


# create a dictionary of series
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}
# create DataFrame
df = pd.DataFrame(d)
print(df)
# T (transpose)
print(df.T)
# axes
print(df.axes)
# dtypes
print(df.dtypes)
# empty
print(df.empty)
# ndim
print(df.ndim)
# shape
print(df.shape)
# size
print(df.size)
# values
print(df.values)
# head
print(df.head(2))
# tail
print(df.tail(2))
