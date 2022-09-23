print('From Code Wars.')
print()

def queue_time(customers, n):

    # This function...
    if customers:
        if len(customers) <= n:
            return max(customers)
        elif n == 1:
            return sum(customers)
        else:
            x = 0
            y = 0
            total_minutes = customers
            while y <= len(customers):
                sub = min(total_minutes[0: n])
                time_curring = [num - sub for num in total_minutes[0+y:n+y]]
                x += sub
                y += n
    else:
        return 0

print(queue_time([4,8,5,2], 2))
print(queue_time([], 1))
