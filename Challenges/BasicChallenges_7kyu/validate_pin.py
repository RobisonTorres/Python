print('From Code Wars')
print()

def validate_pin(pin):

    # This function will check first if all characters are numeric,\
    # then if it has only 4 or 6 digits.
    return pin.isnumeric() and (len(pin) == 4 or len(pin) == 6)
    # return pin.isnumeric() and len(pin) in (4, 6) - clever

print(validate_pin('1234'))  # Outputs - True
