print('From Code Wars')
print()

def series_sum(n):

    # Your task is to write a function\
    # which returns the sum of following series up to nth term(parameter).
    # Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
    x = 1
    d = 4
    for num in range(1, n):
        x += 1 / d
        d += 3
    return f'{x:.2f}' if n != 0 else f'{n:.2f}'

print(series_sum(3))  # Outputs - 1.39
