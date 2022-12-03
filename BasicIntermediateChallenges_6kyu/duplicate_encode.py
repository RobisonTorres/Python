print('From Code Wars.')
print()

def duplicate_encode(word):

    # This function replaces a letter for ')' if the letter
    # appears more than once and for '(' otherwise.
    word = word.lower()
    return ''.join([')' if word.count(a) >= 2 else '(' for a in word])

print(duplicate_encode('din'))  # Outputs - (((
print(duplicate_encode('recede'))  # Outputs - ()()()
