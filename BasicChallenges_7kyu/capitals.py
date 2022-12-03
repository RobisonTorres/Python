print('From Code Wars.')
print()

def capitals(word):

    # This function takes a word and return all\
    # indexes of capitalized letters.
    return [a[0] for a in enumerate(word) if a[1].isupper()]

print(capitals('CodEWaRs'))  # Outputs - [0, 3, 4, 6]
