print('Fibonacci sequence.')
print()

num = int(input())
def fibonacci(n):
    if n <= 1:  # base case
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for number in range(num):
    print(fibonacci(number))
