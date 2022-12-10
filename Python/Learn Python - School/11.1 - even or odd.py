print('Even or Odd.')
print()

number = int(input('Type any integer number: '))
result = number % 2  # the result (= 0) is False, and the result (= 1) is True.
if result:  # True.
    print(f'The number {number} is odd.')
else:
    print(f'The number {number} is even.')

