from itertools import count, cycle, accumulate, product, permutations
print('Working with inter tools.')
print()

# The module itertools is a standard library that contains several\
# functions that are useful in functional programming.
# One type of function it produces is infinite iterators.

# The function count counts up infinitely from a value if it doesn't have a break.
for i in count(5):  # It starts at number 5.
    print(i)
    if i >= 10:  # It ends at number 10.
        break

# The function cycle infinitely iterates through an iterable
name = 'Robison'
'''
for letter in cycle(name):
    print(letter)
'''

# accumulate - returns a running total of values in an iterable.
nums = list(accumulate(range(8)))
print(nums)  # outcome - [0, 1, 3, 6, 10, 15, 21, 28]

# Product and permutation: These are used when you want to accomplish\
# a task with all possible combinations of some items.

letter = ('a', 'b')
print(list(product(letter, range(2))))
# outcome - [('a', 0), ('a', 1), ('b', 0), ('b', 1)]

print(list(permutations(letter)))
# outcome - [('a', 'b'), ('b', 'a')]

a={1, 2}

print(len(list(product(range(3), a))))
