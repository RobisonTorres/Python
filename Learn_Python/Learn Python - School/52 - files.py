print('Working with files')
print()

doc = open('mbox-short.txt')

for line in doc:
    print(line.upper().rstrip())

doc.close()
