print('From Code Wars.')
print()

def cakes(recipe, available):
    
    # Task - Write a function which takes the recipe and the available ingredients,
    # and returns the maximum number of cakes that can be made.
    try:
        result = []
        for key, value in recipe.items():
            result.append(int(available[key]/ value))
        return min(result)
    except: return 0

recipe = {"flour": 500, "sugar": 200, "eggs": 1, "milk": 10}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))  # Outputs - 2 cakes
