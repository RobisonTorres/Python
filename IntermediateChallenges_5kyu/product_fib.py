from functools import lru_cache
print('From Code Wars.')
print()

@lru_cache(maxsize=None)
def fibonacci(n):

    # Fibonacci function.
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def productFib(prod):

    # Given a number, say prod (for product), we search two Fibonacci
    # numbers F(n) and F(n+1) such as: F(n) * F(n+1) = prod.
    fn_number = 0
    n = 1
    while fn_number < prod:
        fn_number = fibonacci(n) * fibonacci(n+1)
        n += 1
    return [fibonacci(n-1), fibonacci(n), fn_number == prod]

print(productFib(714))  # Outputs - [21, 34, True]
