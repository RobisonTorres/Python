print('From Code Wars.')
print()

def decrypt(text, n):
    
    # This function decrypts string.
    for x in range(n):
        x = int(len(text) / 2)
        if len(text) % 2 != 0:
            text = ''.join([''.join(a) for a in list(zip(text[x:], text[0:x]))]) + text[-1]
        else:
            text = ''.join([''.join(a) for a in list(zip(text[x:], text[0:x]))])
    return text

def encrypt(text, n):

    # This function encrypts string.
    for x in range(n):
        text = ''.join([l if n % 2 != 0 else '' for n, l in enumerate(text)] + 
                        [l if n % 2 == 0 else '' for n, l in enumerate(text)])
        # text = text[1::2] + text[::2] - Clever    
    return text

print(decrypt("This is a test!", 2))  # Outputs - s eT ashi tist!
print(encrypt('s eT ashi tist!', 2))  # Outputs - This is a test!
