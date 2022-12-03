print('From Code Wars')
print()

def find_short(s):

    # This function returns the shortest word's length from a group of words.
    return len(min(s.split(), key=len))

print(find_short('Lets all go on holiday somewhere very cold'))  # Outputs - 2
