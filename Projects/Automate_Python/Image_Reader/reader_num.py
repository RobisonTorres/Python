import re
import pytesseract
from PIL import Image
print('Reading Images.')
print()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_nums():

    # This function reads and return numbers from image.
    file = input('Type in the file\'s name: ')
    image = Image.open(file)

    #Remove all non-number characters.
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
    numbers_string = pytesseract.image_to_string(image, config=custom_config)
    numbers_int = re.sub(r'[a-z\n\s]', '', numbers_string.lower())
    
    print('\nAccuracy depends on the photo\'s quality.')
    return numbers_int

print(read_nums())
