import re
print('From Code Wars')
print()

def domain_name(url):

    match = re.findall(r'(?:http(?:s?)://)?(?:www.)?([\w-]+)', url)
    return match[0]
    # return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name') - Clever.

print(domain_name('http://www.zombie-bites.br.com'))  # Outputs - zombie-bites

'''
?: - It indicates that the subpattern is a non-capture subpattern.
That means whatever is matched in (?:\w+\s) , even though it's enclosed
by () it won't appear in the list of matches, only (\w+) will.
'''
