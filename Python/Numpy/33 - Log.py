from math import log
import numpy as np
print('Numpy')
print()

# NumPy provides functions to perform log at the base 2, e and 10.
# We will also explore how we can take log for any base by creating a custom ufunc.

# Use the log2() function to perform log at the base 2.

# Find log at base 2 of all elements of following array:
arr = np.arange(1, 10)
print(arr)
print(np.log2(arr))
print(np.log2(81))  # Output - 6.33985

# Use the log10() function to perform log at the base 10.

# Find log at base 10 of all elements of following array:
arr = np.arange(1, 10)
print(np.log10(arr))
print(np.log10(81))  # Output - 1.90848

# Natural Log, or Log at Base e
# Use the log() function to perform log at the base e.

# Find log at base e of all elements of following array:
arr = np.arange(1, 10)
print(np.log(arr))

# NumPy does not provide any function to take log at any base,
# so we can use the frompyfunc() function along with inbuilt
# function math.log() with two input parameters and one output parameter:
np_log = np.frompyfunc(log, 2, 1)
print(np_log(100, 15))  # 100 - result, 15 - base, 1.70055 - equals.
