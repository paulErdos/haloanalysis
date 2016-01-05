import numpy as np
from matplotlib import pyplot

x = np.arange(0, 5, 0.1)
y = np.sin(x)
pyplot.plot(x, y)

pyplot.savefig('out')
