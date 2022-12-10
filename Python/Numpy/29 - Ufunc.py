import numpy as np
print('Numpy')
print()

# ufuncs stands for "Universal Functions" and they are
# NumPy functions that operates on the ndarray object.

'''
What is Vectorization?

Converting iterative statements into a vector based operation 
is called vectorization. It is faster as modern CPUs are
optimized for such operations. Add the Elements of Two Lists:

list 1: [1, 2, 3, 4]

list 2: [4, 5, 6, 7]

One way of doing it is to iterate over both of the lists 
and then sum each elements.
'''

# Without ufunc, we can use Python's built-in zip() method:
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
    z.append(i + j)
print(z)

# NumPy has a ufunc for this, called add(x, y) that will produce the same result.
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)
