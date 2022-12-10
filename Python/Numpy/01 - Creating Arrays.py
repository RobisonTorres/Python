import numpy as np
print('Numpy')
print()

# NumPy aims to provide an array object that is up to 50x faster
# than traditional Python lists.
# Arrays are very frequently used in data science, where speed
# and resources are very important.

arr = [1, 2, 3, 4, 5]
numpy_arr = np.array(arr)
print(numpy_arr)
print()
# To create an ndarray, we can pass a list, tuple or any array-like
# object into the array() method, and it will be converted into an ndarray.

# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print()
# Create a 3-D array with two 2-D arrays, both containing two arrays with
# the values 1,2,3 and 4,5,6:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print()
# Check how many dimensions the arrays have:
print(arr.ndim)
print()
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)  # Output - 0
print(b.ndim)  # Output - 1
print(c.ndim)  # Output - 2
print(d.ndim)  # Output - 3

# Accessing items:
print(c[:, 2])  # Outputs - [3 6] - All rows of second column.
