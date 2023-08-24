print('From Code Wars')
print()

def nb_year(p0, percent, aug, p):

    # This function calculates how many years\
    # it necessary to reach a future population.
    year = 0
    while p0 < p:
        p0 += int(p0 * (percent/100) + aug)
        year += 1
    return year

print(nb_year(1000, 2, 50, 1200))
# Outputs - 3 years. It means,\ starting with a population\
# of 1000 it will take 3 years to reach a population of 1200.
