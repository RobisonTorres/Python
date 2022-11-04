print('From Code Wars.')
print()

def diamond(n):

    # Make some diamonds!
    if n == '':
        return None
    else:
        new = []
        x = 1
        while x <= n:
            new.append((("*" * x).center(n)).rstrip() + '\\n')
            x += 2
        result = ''.join(new + new[0: len(new) - 1][::-1])
        return None if n % 2 == 0 or n <= 0 else result

print(diamond(3))  # Outputs -  *\n***\n *\n
