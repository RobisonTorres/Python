import sys, subprocess
subprocess.run('cls', shell=True)
print('Test Free')
print()
# crt + D / alt + mouse / alt + up or down / shift + alt + up or down / crt + l
# crt + N .. crt + k, m .. crt + s

def fibonacci(n):
    if n <= 1:  # base case
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def test(number):

    fn_number = 0
    n = 0
    while fn_number < number:
        fn_number = fibonacci(n) * fibonacci(n+1)
        n += 1
    if fn_number == number:
        return [fibonacci(n-1), fibonacci(n), True]
    else:
        return [fibonacci(n-1), fibonacci(n), False]

print(test(4895))
