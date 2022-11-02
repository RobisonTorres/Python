print('From Code Wars.')
print()

def sq_in_rect(l, w):
    
    # This function cuts a given rectangle into squares, 
    # and returns the side of each square.
    a = l * w
    d = [l, w]
    s = []
    while a > 0:
        a -= min(d) ** 2
        s.append(min(d))
        d = [min(d), int(a / min(d))]
    return None if l == w else s

print(sq_in_rect(20, 14))  # Outputs - [14, 6, 6, 2, 2, 2]
