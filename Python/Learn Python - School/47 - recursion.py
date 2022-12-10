print('Working with recursion.')
# The fundamental part of recursion is self-reference\
# - functions calling themselves.

# A classic example of a function that is implemented recursively is the\
# factorial function, which finds the product of all positive integers\
# below a specified number.

def factorial(x):
    if x == 1:  # base case.
        return 1
    else:
        return x * factorial(x-1)
print(factorial(5))

# The base case acts as the exit condition of the recursion.
# It has no base case,\
# so it runs until the interpreter runs out of memory and crashes.
