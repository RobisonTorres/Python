print('From Code Wars')
print()

def vert_mirror(strng):
    return '\n'.join([item[::-1] for item in strng.split('\n')])

def hor_mirror(strng):
    return '\n'.join([item for item in strng.split('\n')[::-1]])

def oper(fct, s):
    return vert_mirror(s) if fct == vert_mirror else hor_mirror(s)
    # return fct(s) - Clever.

print(oper(vert_mirror,("abcd\nefgh\nijkl\nmnop")))
# Outputs - dcba\nhgfe\nlkji\nponm

print(oper(hor_mirror,("abcd\nefgh\nijkl\nmnop")))
# Outputs - mnop\nijkl\nefgh\nabcd
