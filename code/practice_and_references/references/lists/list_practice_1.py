##
#
# We want to iterate through the columns
#
##

import numpy as np

values = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print values 
print values[0]
print values[0][0]
print values[1][0]
print values[1][1]
print values[2][1]
print values[2][:]
print values[:][2]


array = np.array(values)

print array[1,1]
print array[1,:]
print array[:,1]
