print('From Code Wars.')
print()

def is_valid_walk(walk):

    # This function determines if a walk is valid or not.
    return walk.count('n') == walk.count('s') and \
           walk.count('e') == walk.count('w') and len(walk) == 10

print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # True.
