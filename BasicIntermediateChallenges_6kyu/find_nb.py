print('From Code Wars.')
print()

def find_nb(m):

    # This function builds a pile of cubes and determines
    # how many cubes is necessary to sum to reach the volume of 'm'.
    n = 1
    vol = 1
    while m > vol:
        n += 1
        vol += n ** 3
    return - 1 if vol > m else n

print(find_nb(4183059834009))  # Outputs - 2022
