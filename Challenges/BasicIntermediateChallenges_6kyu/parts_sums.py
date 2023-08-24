print('From Code Wars.')
print()

def parts_sums(ls):
    
    '''
    This function sums parts of an array, reducing the size of it in each iteration, 
    and puts the result in a new list.
    ls = [0, 1, 3, 6, 10], ls = [1, 3, 6, 10], ls = [3, 6, 10], ls = [6, 10], ls = [10], ls =  []
    '''
    result = [sum(ls)]
    [result.append(result[-1] - ls[i]) for i in range(0, len(ls))]
    return result

print(parts_sums([0, 1, 3, 6, 10]))  
# Outputs - [20, 20, 19, 16, 10, 0]
