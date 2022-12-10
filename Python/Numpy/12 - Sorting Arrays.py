import numpy as np
print('Numpy')
print()

# Sorting means putting elements in an ordered sequence.
# The NumPy ndarray object has a function called sort(),
# that will sort a specified array.

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
# This method returns a copy of the array, leaving the original array unchanged.

# If you use the sort() method on a 2-D array, both arrays will be sorted:
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

