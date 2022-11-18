print('From Code Wars.')
print()

def consonant_value(s):

    # Given a lowercase string that has alphabetic characters only and
    # no spaces, return the highest value of consonant substrings.  
    s = ''.join([' ' if l in 'aeiou' else l for l in s])
    return max([sum([(ord(num) - 96) for num in x]) for x in s.split(' ')])
    # return max(sum(ord(x)-96 for x in c) for c in re.split('[aeiou]',s)) - Clever.

print(consonant_value("zodiac"))  # Outputs - 26
