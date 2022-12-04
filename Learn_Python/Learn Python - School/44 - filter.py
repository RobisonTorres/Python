print('Working with filter')

# The function 'filter' filters an iterable by removing items that\
# don't match a predicate (a function that returns a Boolean).

numbers = list(range(0, 11))

result = list(filter(lambda x: x % 2 == 0, numbers))
# It removes all odd numbers from the numbers list.

for item in result:
    print(item)
