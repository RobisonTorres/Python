print('Test Free - keep it clean')
print()

def queue_time(customers, n):

    # This function...
    if customers:
        if len(customers) <= n:
            return max(customers)
        elif n == 1:
            return sum(customers)
        else:
            return "To do"
    else:
        return 0

print(queue_time([4,8,5,2], 1))
print(queue_time([], 1))
