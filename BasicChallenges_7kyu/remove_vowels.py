print('From Code Wars.')
print()

def disemvowel(string_):

    # This function will remove all vowels from the input.
    return ''.join([letter for letter in string_ if letter not in 'AEIOUaeiou'])

print(disemvowel('This website is for losers LOL'))
# Outputs - Ths wbst s fr lsrs LL
