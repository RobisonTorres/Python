print('From Code Wars.')
print()

def increment_string(strng):

    # Task - Your job is to write a function which increments a string, to create a new string.
    # If the string already ends with a number, the number should be incremented by 1. If 
    # the string does not end with a number. the number 1 should be appended to the new string.
    if strng and strng[-1].isnumeric():
        nums = ''.join([l if l.isnumeric() else ' ' for l in strng]).split()
        # num = s[len(s.rstrip("0123456789")):] - Clever.
        return strng[:-(len(nums[-1]))]  + str(int(nums[-1]) + 1).zfill(len(nums[-1]))
    return strng + '1'

print(increment_string('fo99obar100'))  # Outputs - fo99obar101
