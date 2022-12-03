from datetime import datetime
print('From Code Wars.')
print()

def check_coupon(entered_code, correct_code, current_date, expiration_date):

    # This function checks if a coupon is valid or not.
    return entered_code is correct_code \
           and datetime.strptime(current_date, "%B %d, %Y") \
           <= datetime.strptime(expiration_date, "%B %d, %Y")

print(check_coupon('123', '123', 'September 5, 2014', 'October 1, 2014'))
# Outputs - True
print(check_coupon('123a', '123', 'September 5, 2014', 'October 1, 2014'))
# Outputs - False
