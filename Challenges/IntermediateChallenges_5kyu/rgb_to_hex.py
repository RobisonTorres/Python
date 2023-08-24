print('From Code Wars.')
print()

def rgb_to_hex(r, g, b):

    # This function converts rgb color to hexadecimal.
    r = 0 if r < 0 else 255 if r > 255 else r
    g = 0 if g < 0 else 255 if g > 255 else g
    b = 0 if b < 0 else 255 if b > 255 else b
    return '%02X%02X%02X' % (r, g, b)

print(rgb_to_hex(254, 253, 252))  # Outputs - FEFDFC
# round = lambda x: min(255, max(x, 0))
# return ("{:02X}" * 3).format(round(r), round(g), round(b)) - Clever.
