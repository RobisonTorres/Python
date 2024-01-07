print('From Code Wars.')
print()

def count_smileys(arr):

    # Given the array, this function counts how many
    # valid smileys there are.
    faces = [':-)', ':)', ':~)', ':-D', ':D', ':~D',
             ';-)', ';)', ';~)', ';-D', ';D', ';~D']
    return len([ch for ch in arr if ch in faces])

print(count_smileys(([':)', ';(', ';}', ':-D'])))  # Outputs - 2
print(count_smileys(([';D', ':-(', ':-)', ';~)'])))  # Outputs - 3
