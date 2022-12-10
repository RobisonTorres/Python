import numpy as np
print('Numpy')
print()

# Iterate on the elements of the following 1-D array:
arr = np.array([1, 2, 3])
for x in arr:
    print(x)

# In a 2-D array it will go through all the rows.
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)

# To return the actual values, the scalars, we have to
# iterate the arrays in each dimension.
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)

# Iterate on the elements of the following 3-D array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)

# To return the actual values, the scalars, we have to
# iterate the arrays in each dimension.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

# Iterating Arrays Using nditer()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)

# We can use op_dtypes argument and pass it the expected
# datatype to change the datatype of elements while iterating.
# NumPy does not change the data type of the element in-place
# (where the element is in array) so it needs some other space
# to perform this action, that extra space is called buffer, and
# in order to enable it in nditer() we pass flags=['buffered'].

# Iterate through the array as a string:

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
