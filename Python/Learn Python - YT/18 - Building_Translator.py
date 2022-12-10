print('Building a Translator.')
print()

def translate(phrase):
    translation = ' '
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation + 'R'
            else:
                translation = translation + 'r'
        else:
            translation = translation + letter
    return translation

a = input('Enter the phrase that you want to translate: ')
print(translate(a))
