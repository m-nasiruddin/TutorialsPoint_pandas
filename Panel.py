import numpy as np
import pandas as pd


# create Panel
# create an empty Panel
p = pd.Panel()
print(p)
# from 3D ndarray
data = np.random.rand(2, 4, 5)
print(data)
p = pd.Panel(data)
print(p)
# from dict of DataFrame objects
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)
# selecting the data from Panel
# using items
print(p['Item1'])
# using major axis
print(p.major_xs(1))
# using minor axis
print(p.minor_xs(1))
