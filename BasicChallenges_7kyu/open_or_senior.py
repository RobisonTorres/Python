print('From Code Wars')
print()

def open_or_senior(data):

    # This function categorizes a person as 'Senior' or 'Open'
    # based on his/ her age and 'handicap'.
    return ['Senior' if p[0] >= 55 and p[1] > 7 else 'Open' for p in data]
    # return [...if age >= 55 and handicap >= 8
    # else "Open" for (age, handicap) in data]

club = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
print(open_or_senior(club))
# Outputs - ['Open', 'Open', 'Senior', 'Open', 'Open', 'Senior']
