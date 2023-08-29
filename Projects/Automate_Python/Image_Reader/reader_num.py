import re
import cv2
import pytesseract
from PIL import Image
print('Reading Images.')
print()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_nums():

    # This function reads and return numbers from image.
    file = input('Type in the file\'s name: ')
    image = Image.open(file)
    # image = cv2.imread(file, 0)
    # thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
    numbers_string = pytesseract.image_to_string(image, config=custom_config)
    #numbers_string = pytesseract.image_to_string(thresh, config=custom_config)

    #Remove all non-number characters.
    numbers_int = re.sub(r'[a-z\n]', '', numbers_string.lower())
    print('\nAccuracy depends on the photo\'s quality.')
    return numbers_int

print(read_nums())
