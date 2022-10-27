print('Test Free - keep it clean')
print()

def solution(n):

    # This function...
    nums = []
    num = str(n)
    while num:
        nums.append(num[0] + '0' * len(num[1:]))
        num = num[1:]
    numbers = [int(n) for n in nums if not n.startswith('0')]

    dict_M = {1: 'M', 2: 'MM', 3: 'MMM', 4: 'IV', 5: 'V', 6: 'VI',
              7: 'VII', 8: 'VIII', 9: 'IX'}

    dict_C = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC',
              7: 'DCC', 8: 'DCCC', 9: 'CM'}

    dict_D = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX',
              7: 'LXX', 8: 'LXXX', 9: 'XC'}

    dict_U = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI',
              7: 'VII', 8: 'VIII', 9: 'IX'}

    m = int((numbers[0])/ 1000)
    c = int((numbers[1])/ 100)
    d = int((numbers[2])/ 10)
    return dict_M[m] + dict_C[c] + dict_D[d] + dict_U[numbers[3]]

print(solution(1999))
