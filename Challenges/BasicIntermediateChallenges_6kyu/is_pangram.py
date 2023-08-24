print('From Code Wars.')
print()

def is_pangram(s):

    # This function determines if a sentence is a pangram.
    return len(set([l for l in s.lower() if l.isalpha()])) == 26

print(is_pangram('The quick brown fox jumps over the lazy dog'))
# Outputs - True

'''
A pangram is a sentence that contains every single letter of the 
alphabet at least once.
'''
