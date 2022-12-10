import datetime

print('3W School.')
print()

x = datetime.datetime.now()
'''
print(x)
print(x.year)
print(x.day)
print(x.strftime('%A'))
'''
y = datetime.datetime(2020, 5, 12)
# It's possible to create a variable as a date (year, month, day.)

print(y)
'''
print(y.strftime('%A'))  # It gives the weekday.
print(y.strftime('%a'))
print(y.strftime('%B'))  # Month.
print(y.strftime('%C'))  # Day
'''
