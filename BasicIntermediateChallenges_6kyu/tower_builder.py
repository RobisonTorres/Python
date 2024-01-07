print('From Code Wars.')
print()

def tower_builder(n_floors):

    # This function builds a tower of asterisks based on any
    # given number (number of floors).
    new = ['*'.center(2 * n_floors - 1)]
    while len(new) != n_floors:
        new.append(('**' + (new[-1]).strip()).center(2 * n_floors - 1))
    return '\n'.join(new)

print(tower_builder(5))  # Outputs:

# '    *    '
# '   ***   '
# '  *****  '
# ' ******* '
# '*********'
