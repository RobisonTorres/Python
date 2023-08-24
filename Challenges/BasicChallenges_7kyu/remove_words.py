print('From Code Wars')
print()

def remove_duplicate_words(s):

    # This function removes duplicate words from any given string.
    new = []
    a = [new.append(word) for word in s.split() if word not in new]
    return ' '.join(new)

print(remove_duplicate_words('alpha beta beta gamma gamma gamma delta\
                            alpha beta beta gamma gamma gamma delta'))

# Outputs - alpha beta gamma delta
