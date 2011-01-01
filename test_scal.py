import tables
import numpy as np


h5file = tables.openFile('test4.h5', mode='w', title="Test Array")

array_len = 10000000

arrays = np.arange(50) 

for x in arrays:
    x_a = np.zeros(array_len, dtype=float)
    h5file.createArray(h5file.root, "test" + str(x), x_a)

h5file.close()