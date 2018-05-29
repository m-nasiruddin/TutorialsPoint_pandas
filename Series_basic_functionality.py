import numpy as np
import pandas as pd


# create a series with 100 random numbers
s = pd.Series(np.random.rand(4))
print(s)
# axes
print(s.axes)
# empty
print(s.empty)
# ndim
print(s.ndim)
# size
print(s.size)
# values
print(s.values)
# head
print(s.head(2))
# tail
print(s.tail(2))
