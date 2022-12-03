print('From Code Wars.')
print()

def clean_string(s):
    
    # This function uses '#' as backspace in a string. Thus, every time 
    # there is a '#' in front of a character, this character will be removed.
    while '#' in s:
        if s[0] == '#':
            s = s[1:]
        else:
            i = s.index('#')
            s = s[0:i-1] + s[i+1:]
    return s

print(clean_string("abc#d##c"))  # "ac"
