print('From Code Wars.')
print()

def diamond(n):

    ''' You need to return a string that looks like a diamond shape when printed
    on the screen, using asterisk (*) characters. Trailing spaces should be removed,
    and every line must be terminated with a newline character (\n).'''

    if n == '' or n <= 0 or n % 2 == 0:
        return None
    new = []
    x = 1
    while x <= n:
        new.append((("*" * x).center(n)).rstrip() + '\\n')
        x += 2
    return ''.join(new + new[0: len(new) - 1][::-1])

print(diamond(3))  # Outputs -  *\n***\n *\n
