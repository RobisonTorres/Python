print('From Code Wars.')
print()

def to_weird_case(str):
    
    # This function takes a string and returns the same string with all even indexed
    # characters in each word upper cased, and all odd indexed characters in lower cased.
    list_letters = []
    string = str.split()
    for i in range(len(string)):
         list_letters.append(''.join([l.upper() if n % 2 == 0  else l.lower() 
                            for n, l in enumerate(string[i])]))
    return ' '.join(list_letters)
    # return ' '.join([''.join([y.lower() if i%2 else y.upper() for i, y in enumerate(x)])
    # for x in string.split()]) - Clever.

print(to_weird_case('Weird string case'))  # Outputs - WeIrD StRiNg CaSe
