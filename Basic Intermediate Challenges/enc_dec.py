print('From Code Wars.')
print()

def encode(st):

    # This function encodes a string changing the vowel letters
    # to numbers, fallowing this rule: a-1, e-2, i-3, o-4, u-5.
    vowel_code = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    return ''.join([str(vowel_code[l]) if l in ('aeiou') else l for l in st])
   
def decode(st):

    # This function decodes the encode function.
    nums_code = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}
    return ''.join([nums_code[int(n)] if n in ('12345') else n for n in st])
''' - Clever.
def encode(s, t=str.maketrans("aeiou", "12345")):
def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)  
'''
print(encode('How are you today?'))  # Outputs - H4w 1r2 y45 t4d1y?       
