from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# image_path = r'C:\Users\user\Python\Info.jpg'

with open("Info.jpg", 'rb') as file:
    text = pytesseract.image_to_string(Image.open(file))

print(text)
