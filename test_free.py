import sys, subprocess
subprocess.run('cls', shell=True)
print('Test Free')
print()
# crt + D / alt + mouse / alt + up or down / shift + alt + up or down / crt + l
# crt + N .. crt + k, m .. crt + s

def scramble(s1, s2):

    return set(s2).issubset(set(s1))

print(scramble("scriptjavx", "javascript"))
