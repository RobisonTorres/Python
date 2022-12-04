import numpy as np
print('Numpy')
print()

# Numpy Boolean Arrays

arr = np.array(range(1, 6))
test = list(arr > 3)
print(test)
# Outputs - [False, False, False, True, True]

# It is possible to combine.
print(list(arr[test]))  # [4, 5]
