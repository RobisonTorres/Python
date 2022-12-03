print('From Code Wars.')
print()

def rot13(message):
    
    # Task - Create a function that takes a string and returns the string
    # ciphered with Rot13. If there are numbers or special characters 
    # included in the string, they should be returned as they are.
    numbers_position = [[(ord(l) + 13 if l < 'n' else ord(l) - 13) if l.islower()       
                        else (ord(l) + 13 if l < 'N' else ord(l) - 13) for l in word]
                        if word.isalpha() else word for word in message]
    
    letters_position = ''.join([''.join([chr(n) for n in g]) if isinstance(g, list)  
                                                        else g for g in numbers_position])
    return letters_position

print(rot13('ZiG28rBlTh'))  # Outputs - 'MvT28eOyGu'
# - Clever
# return message.translate(message.maketrans(
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
# 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))