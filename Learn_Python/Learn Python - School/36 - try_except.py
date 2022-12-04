print('3W School.')
print()

try:
    print(x)
except:  # Since the try block raises an error, the except block will be executed.
    print('Something went wrong.')

# You can define as many exception blocks as you want,\
# e.g. if you want to execute a special block of code for a special kind of error:
try:
    print(y)
    print(y/0)
    # print( "a" + 1)
except (NameError, ZeroDivisionError):
    # Multiple exceptions can also be put into a single\
    # except block using parentheses,\
    # to have the except block handle all of them.
    print('Something went wrong.')

# Using the Else statement.
try:
    print('Hello!')
except:
    print('Something went wrong.')
else:
    print('Nothing went wrong.')

# Using the Finally statement.
try:
    print(x)
except:
    print('Something went wrong.')
finally:
    # The finally block, if specified, will be executed regardless\
    # if the try block raises an error or not.
    print('The try method is finished.')

'''
# Raising an exception
a = -1

if a < 0:
    raise Exception('Sorry, no numbers below zero.')

'''
b = 'hello'

if not type(b) is int:
    raise TypeError('Only numbers are allowed.')
