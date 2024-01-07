print('From Code Wars.')
print()

def max_rot(n):

    # This function returns the max value\
    # after rotating one digit to the right.
    n = str(n)
    list_number = [n]
    rot = 0
    while len(n) - 1 > rot:
        n = list(n)
        add = n.pop(rot)
        n = ''.join(n) + add
        list_number.append(n)
        rot += 1
    return int(max(list_number))
print(max_rot('56789'))  # Outputs - 68957
# ['56789', '67895', '68957', '68579', '68597']
