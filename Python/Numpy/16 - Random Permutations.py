from numpy import random
import numpy as np
print('Numpy')
print()

# A permutation refers to an arrangement of elements.
# e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
# The NumPy Random module provides two methods for this:
# shuffle() and permutation().

# Randomly shuffle elements of following array:
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)
# The shuffle() method makes changes to the original array.

# Generate a random permutation of elements of following array:
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))
# The permutation() method returns a re-arranged array
# (and leaves the original array un-changed).
