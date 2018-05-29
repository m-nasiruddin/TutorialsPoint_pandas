# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np


# create an empty Series
s = pd.Series()
print(s)
# create a Series from ndarray
# example 1
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)
# example 2
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[100, 101, 102, 103])
print(s)
# create a Series from dict
# example 1
dict = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(dict)
print(s)
# example 2
dict = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(dict, index=['b', 'c', 'd', 'a'])
print(s)
# create a Series from scalar
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)
# accessing data from Series with position
# example 1
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s[2])  # retrieve the 3rd element
# example 2
print(s[:3])  # retrieve the 1st 3 element
# example 3
print(s[-3:])  # retrieve the last 3 element
# retrieve data using label (index)
# example 1
print(s['a'])  # retrieve a single element
# example 2
print(s[['a', 'c', 'd']])  # retrieve a single element
# example 3
print(s['f'])  # if a label isn't contained, an exception is raised
