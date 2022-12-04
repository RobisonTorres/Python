import numpy as np
print('Numpy')
print()

# Slice elements from index 1 to index 5 from the following array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])  # Output - [2 3 4 5]

# Slicing 2-D Arrays
# From the second element, slice elements from index 1 to index 4 (not included):
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])  # Output - [7 8 9]

# From both elements, return index 2:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])  # Output - [3 8]

# Changing elements in an array:
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
a[:, 2] = 20  # Change in both arrays.
print(a)

# Example
a = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
b = np.max(a, axis=1).sum()  # 5 + 10
print(b)

A = np.array([
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
])

print(A[:2])  # Rows and Columns
