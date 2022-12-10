print('Test from SoloLearn')
print()

book = open('22 - book.txt', 'r')

list_books = book.readlines()

for item in list_books:
    if not item == list_books[-1]:
        print(item[0] + str(len(item)-1))
    else:
        print(item[0] + str(len(item)))

book.close()
