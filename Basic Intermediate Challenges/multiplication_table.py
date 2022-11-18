print('From Code Wars.')
print()

def multiplication_table(size):
    
    # Your task, is to create NxN multiplication table, 
    # of size provided in parameter.
    return [[n*m for n in range(1, size+1)] for m in range(1, size + 1)]

print(multiplication_table(3))  # Outputs - [[1,2,3],[2,4,6],[3,6,9]]
