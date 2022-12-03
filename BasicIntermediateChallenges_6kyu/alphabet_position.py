print('From Code Wars.')
print()

def alphabet_position(text):

    # This function converts letter to number based on alphabetic position.
    return ' '.join([str(ord(num) - 96) for num in text.lower() if num.isalpha()])

print(alphabet_position('The sunset sets at twelve o\' clock.'))
# Outputs - 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
