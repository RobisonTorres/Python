import numpy as np
print('Numpy')
print()

# Splitting is reverse operation of Joining.
# We use array_split() for splitting arrays, we pass it
# the array we want to split and the number of splits.

# Split the array in 3 parts:
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 3)
print(new_arr)

# Split the array in 4 parts:
# If the array has less elements than required, it will
# adjust from the end accordingly.
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 4)
print(new_arr)

# Split the 2-D array into three 2-D arrays.
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
new_arr = np.array_split(arr, 3)
print(new_arr)

# The example below also returns three 2-D arrays, but they
# are split along the row (axis=1).
# Split the 2-D array into three 2-D arrays along rows.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12],
                [13, 14, 15], [16, 17, 18]])
new_arr = np.array_split(arr, 3, axis=1)
print(new_arr)
