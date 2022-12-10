import numpy as np
import matplotlib.pyplot as plt
print('Machine Learning')
print()

# To create big data sets for testing, we use the Python
# module NumPy, which comes with a number of methods to create
# random data sets, of any size.

# Create an array containing 250 random floats between 0 and 5:
x = np.random.uniform(0.0, 5.0, 250)
# print(x)

# Histogram - To visualize the data set we can draw a histogram
# with the data we collected.
plt.hist(x, 5)  # 5 -  for 5 bars
plt.show()
