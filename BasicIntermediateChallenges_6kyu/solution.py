print('From Code Wars.')
print()

def solution(number):

    # This function creates an array of the multiples of 3 and 5
    # below a given number, and returns the sum of it.
    return sum([n for n in range(1, number) if n % 3 == 0 or n % 5 == 0])

print(solution(10))  # Outputs - 23
