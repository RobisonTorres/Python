print('From Code Wars.')
print()

def find_even_index(arr):

    # Your job is to take an array and find an index N where the sum
    # of the integers to the left of N is equal to the sum of the integers
    # to the right of N
    n = 0
    while sum(arr[:n]) != sum(arr[n+1:]) and n < len(arr):
        n += 1
    return n if n != len(arr) else -1

print(find_even_index([1, 2, 3, 4, 3, 2, 1]))  # Outputs - 3
print(find_even_index([20, 10, -80, 10, 10, 15, 35]))  # Outputs - 0
