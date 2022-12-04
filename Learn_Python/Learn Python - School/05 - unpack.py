print('Testing W3...')

fruits = ['Banana', 'Apple', 'Cherry']
fruits1 = ('Banana', 'Apple', 'Cherry')
a = True
x, y, z = fruits # Unpacking a list into multi variables.

print(x)
print(y)
print(z)
print(type(fruits))
print(type(a))

a, b, *c, d = [1, 2, 3, 4, 5, 6]
# A variable that is prefaced with an asterisk (*) takes all values\
# from the iterable that are left over from the other variables.
print(c)
print(d)
