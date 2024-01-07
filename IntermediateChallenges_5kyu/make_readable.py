print('From Code Wars.')
print()

def make_readable(t):
    
    # This function takes a integer (seconds) as input and 
    # returns the time in a format of (HH:MM:SS)
    return f'{int(t/3600):02}:{int(t/60%60):02}:{int(t%60):02}'

print(make_readable(359999))  # Outputs - 99:59:59
