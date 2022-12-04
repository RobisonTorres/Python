import numpy as np
print('Numpy')
print()

# Get the first element from the following array:
my_arr = np.array([1, 2, 3, 4])
print(my_arr[0])

# Access the element on the first row, second column(2-D Array):
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0, 1])

# Access the third element of the second array of the first array(3-D Array):
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
