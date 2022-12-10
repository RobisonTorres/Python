print('3W School.')
print()

fruits = ['Banana', 'Kiwi', 'Apple', 'Mango', 'Strawberry']

'''
for fruit in fruits:
    print(fruit)
    if fruit == 'Mango':
        break  # With the break statement we can stop a iteration, 'Mango' appears.
'''
'''
for fruit in fruits:
    if fruit == 'Mango':
        break  # 'Mango' doesn't appear.
    print(fruit)
'''
'''
for fruit in fruits:
    if fruit == 'Mango':
        continue  # The continue statement will pass the given parameter.
    print(fruit)
'''
'''
for fruit in fruits:
    print(fruit + ' none')
'''

text = 'this is a simple text.'
count = 0

for letter in text:
    if letter == 't':
        count += 1
print(count)
