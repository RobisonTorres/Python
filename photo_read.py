import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"/home/robisontorres/.local/bin"

with open('a-fistful-of-dollars-clint-eastwood-man-with-no-name-mules-wallpaper-preview.jpg', 'rb') as file:
    image = pytesseract.image_to_string(Image.open(file))

print(image)
