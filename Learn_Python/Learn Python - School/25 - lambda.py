print('3W School.')
print()

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments,\
# but can only have one expression.

x = lambda a: a * 5
print(x(5))

# Or in a different way:
def multi_5(num):
    return num * 5

# Others example:
y = lambda a, b: a * b
print(y(5, 6))

z = lambda a, b, c: a + b + c
print(z(1, 2, 3))

def my_func(n):
    return lambda a: a * n

my_double = my_func(2)

print(my_double(11))
print(my_double(5))

print((lambda a: a ** 2)(6))

