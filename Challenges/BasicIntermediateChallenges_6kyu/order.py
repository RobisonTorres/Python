print('From Code Wars.')
print()

def order(sentence):

    # This function puts a string in order
    # based in the number present in each word.
    n = 1
    new = []
    while len(sentence.split()) >= n:
        new.append(''.join([w for w in sentence.split() if str(n) in w]))
        n += 1
    return ' '.join(new)
    # return ' '.join(sorted(words.split(), key=lambda w:sorted(w))) - Clever

print(order('is2 Thi1s T4est 3a'))  # Outputs - Thi1s is2 3a T4est
