import numpy as np
print('Machine Learning')
print()

'''
What is Standard Deviation? Standard deviation is a number that 
describes how spread out the values are. A low standard deviation 
means that most of the numbers are close to the mean (average) value.
A high standard deviation means that the values are spread out over a wider range
'''

# Use the NumPy std() method to find the standard deviation:
speed = [86, 87, 88, 86, 87, 85, 86]
x = np.std(speed)
print(x)  # Outputs - 0.90

# Variance is another number that indicates how spread out the values are.
# Use the NumPy var() method to find the variance:
speed = [32, 111, 138, 28, 59, 77, 97]
x = np.var(speed)
print(x)  # Outputs - 1432.24

