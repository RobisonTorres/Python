print('From Code Wars')
print()

def sort_by_length(arr):

    # This function sorts an array by the length of each element of it,\
    # from the shortest to longest.
    return sorted(arr, key=len)

print(sort_by_length(["Teles", "Glasses", "Eyessssss", "Monocles"]))
# Outputs - ['Teles', 'Glasses', 'Monocles', 'Eyessssss']
