import numpy as np
print('Numpy')
print()

# A discrete difference means subtracting two successive elements.
# E.g. for [1, 2, 3, 4], the discrete difference
# would be [2-1, 3-2, 4-3] = [1, 1, 1]

# To find the discrete difference, use the diff() function.
arr = np.array([10, 15, 25, 5])
new_arr = np.diff(arr)
print(new_arr)  # Output - [ 5  10 -20]

# We can perform this operation repeatedly by giving parameter n.
# E.g. for [1, 2, 3, 4], the discrete difference with n = 2
# would be [2-1, 3-2, 4-3] = [1, 1, 1] , then, since n=2,
# we will do it once more, with the new result: [1-1, 1-1] = [0, 0]
arr = np.array([10, 15, 25, 5])
new_arr = np.diff(arr, n=2)
print(new_arr)  # Output - [  5 -30]

