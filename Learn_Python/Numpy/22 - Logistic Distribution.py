import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random
print('Numpy')
print()

# Logistic Distribution is used to describe growth.

# It has three parameters:
# loc - mean, where the peak is. Default 0.
# scale - standard deviation, the flatness of distribution. Default 1.
# size - The shape of the returned array.

# Draw 2x3 samples from a logistic distribution with mean at 1 and stddev 2.0:
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

# Visualization of Logistic Distribution
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()
