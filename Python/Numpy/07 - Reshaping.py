import numpy as np
print('Numpy')
print()

# Reshaping means changing the shape of an array.
# By reshaping we can add or remove dimensions or
# change number of elements in each dimension.

# Convert the following 1-D array with 12 elements into a 2-D array.
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr1 = arr1.reshape(4, 3)
print(new_arr1)

# Convert the following 1-D array with 12 elements into a 3-D array.
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr2 = arr2.reshape(4, 1, 3)
print(new_arr2)

# Can We Reshape Into any Shape? Yes, as long as the elements
# required for reshaping are equal in both shapes.
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_arr3 = arr3.reshape(2, 4)
print(new_arr3)

# You are allowed to have one "unknown" dimension.
# Pass -1 as the value, and NumPy will calculate this number for you.
arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_arr4 = arr4.reshape(2, -1, 2)
# new_arr4 = arr4.reshape(2, 2, -1)
print(new_arr4)

# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.
arr5 = np.array([[1, 2, 3], [4, 5, 6]])
new_arr5 = arr5.reshape(-1)
print(new_arr5)

# Reorganizing arrays
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

reo = np.vstack([v1, v2])  # vstack or hstack
print(reo)
