import numpy as np
print('Machine Learning')
print()

'''
What are Percentiles? Percentiles are used in statistics to give
you a number that describes the value that a given percent of the
values are lower than.

Example: Let's say we have an array of the ages of all the people 
that lives in a street.
'''
# Use the NumPy percentile() method to find the percentiles:
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82,
        32, 2, 8, 6, 25, 36, 27, 61, 31]
x = np.percentile(ages, 75)

print(x)  # What is the 75. percentile? The answer is 43,
# meaning that 75% of the people are 43 or younger.
