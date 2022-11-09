print('From Code Wars.')
print()

def meeting(s):

    # This function makes a list of names uppercase, sorted in alphabetical
    # order by last name, and divides the result by parentheses.
    list_names = sorted([f'({", ".join(name.split(":")[::-1]).upper()})' for name in s.split(';')])
    return ''.join(list_names)

print(meeting("Fred:Corwill;Barney:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))
# Outputs - (CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(TORNBULL, BARNEY)(TORNBULL, BJON)
