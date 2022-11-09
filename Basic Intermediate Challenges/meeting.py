print('From Code Wars.')
print()

def meeting(s):

    # This function makes a list of names uppercase, sorted in alphabetical
    # order by last name, and divides the result by parentheses.
    list_names = sorted([f'({", ".join(name.split(":")[::-1]).upper()})' for name in s.split(';')])
    return ''.join(list_names)

print(meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))
