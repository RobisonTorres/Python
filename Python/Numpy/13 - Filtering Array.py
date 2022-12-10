import numpy as np
print('Numpy')
print()

# Getting some elements out of an existing array and
# creating a new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.

# Create an array from the elements on index 0 and 2:
arr = np.array([41, 42, 43, 44])
filter_arr = [True, False, True, False]
new_arr = arr[filter_arr]
print(new_arr)

# Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
    # if the element is higher than 42, set the value to True, otherwise False:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

new_arr = arr[filter_arr]
print(filter_arr)
print(new_arr)

# The above example is quite a common task in NumPy and NumPy
# provides a nice way to tackle it. Create a filter array that
# will return only values higher than 42:
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
new_arr = arr[filter_arr]
print(filter_arr)
print(new_arr)
