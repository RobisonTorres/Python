import numpy as np
import matplotlib.pyplot as plt
print('Machine Learning')
print()

# A scatter plot is a diagram where each value in the data
# set is represented by a dot.

# Use the scatter() method to draw a scatter plot diagram:
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
plt.scatter(x, y)
plt.show()

'''
Random Data Distributions - In Machine Learning the data sets can
contain thousands-, or even millions, of values. You might not 
have real world data when you are testing an algorithm, you might
have to use randomly generated values. As we have learned in the 
previous chapter, the NumPy module can help us with that!
Let us create two arrays that are both filled with 1000 random numbers
from a normal data distribution.
The first array will have the mean set to 5.0 with a standard deviation of 1.0.
The second array will have the mean set to 10.0 with a standard deviation of 2.0:
'''
# A scatter plot with 1000 dots:
x = np.random.normal(5.0, 1.0, 100)  # mean, standard d., quantity
y = np.random.normal(10.0, 2.0, 100)
plt.scatter(x, y)
plt.show()
