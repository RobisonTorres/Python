print('From Code Wars.')
print()

def solution(roman):
    
    # This function takes a roman numeral representation (I - MMMCMXCIX), 
    # and returns its values as a numeric integer.
    roman_numbers = {

        'M': 1000, 'C': 100, 'D': 500, 'X': 10, 'L': 50, 'I': 1, 'V': 5
    }

    numbers = [roman_numbers[n] for n in [l for l in roman]]
    return sum([x[0] * (-1) if x[0] < x [1] else x[0] 
                for x in zip(numbers, numbers[1:] + [0])])

print(solution('MCMXC'))  # Outputs - 1990
