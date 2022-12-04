import numpy as np
print('Numpy')
print()

# NumPy arrays have an attribute called shape that
# returns a tuple with each index having the number
# of corresponding elements.
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)  # Output - (2, 4)

# Create an array with 5 dimensions using ndmin using
# a vector with values 1,2,3,4 and verify that last dimension has value 4:
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)  # [[[[[1 2 3 4]]]]]
print('shape of array :', arr.shape)  # (1, 1, 1, 1, 4)
