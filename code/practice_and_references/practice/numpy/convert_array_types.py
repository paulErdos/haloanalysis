import numpy as np


catalog = [['0', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
           ['0', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
           ['0', '2', '3', '4', '5', '6', '7', '8', '9', '10']]

array = np.array(catalog)

print type(array[0][0])

int_array = [[int(y) for y in x] for x in catalog]

print type(int_array[0][0])
