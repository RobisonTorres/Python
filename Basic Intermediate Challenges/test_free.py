print('Test Free - keep it clean')
print()

def queue_time(customers, n):

    total_minutes = 0
    while customers:
        sub = min(customers[0: n])
        total_minutes += sub
        minutes = [num - sub for num in customers[0:n]]
        customers[0: n] = minutes
        customers = [num for num in customers if num != 0]
    return total_minutes

print(queue_time([4, 8, 5, 2, 4], 1))
