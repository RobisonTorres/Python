import ipaddress
print('From Code Wars.')
print()

def is_valid_IP(x):

    # This function checks whether a string is a valid IPv4 address.
    try: return str(ipaddress.ip_address(x)) == x
    except: return False

print(is_valid_IP('12.0.56.1'))  # Outputs - True
print(is_valid_IP('12.0.056.1'))  # Outputs - False
