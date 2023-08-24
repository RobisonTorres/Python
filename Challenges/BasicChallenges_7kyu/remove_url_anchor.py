print('From Code Wars.')
print()

def remove_url_anchor(url):

    # This function removes everything after this symbol '#',
    # and return the result.
    return url[0:url.index('#')] if '#' in url else url

print(remove_url_anchor('www.wars.com#about'))  # Outputs - www.wars.com
