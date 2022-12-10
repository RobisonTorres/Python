import numpy as np
print('Numpy')
print()

# Get the data type of an array object:
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

# Converting Data Type on Existing Arrays
# The best way to change the data type of an existing array,
# is to make a copy of the array with the astype() method.

# Change data type from float to integer by using 'i' as parameter value:
arr = np.array([1.1, 2.1, 3.1])
new_arr = arr.astype('i')
print(new_arr)
print(new_arr.dtype)
