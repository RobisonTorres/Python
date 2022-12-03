print('From Code Wars')
print()

def capitalize(s):

    # Given a string, capitalize the letters that occupy even indexes\
    # and odd indexes separately. Ex: ['AbCdEf', 'aBcDeF']
    a = ''.join([l.upper() if n % 2 else l for n, l in enumerate(s)])
    return [a, a.swapcase()]

print(capitalize('abracadabra'))  # Outputs - ['AbRaCaDaBrA', 'aBrAcAdAbRa']
