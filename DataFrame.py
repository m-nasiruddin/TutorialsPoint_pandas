# import the pandas library and aliasing as pd
import pandas as pd


# create and empty DataFrame
df = pd.DataFrame()
print(df)
# create a DataFrame from lists
# example 1
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)
# example 2
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
# example 3
df = pd.DataFrame(data, columns=['Name', 'Age'], dtype=float)
print(df)
# create a DataFrame from dict of ndarrays / lists
# example 1
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data)
print(df)
# example 2
df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df)
# create DataFrame from list of dicts
# example 1
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
# example 2
df = pd.DataFrame(data, index=['first', 'second'])
print(df)
# example 3
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])  # with two column indices, values are same as
# dictionary keys
print(df1)
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])  # with two column indices with one index with
# other name
print(df2)
# create a DataFrame from dict of Series
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
# column selection
print(df['one'])
# column addition (adding a new column to an existing DataFrame object with column label by passing new series)
print('adding a new column by passing as Series:')
df['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(df)
print('adding a new column using the existing columns in DataFrame:')
df['four'] = df['one'] + df['three']
print(df)
# column deletion (using the previous DataFrame, we will delete a column using del function)
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
df = pd.DataFrame(d)
print('our DataFrame is:\n', df)
print('deleting the 1st column using del function:')
del df['one']  # using del function
print(df)
print('deleting another column using pop function:')
df.pop('two')  # using pop function
print(df)
# row selection, addition and deletion
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
# selection by label
print(df.loc['b'])  # rows can be selected by passing row label to a loc function
# selection by integer location
print(df.iloc[2])  # rows can be selected by passing integer location to an iloc function
# slice rows
print(df[2:4])  # multiple rows can be selected using ':' operator
# addition of rows
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
df = df.append(df2)  # add new rows to a DataFrame using the append function
print(df)
# deletion of rows (use index label to delete or drop rows from a DataFrame)
df = df.drop(0)
print(df)
