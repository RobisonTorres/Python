import numpy as np
print('Numpy')
print()

# What is the difference between summation and addition?
# Addition is done between two arguments whereas summation happens over n elements.

# Add the values in arr1 to the values in arr2:
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
new_arr = np.add(arr1, arr2)
print(new_arr)

# Sum the values in arr1 and the values in arr2:
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr)

# If you specify axis=1, NumPy will sum the numbers in each array.
arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 4, 6])
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)

# Cumulative sum means partially adding the elements in array.
# E.g. The partial sum of [1, 2, 3, 4]
# would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
# Perform partial sum with the cumsum() function.
arr = np.array([1, 2, 3, 4])
newarr = np.cumsum(arr)
print(newarr)
