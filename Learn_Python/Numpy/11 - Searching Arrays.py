import numpy as np
print('Numpy')
print()

# You can search an array for a certain value,
# and return the indexes that get a match.
# To search an array, use the where() method.

# Find the indexes where the value is 4:
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

# Find the indexes where the values are even:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr % 2 == 0)
print(x)

# There is a method called searchsorted() which performs
# a binary search in the array, and returns the index where
# the specified value would be inserted to maintain the search order.
# Find the indexes where the value 7 should be inserted:
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

# Find the indexes where the value 7 should be inserted,
# starting from the right:
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

# Find the indexes where the values 2, 4, and 6 should be inserted:
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
# The return value is an array: [1 2 3] containing the three
# indexes where 2, 4, 6 would be inserted in the original array
# to maintain the order.
