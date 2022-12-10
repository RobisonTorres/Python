import numpy as np
print('Numpy')
print()

# Zeros matrix
matrix_zeros = np.zeros(5)
# print(matrix_zeros)  # [0. 0. 0. 0. 0.]

# matrix_zeros = np.zeros((2, 3, 3, 2))  # or ((2, 3, 3)) changes the shape.
# print(matrix_zeros)

matrix_ones = np.ones((2, 3, 3))
print(matrix_ones)

# Any other number
matrix_any = np.full((3, 3), 15)
# print(matrix_any)

# Full like
matrix_like = np.full_like(matrix_zeros, 1)
# print(matrix_like)

# Exercise: Build a simple matrix
matrix_ones = np.ones((5, 5))
matrix_zeros = np.zeros((3, 3))

matrix_zeros[1, 1] = 9

matrix_ones[1:4, 1: 4] = matrix_zeros
print(matrix_ones)
'''
[[1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 9. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]]
'''
