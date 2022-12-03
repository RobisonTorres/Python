print('From Code Wars.')
print()

def tribonacci(signature, n):

    # This function is useless.
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res  # Clever.

print(tribonacci([1, 1, 1], 10))
# Outputs - [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
