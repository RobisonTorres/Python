print('From Code Wars.')
print()

def stationary(num):
   
    # This function finds the stationary number.
    numbers = [0]
    while num != numbers[-1]:
        numbers.append(num)
        digits = [n for n in str(num)][::-1]
        remainders = [10 ** int(n) % 13 for n in range(0, len(str(num)))]
        num = sum([int(x[0]) * x[1] for x in zip(digits, remainders)])
    return numbers[-1]

print(stationary(1234567))
