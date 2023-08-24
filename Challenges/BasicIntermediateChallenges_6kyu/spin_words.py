print('From Code Wars.')
print()

def spin_words(sentence):

    # This function reverse a word if its length is great than 5.
    return ' '.join([w[::-1] if len(w) >= 5 else w for w in sentence.split()])

print(spin_words('Hey fellow warriors'))  # Outputs - Hey wollef sroirraw
