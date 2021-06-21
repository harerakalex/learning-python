from PIL import Image
from IPython.display import display
import pytesseract

image = Image.open("../assests/Noisy_OCR.png")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(image)
print(text)

# Gray Image to get text
gray_scale_img = image.convert("L")

gray_scale_img.save("../assests/gray_scale_noise.png")
text = pytesseract.image_to_string(Image.open("../assests/gray_scale_noise.png"))
print(text)

# Black and white image just use one in the convert function as string, it will do the magic
b_w_img = image.convert("1")

gray_scale_img.save("../assests/black_and_white.png")
text = pytesseract.image_to_string(Image.open("../assests/black_and_white.png"))
print(text)

# Using custom function to make black and white threshold
def binalize(image_to_transform, threshold):
    output_image = image_to_transform.convert("L")
    width, height = output_image.size
    for x in range(width):
        for y in range(height):
            if output_image.getpixel((x, y)) < threshold:
                output_image.putpixel((x,y), 0)
            else:
                output_image.putpixel((x,y), 255)
    
    return output_image

for t in range(0, 257, 64):
    print("treshold====", t)
    #display(binalize(image, t))
    print(pytesseract.image_to_string(binalize(image, t))) 