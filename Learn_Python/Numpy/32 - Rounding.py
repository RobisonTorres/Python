import numpy as np
print('Numpy')
print()

# There are primarily five ways of rounding off decimals in NumPy:

# Truncation - Remove the decimals, and return the float number
# closest to zero. Use the trunc() and fix() functions.
arr = np.trunc([-3.1666, 3.6667])  # or np.fix
print(arr)

# Rounding - The around() function increments preceding digit or
# decimal by 1 if >=5 else do nothing.

arr = np.around(3.1666, 2)
print(arr)

# Floor - The floor() function rounds off decimal to nearest lower integer.
arr = np.floor([-3.1666, 3.6667])
print(arr)

# Ceil - The ceil() function rounds off decimal to nearest upper integer.
arr = np.ceil([-3.1666, 3.6667])
print(arr)
