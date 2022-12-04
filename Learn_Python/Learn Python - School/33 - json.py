import json

print('3W School.')
print()

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)  # Converting a json object to python.

# the result is a Python dictionary:
print(y)

z = json.dumps(y, indent=4, separators=(',', ':'))  # Converting a python object to json.
print(y)

print(json.dumps({'name': 'John', 'age': 30}))
print(json.dumps(42))
