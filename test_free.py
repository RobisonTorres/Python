import sys, subprocess
subprocess.run('cls', shell=True)
print('Test Free - Inter. Challenges - 100')
print()
# crt + D / alt + mouse / alt + up or down / shift + alt + up or down / crt + l
# crt + N .. crt + k, m .. crt + s

def cakes(recipe, available):
    
    # This function...
    return [list(recipe.keys()), list(available.keys())]
    '''
    if recipe.keys() in available.keys() and all([n > 0 for n in available.values()]):
        return "bake some cakes"
    else:
        return 0
    '''
recipe = {"flour": 500, "sugar": 200, "eggs": 1, "milk": 10}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))
