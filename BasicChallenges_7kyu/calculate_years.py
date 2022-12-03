print('From Code Wars')
print()

def calculate_years(principal, interest, tax, desired):

    # This function calculates how many years\
    # is necessary to reach a desired amount of money.
    year = 0
    while principal < desired:
        principal += principal * interest - principal * interest * tax
        year += 1
    return year

print(calculate_years(1000, 0.05, 0.18, 1100))
# Outputs - 3 years. It means,\ starting with a principal\
# of 1000 it will take 3 years to reach a desired amount of 1100.
