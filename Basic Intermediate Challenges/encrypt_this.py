print('From Code Wars.')
print()

def encrypt_this(text):
    
    # This function encrypts a string based on this rules:
    # 1 - The first letter must be converted to its ASCII code.
    # 2 - The second letter must be switched with the last letter
    new_text = []
    while len(new_text) < len(text.split()):
        for w in text.split():
            if len(w) == 1:
                new_text.append(str(ord(w)))
            elif len(w) == 2:
                new_text.append(str(ord(w[0])) + w[1])
            else:
                new_text.append(str(ord(w[0])) + w[-1] + w[2:-1] + w[1])
    return ' '.join(new_text)

print(encrypt_this("Thank you Piotr for all your help"))
# Outputs - 84kanh 121uo 80roti 102ro 97ll 121ruo 104ple
