import numpy as np
print('Numpy')
print()

# To find the product of the elements in an array, use the prod() function.
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)  # Output - 24

# Find the product of the elements of two arrays:
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x)  # Output - 40320

# If you specify axis=1, NumPy will return the product of each array.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2], axis=1)
print(x)  # Output - [24 1680]

# Cumulative product means taking the product partially.
# E.g. The partial product of [1, 2, 3, 4] is
# [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
# Perform partial sum with the cumprod() function.
arr = np.array([5, 6, 7, 8])
new_arr = np.cumprod(arr)
print(new_arr)  # Output - [ 5   30  210 1680]
