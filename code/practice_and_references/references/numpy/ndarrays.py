import numpy as np

character_list = ['1', '2', '3', '4', '5']

integer_list = [map(int, x) for x in character_list]

numpy_array = np.array(integer_list)

product = numpy_array[0] * numpy_array[1]

print type(product)
print product
