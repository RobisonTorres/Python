print('3W School.')
print()

a = 60
b = 10
c = 12
'''
Short hand If statement.
if a > b: print(f'{a} is greater than {b}.')
print('a is greater than b.') if a > b else print('a is not greater than b.')
print('a') if a > b else print('=') if a == b else print('b')
if a > b and a > c:
    print('Both conditionals are true.')
if a > b or a > c:
    print('At least one conditional is true.')
'''

if a > 20:
    print('Yes, it is greater than 20')
    if a > 40:
        print('Yes, It is also greater than 40')
    else:
        print('It is not greater than 40')

if a > b:
    pass
