print('From Code Wars.')
print()

def words_to_marks(s):

    # This function turns letters into numbers 
    # based on alphabetic position, then sums the numbers.
    return sum([(ord(a) - 96) for a in list(s)])
    
print(words_to_marks('friendship'))  # Outputs - 108
