print('From Code Wars')
print()

def domain_name(url):
    
    # This function extract the url domain's name of a web site.
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')
    
    return url[0:url.find('.')]
    # return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name') - Clever.

print(domain_name('http://www.zombie-bites.com'))  # Outputs - zombie-bites
