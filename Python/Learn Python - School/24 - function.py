print('3W School.')
print()

# Arbitrary arguments. * args

def my_func1(*names):
    return 'The person chosen is ' + names[-1] + '.'

print(my_func1('Rob', 'Kyo', 'Ana', 'Paul'))

# Keyword arguments.  kwargs

def my_func2(person1, person2, person3):
    return 'The person chosen is ' + person2 + '.'

print(my_func2(person1='Rob', person2='Ralph', person3='Bush'))

# Arbitrary keyword arguments.  ** kwargs

def my_func3(**person):
    return 'The person chosen is ' + person['last_name'] + '.'

print(my_func3(first_name='Rob', last_name='Torres'))

# Default parameter value.

def my_func4(country='Norway'):
    # If we call a function without giving an argument it uses a default value.

    return 'I\'m from ' + country

print(my_func4('Brazil'))
print(my_func4('Argentina'))
print(my_func4())

'''
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print(tri_recursion(2))
'''

def test(txt):
    print('Brazil' + txt)

test('!')

function = test
function('?')
success = function
success(' any')

# A function inside a function

def sqrt(num):
    return num ** (1/2)

def inside(fun, num, num1):
    print(fun(num)+num1)

inside(sqrt, 81, 1)
