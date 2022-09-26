print('From Code Wars.')
print()

def queue_time(customers, n):

    # This function calculates the amount of time required 
    # to attend all the customers in a queue.
    total_minutes = 0
    while customers:
        sub = min(customers[0: n])
        total_minutes += sub
        minutes = [num - sub for num in customers[0:n]]
        customers[0: n] = minutes
        customers = [num for num in customers if num != 0]
    return total_minutes

print(queue_time([4,8,5,2], 2))  # Output - 10 minutes
print(queue_time([], 1))  # Outputs - 0 minutes
