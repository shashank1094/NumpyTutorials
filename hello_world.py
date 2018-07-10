# https://docs.scipy.org/doc/numpy/user/quickstart.html

import numpy as np

print(np.__version__)

# a = np.array(1,2,3,4) # Wrong
a = np.array([1, 2, 3, 4])
print(a, type(a), a.ndim, a.itemsize, a.dtype)
a.shape = (2, 2)
print(a, type(a), a.ndim, a.itemsize, a.dtype)

print(np.zeros((3, 4), dtype=np.int64))
print(np.ones((3, 4), dtype=np.int64))





