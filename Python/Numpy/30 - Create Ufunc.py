import numpy as np
print('Numpy')
print()

# To create your own ufunc, you have to define a function,
# like you do with normal functions in Python, then you
# add it to your NumPy ufunc library with the frompyfunc() method.

# The frompyfunc() method takes the following arguments:

# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.

# Create your own ufunc for addition:
def my_add(x, y):
    return x + y

my_add = np.frompyfunc(my_add, 2, 1)  # Name, N. Arrays, Output.

print(my_add([1, 2, 3, 4], [5, 6, 7, 8]))

# Check if a function is a ufunc:
print(type(np.add))
