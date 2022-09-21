print('From Code Wars.')
print()

def queue_time(customers, n):

    # This function...
    if customers:
        return sum(customers)/ n if len(customers) > n else max(customers)
    else:
        return 0

print(queue_time([1,2,3,4,5], 100))
print(queue_time([], 1))
