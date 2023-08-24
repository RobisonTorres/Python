print('From Code Wars')
print()

def evaporator(content, evap_per_day, threshold):

    # This program tests the life of an evaporator containing a gas. 
    days = 0
    limit = content * threshold/ 100
    while content > limit:
        content = content - (content * evap_per_day/ 100)
        days += 1
    return days

print(evaporator(10, 10, 5))  # Outputs - 29 Days.
