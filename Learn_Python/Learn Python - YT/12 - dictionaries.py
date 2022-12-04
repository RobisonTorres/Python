print('Working with dictionaries.')
months_conversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December',

}
print(months_conversions['Nov'])
print(months_conversions.get('Dec'))
print(months_conversions.get('Kq', 'Not a valid key.'))
