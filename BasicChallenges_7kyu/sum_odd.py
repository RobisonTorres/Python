print('From Code Wars')
print()

def sum_odd(n):

    # Given the triangle of consecutive odd numbers.
    # It calculates the sum of the numbers in the nth row of this triangle.
    return sum([num for num in range(n * n - n, n * n + n) if num % 2 != 0])
    # return n**3 - Clever.

print(sum_odd(3))  # Outputs - 27
'''
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
'''
