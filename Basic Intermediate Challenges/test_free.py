print('Test Free - keep it clean')
print()

def to_weird_case(str):
    
    # This function...
    list_letters = []
    string = str.split()
    for i in range(len(string)):
         list_letters.append(''.join([l.upper() if n % 2 == 0  else l.lower() 
                            for n, l in enumerate(string[i])]))
    return ' '.join(list_letters)

print(to_weird_case('Weird string case'))  # Outputs - WeIrD StRiNg CaSe
