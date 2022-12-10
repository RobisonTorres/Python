import numpy as np
print('Numpy')
print()

# The copy owns the data and any changes made to the copy
# will not affect original array, and any changes made to
# the original array will not affect the copy.
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

# The view does not own the data and any changes made to
# the view will affect the original array, and any changes
# made to the original array will affect the view.
arr = np.array([1, 2, 3, 4, 5])
y = arr.view()
arr[0] = 42
print(arr)
print(y)

# Check if Array Owns its Data - Every NumPy array has the
# attribute base that returns None if the array owns the data.
# Otherwise, the base attribute refers to the original object.
print(x.base)
print(y.base)
