from numpy import random
print('Numpy')
print()

# A random distribution is a set of random numbers that
# follow a certain probability density function.

'''
The choice() method allows us to specify the probability for each value.
The probability is set by a number between 0 and 1, 
where 0 means that the value will never occur and 1 means 
that the value will always occur.

Example:
Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
The probability for the value to be 3 is set to be 0.1
The probability for the value to be 5 is set to be 0.3
The probability for the value to be 7 is set to be 0.6
The probability for the value to be 9 is set to be 0
'''
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=50)
# The sum of all probability numbers should be 1.
print(x, 'length is ' + str(len(x)), 'and dimension is equals to ' + str(x.ndim) + '.')

# Same example as above, but return a 2-D array with 3 rows,
# each containing 5 values.
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 4))
# The sum of all probability numbers should be 1.
print(x)
