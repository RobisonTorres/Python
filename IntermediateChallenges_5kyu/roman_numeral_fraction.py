print('From Code Wars.')
print()

def roman_numeral(n):

    # This function takes a positive integer (1 - 9999) as its parameter and returns
    # a string containing the Roman Numeral representation of that integer.
    nums = []
    num = str(n)
    while num:
        nums.append(num[0] + '0' * len(num[1:]))
        num = num[1:]
    numbers = [int(n) for n in nums if not n.startswith('0')]
    dict_M = {
        1000: 'M', 2000: 'MM', 3000: 'MMM', 4000: 'IV',5000: 'V', 6000: 'VI', 7000: 'VII', 8000: 'VIII', 9000: 'IX', 
        100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 
        10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    
    return ''.join([dict_M[r] for r in numbers])

def fraction_numeral(f):

    # This function takes a positive fraction (0 - 11) as its parameter and returns
    # a string containing the Roman Numeral representation of that fraction.
    fraction = {
        0: '', 1: '.', 2: ':', 3: ':.', 4: '::', 5: ':.:', 6: 'S',
        7: 'S.', 8: 'S:', 9: 'S:.', 10: 'S::', 11: 'S:.:'}
    return fraction[f]

def roman_fractions(n, fraction=False):

    # This function takes a number with its fractional component and 
    # returns the Roman Numeral representation of it (i.e: 1.9/12 -> IS:.).
    if n == 0 and fraction == False:
        return 'N'
    elif n not in range(0, 5001) or fraction not in range(0, 12):
        return 'NaR'
    else:
        result = ''
        result += roman_numeral(n)
        if fraction:
            result += fraction_numeral(fraction)
        return result

print(roman_fractions(1, 9))