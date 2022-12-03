print('From Code Wars')
print()

def reverse_words(text):

    # This function reverses each word in the string.
    return ' '.join((reversed(text[::-1].split(' '))))
    # The 'split' makes the 'reverse' applies in each word rather than in each letter.

print(reverse_words('double  spaced  words'))  # Outputs - elbuod  decaps  sdrow
