print('3W School.')
print()


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for value in adj:  # The inner loop will be executed\
    # one time for each iteration of the outer loop.

    for fruit in fruits:
        print(value, fruit)

for n in [0, 2]:  # For loops cannot be empty. So to avoid errors put a pass method.
    pass
