import re
print('From Code Wars.')
print()

def valid_phone_number(phone_number):
    
    # This function checks if a given string is a valid phone number.
    try:
        test_number = ''.join(re.findall(r'\d+', phone_number))
        return "({}{}{}) {}{}{}-{}{}{}{}".format(*test_number) == phone_number
    except: return False
    # return bool(re.match("^[(][0-9]{3}[)] [0-9]{3}-[0-9]{4}$", phone_number)) - Clever.

print(valid_phone_number("(123) 456-7890"))  # Outputs - True
