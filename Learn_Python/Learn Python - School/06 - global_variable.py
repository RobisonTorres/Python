print('Testing W3')
print()

a = 'Awesome.'
b = 'Fantastic'
def function():
    global b, a  # Also, use the global keyword if you want to
# change a global variable inside a function.
    a = 'None'
    b = 'Great!'
    print('Python is ' + b)
    print(a)
print()
function()
print(b)
print(a)
