print('3W School.')
print()

a = 0
'''
while a < 6:
    print(a)
    a += 1
'''
'''
while a < 6:
    print(a)
    if a == 3:
        break  # The loop will break when i == 3.
    a += 1
'''
'''
while a < 6:
    a += 1
    if a == 3:
        continue  # The number 3 won't be printed.
    print(a)
'''

while a <= 6:
    print(a)
    a += 1
else:  # With the else statement is possible to print\
    # a phrase when the condition is no longer true.
    print('\'a\' is no longer less than 6.')

x = 0

while x <= 10:
    if x % 2 == 0:
        print(f'The number {x} is even.')
    else:
        print(f'The number {x} is odd.')
    x += 1

y = 5

while True:
    print(y)
    y -= 1
    if y <= 2:
        print('Breaking')
        break
