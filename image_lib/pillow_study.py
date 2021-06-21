from PIL import Image
from PIL import ImageDraw
from IPython.display import display

image = Image.open("../assests/carlos.jpeg")

print(image.format, image.size, image.mode)
print("{}x{}".format(image.width, image.height))

# Original Image
image.show()

# Draw on the image
drawing_object=ImageDraw.Draw(image)
drawing_object.rectangle((180, 145, 625, 695), fill=None, outline = "red")
image.show()

# Crop the drawn Image
image = image.crop((180, 145, 625, 695))
image.show()
# display(image)
# display(image.crop((185, 150, 625, 690)))