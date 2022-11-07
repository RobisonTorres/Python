print('From Code Wars.')
print()

def parse(text):

    x = 0
    n = []
    for y in range(len(text)):
        if text[y] == 'i':
            x += 1
        if text[y] == 'd':
            x -= 1
        if text[y] == 's':
            x **= 2
        if text[y] == 'o':
            n.append(x)
    return n

print(parse("faosdfads"))
