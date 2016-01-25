##
# Produce a histogram
##

from numpy.random import normal
import matplotlib.pyplot as plt

gaussian_numbers = normal(size=12000000)
plt.hist(gaussian_numbers)
plt.title("title")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("filename.png")

#note that this clears the figure
plt.show()
