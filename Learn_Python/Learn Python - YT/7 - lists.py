print('Working with lists.')
print()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers.reverse()
print(numbers)
games = [

        'Battlefield 1', 'Gta V', 'Gta V', 'Gta V', 'Batman'

]
games_copy = games.copy()
games.sort()
print(games)
print(games[2])
games[0] = 'Tony Hawks'
print(games)
games.extend(numbers)
print(games)
games.append('Guitar hero')
print(games)
games.insert(1, 'Pes')
print(games)
games.insert(-1, 8)
print(games)
games.remove(6)
print(games)
#games.clear()
#print(games)
games.pop()
print(games)
print(games.index('Tony Hawks'))
print(games.count('Gta V'))
print(games_copy)
