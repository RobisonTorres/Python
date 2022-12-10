print('Working with map')

# The function map takes a function and an iterable as arguments,\
# and returns a new iterable with the function applied to each argument.


def even_odd(num):
    if num % 2 == 0:
        return f'The number {num} is even.'
    else:
        return f'The number {num} is odd.'

numbers = list(range(0, 11))

result = list(map(even_odd, numbers))

for item in result:
    print(item)

