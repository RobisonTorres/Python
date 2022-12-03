print('From Code Wars.')
print()

def high(x):

    # This function converts words to numbers based on alphabetic position.
    # Then it sums the numbers of each word, and return the word that has the
    # highest number.
    text = x.split()
    txt = [list(w) for w in text]
    new = []
    r = 0
    while len(text) > r:
        new.append(sum([ord(num) - 96 for num in txt[r]]))
        r += 1
    return text[new.index(max(new))]

print(high('man i need a taxi'))  # Outputs - taxi
