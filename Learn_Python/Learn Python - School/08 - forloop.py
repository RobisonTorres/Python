print('Testing For Loop.')

fruits = ['Banana', 'Apple', 'Cherry']


for fruit in reversed(fruits):
    print(fruit)

print()

[print(fruit) for fruit in fruits]  # For loop in comprehension list.

'''
for number in range(1, 10):
    print(number)

for letter in 'Banana':
    print(letter)#You can loop through the characters of string.
'''

[print(number) for number in range(1, 10)]  # 10 it's not included.
