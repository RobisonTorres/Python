print('From Code Wars')
print()

def printer_error(s):

    # This function counts letters above letter 'n' in a string,\
    # and show the result beside the total amount of letters.
    return str(len([let for let in s if let > 'm'])) + '/' + str(len(s))
    # return '{}/{}'.format(len([let for let in s if let > 'm']), len(s))

print(printer_error('aaaxbbbbyyhwawiwjjjwwm'))  # Outputs - 8/22
