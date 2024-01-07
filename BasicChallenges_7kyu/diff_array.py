print('From Code Wars')
print()

def number(bus_stops):

    # This function calculates the difference between two numbers inside a list,
    # nested in another list and return the total.
    return sum([num[0] - num[1] for num in bus_stops])

print(number([[10, 0], [3, 5], [5, 8]]))  # Outputs - 5
