print('From Code Wars.')
print()


def solution(n):

    # This function takes a positive integer as its parameter and returns
    # a string containing the Roman Numeral representation of that integer.
    nums = []
    num = str(n)
    while num:
        nums.append(num[0] + '0' * len(num[1:]))
        num = num[1:]
    numbers = [int(n) for n in nums if not n.startswith('0')]

    dict_M = {1000: 'M', 2000: 'MM', 3000: 'MMM', 40000: 'IV',5000: 'V', 6000: 'VI',
              7000: 'VII', 8000: 'VIII', 9000: 'IX', 
              100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC',
              700: 'DCC', 800: 'DCCC', 900: 'CM', 
              10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX',
              70: 'LXX', 80: 'LXXX', 90: 'XC', 
              1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI',
              7: 'VII', 8: 'VIII', 9: 'IX'}
    
    return ''.join([dict_M[r] for r in numbers])

print(solution(1990))
