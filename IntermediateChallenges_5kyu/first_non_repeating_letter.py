print('From Code Wars.')
print()

def first_non_repeating_letter(string):

    # Task - Write a function that takes a string, and returns 
    # the first character that is not repeated anywhere in the string.
    copy = string.lower()
    copy_count = ''.join([l for l in copy if copy.count(l) == 1])
    if copy == '' or copy_count == '':
        return ''
    else:
        try:
            return string[string.index(copy_count[0])]
        except:
            return string[string.index(copy_count[0].upper())]

print(first_non_repeating_letter('Toshiba'))  # Outputs - T
