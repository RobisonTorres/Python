print('From Code Wars.')
print()

def parse(text):

    # Write a simple parser that will parse and run Deadfish.
    # It has 4 commands, each 1 character long:
    # 'i': + 1, 'd': - 1, 's': ** 2, 'o': append()
    x = 0
    n = []
    for y in range(len(text)):
        if text[y] == 'i': x += 1
        if text[y] == 'd': x -= 1
        if text[y] == 's': x **= 2
        if text[y] == 'o': n.append(x)
    return n

print(parse("idiiidiisoso"))  # Outputs - [16, 256]
