print('From Code Wars')
print()

def friend(x):

    # This function maintains only names with 4 letters.
    return [name for name in x if name.isalpha() and len(name) == 4]

names = ["Ryan", "Kieran", "Jason", "Yous", '123']
print(friend(names))  # Outputs - ['Ryan', 'Yous']
