import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random
print('Numpy')
print()

# The Normal Distribution is one of the most important distributions.
# Use the random.normal() method to get a Normal Data Distribution.

# It has three parameters:
# loc - (Mean) where the peak of the bell exists.
# scale - (Standard Deviation) how flat the graph distribution should be.
# size - The shape of the returned array.

# Generate a random normal distribution of size 2x3:
x = random.normal(size=(2, 3))
print(x)

# Generate a random normal distribution of size 2x3 with
# mean at 1 and standard deviation of 2:
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

# Visualization of Normal Distribution
sns.distplot(random.normal(size=1000), hist=False)
plt.show()

