print('From Code Wars.')
print()

def zeros(n):

    # This function calculates the number of trailing zeros
    # in a factorial of a given number.        
    count = 0
    while (n >= 5):
        n = n // 5
        count += n 
    return count

print(zeros(12))  # Outputs - 2 (12! = 479001600)