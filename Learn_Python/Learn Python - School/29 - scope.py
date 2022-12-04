print('3W School.')
print()

def my_func():
    x = "Rob"
    print(x)

my_func()
# print(x) - name 'x' is not defined.

z = 5  # Global variables are available from within any scope, global and local.

def my_func(number):
    global y
    y = number  # This variable can only be accessed inside the function.
    print(y)

    def my_inner_func():
        print(y / 2)
    my_inner_func()  # You have to call it in the end.

    print(y/z)

my_func(100)

a = 'Rob'

def my_name():
    global a  # Use the global keyword if you want\
    # to make a change to a global variable inside a function.

    a = 'Robison'
    print(a)

my_name()
print(a)
