print('Test Free - keep it clean')
print()

def queue_time(customers, n):

    total_minutes = 0
    minutes = customers   
    while minutes:
        sub = min(total_minutes[0: n])
        x += sub
        minutes = [num - sub for num in minutes[0:n]]
        minutes = [num for num in minutes if num != 0]
    return minutes

print(queue_time([4,8,5,2], 2))
