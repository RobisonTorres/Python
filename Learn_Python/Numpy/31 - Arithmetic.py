import numpy as np
print('Numpy')
print()

'''
You could use arithmetic operators + - * / directly between 
NumPy arrays, but this section discusses an extension of the 
same where we have functions that can take any array-like 
objects e.g. lists, tuples etc. and perform arithmetic conditionally.

Arithmetic Conditionally: means that we can define conditions
where the arithmetic operation should happen.
'''

# The add() function sums the content of two arrays, and return
# the results in a new array.
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

new_arr = np.add(arr1, arr2)
print(new_arr)

# The subtract() function subtracts the values from one
# array with the values from another array, and return the results in a new array.
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

new_arr = np.subtract(arr1, arr2)
print(new_arr)

# The multiply() function multiplies the values from one array with the
# values from another array, and return the results in a new array.
arr1 = np.array([2, 11, 12, 13, 14, 15])
arr2 = np.array([2, 21, 22, 23, 24, 25])

new_arr = np.multiply(arr1, arr2)
print(new_arr)

# The divide() function divides the values from one array with the values
# from another array, and return the results in a new array.
arr1 = np.array([2, 11, 12, 13, 14, 15])
arr2 = np.array([2, 21, 22, 23, 24, 25])

new_arr = np.divide(arr1, arr2)
print(new_arr)

# The power() function rises the values from the first array to the power
# of the values of the second array, and return the results in a new array.
arr1 = np.array([2, 11, 12, 13, 14, 15])
arr2 = np.array([2, 21, 22, 23, 24, 2])

new_arr = np.power(arr1, arr2)
print(new_arr)

# Both the mod() and the remainder() functions return the remainder of the values
# in the first array corresponding to the values in the second array,
# and return the results in a new array.
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
# You get the same result when using the remainder() function:
new_arr = np.mod(arr1, arr2)
print(new_arr)

# Quotient and Mod - The divmod() function return both the quotient and the
# the mod. The return value is two arrays, the first array contains the quotient
# and second array contains the mod.
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

new_arr = np.divmod(arr1, arr2)
print(new_arr)

# Both the absolute() and the abs() functions functions do the same absolute
# operation element-wise but we should use absolute() to avoid confusion with
# python's inbuilt math.abs()
arr = np.array([-1, -2, 1, 2, 3, -4])

new_arr = np.absolute(arr)
print(new_arr)

# Other examples;
new_arr += 3
print(new_arr)

# Multiply matrix
a = np.array([[2, 2, 3], [2, 1, 4]])
b = np.ones((3, 2))
c = np.matmul(a, b)
print(c)

# Finding the determinant
d = np.linalg.det(c)
print(d)

# Statistic
a = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
b = np.max(a, axis=1).sum()  # 15
print(np.min(a))
print(np.max(a))
print(np.mean(a))

