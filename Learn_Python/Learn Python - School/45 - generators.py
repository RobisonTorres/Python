print('Working with generators.')
print()

# In short, generators allow you to declare a function that behaves like an iterator,\
# i.e. it can be used in a for loop.

def countdown():
    x = 5
    while x > 0:
        yield x
        x -= 1
for i in countdown():
    print(i)
# Using generators results in improved performance,\
# which is the result of the lazy (on demand) generation of values,\
# which translates to lower memory usage.\
# Furthermore, we do not need to wait until all the elements have been generated\
# before we start to use them.
