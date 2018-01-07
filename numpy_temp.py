import openpyxl
import numpy as np
import matplotlib as mat
import os

test_array = np.array(range(1000))


%timeit np.sum(test_array)

print(test_array)
