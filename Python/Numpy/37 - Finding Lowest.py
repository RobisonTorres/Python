import numpy as np
print('Numpy')
print()

# The Lowest Common Multiple is the least number that is
# common multiple of both of the numbers.

# Find the LCM of the following two numbers:
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)  # Returns: 12 because that is the lowest common
# multiple of both numbers (4*3=12 and 6*2=12).

# Finding LCM in Arrays - To find the Lowest Common Multiple
# of all values in an array, you can use the reduce() method.
# The reduce() method will use the ufunc, in this case the lcm()
# function, on each element, and reduce the array by one dimension.

# Find the LCM of the values of the following array:
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)  # Returns: 18 because that is the lowest common multiple
# of all three numbers (3*6=18, 6*3=18 and 9*2=18).

# Find the LCM of all numbers of an array where the array contains
# all integers from 1 to 10:
arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)
