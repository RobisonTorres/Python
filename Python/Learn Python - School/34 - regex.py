import re

print('3W School.')
print()

txt = "The rain in Spain"
x = re.search('^The.*Spain$', txt)  # regex can be used to check if a\
                                    # string contains the specified search pattern.
print(x)  # Outcome = <re.Match object; span=(0, 17), match='The rain in Spain'>

# The findall() function returns a list containing all matches.
y = re.findall('ai', txt)
print(y)

# Search where the first occurrence happens.
z = re.search('\s', txt)
print('The first white space is located in position', z.start())

# The split function returns a list where the string has been split at each match.
a = re.split('\s', txt)
print(a)  # Outcome = ['The', 'rain', 'in', 'Spain']

# The sub() function replaces the matches with the text of your choice.
b = re.sub('\s', '9', txt)
print(b)

# Match object
c = re.search(r"\bS\w+", txt)
print(c)
print(c.span())
print(c.string)
print(c.groups())
