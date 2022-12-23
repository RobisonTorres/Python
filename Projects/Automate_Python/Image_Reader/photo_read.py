from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

with open('Info.jpg', 'rb') as file:
    image = pytesseract.image_to_string(Image.open(file))

print(image)
