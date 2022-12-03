print('From Code Wars')
print()

def arithmetic(a, b, operator):

    # A simple calculator.
    if operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b
    elif operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return a / b

print(arithmetic(5, 2, 'add'))  # Outputs - 7
print(arithmetic(5, 2, 'subtract'))  # Outputs - 3
