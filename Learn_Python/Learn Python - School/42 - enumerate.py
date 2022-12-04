print('Working with enumerate.')
print()

# The enumerate() function takes a collection \
# and returns it as an enumerate object.

# The enumerate() function adds a counter\
# as the key of the enumerate object.

some = [1, 2, 2]

print(enumerate(some, 1))  # Output - <enumerate object at 0x000001C73B855600>
print(list(enumerate(some, 1)))  # [(1, 1), (2, 2), (3, 2)]
enumerate(some, 0)  # In this case, the 0 will determine the start point.
