print('From Code Wars.')
print()

def data_reverse(data):

    # Task - A stream of data is received and needs to be reversed.    
    new_data = []
    while data:
        new_data.append(data[0:8])
        data = data[8:]
    return [n for z in new_data[::-1] for n in z]
   
print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))
# Outputs - [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
