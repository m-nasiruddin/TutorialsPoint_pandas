import pandas as pd


# create a dictionary of Series
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack', 'Lee', 'David', 'Gasper', 'Betina',
                        'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
# create a DataFrame
df = pd.DataFrame(d)
print(df)
# count() (returns the number of non-null observations)
print(df.count())
# sum() (returns the sum of the values for the requested axis)
print(df.sum())
print(df.sum(1))  # axis=1
# mean() (returns the average value)
print(df.mean())
# median() (returns the Median of values)
print(df.median())
# mode() (returns the Mode of values)
print(df.mode())
# std() (returns the Bressel standard deviation of the numerical columns)
print(df.std())
# min() (returns the minimum value)
print(df.min())
# max() (returns the maximum value)
print(df.max())
# prod() (returns the product of values)
print(df.prod())
# cumsum() (returns the cumulative sum)
print(df.cumsum())
# summarizing data
print(df.describe())
# summarizes String columns
print(df.describe(include=['object']))
# summarizes numeric columns
print(df.describe(include=['number']))
# summarizes all columns together
print(df.describe(include='all'))
