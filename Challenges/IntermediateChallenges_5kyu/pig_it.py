print('From Code Wars.')
print()

def pig_it(string):

    # This function moves the first letter of each word to the end of it,
    # then adds "ay" to the end of the word. Leave punctuation marks untouched.
    return ' '.join([w[1:] + w[0] + 'ay' if w.isalpha() else w for w in string.split()])

print(pig_it('Pig latin is cool !')) # Output - igPay atinlay siay oolcay ! 
