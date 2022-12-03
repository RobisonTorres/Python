print('From Code Wars')
print()

def reverse_letter(string):

    # This function reverse any given string\
    # while removing any non-alphabetic character.
    return ''.join([let for let in string if let.isalpha()])[::-1]

print(reverse_letter('ultr53o?n'))  # Outputs - nortlu
