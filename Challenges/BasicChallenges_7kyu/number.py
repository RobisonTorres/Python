print('From Code Wars')
print()

def number(lines):

    # This function takes a list and return each element prepended\
    # with a number, starting with 1.
    return [f'{item[0]}: {item[1]}' for item in (enumerate(lines, 1))]

print(number(['a', 'b', 'c']))  # Outputs - ['1: a', '2: b', '3: c']
print(number([]))  # Outputs - []
