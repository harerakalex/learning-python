from PIL import Image
from IPython.display import display
import pytesseract

image = Image.open("../assests/text.png")
#image.show()
#text = pytesseract.image_to_string(image)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(image, config='--psm 11')
print(text)
