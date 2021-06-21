import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from IPython.display import display

image = Image.open("readonly/msi_recruitment.gif")
image = image.convert('RGB')

intensity = [0.1, 0.5, 0.9]

def draw_text(channel, inten_index, image):
    font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 50)
    draw = ImageDraw.Draw(image)
    msg = "channel {}, intensity {}".format(channel, intensity[inten_index])
    draw.text((0,0), msg, font = font, color="white")

def format_each_band_image(channel, inten_index, band_image):
    colors = [0,1,2]
    colors.pop(channel)
    if channel == 0:
        bands = (band_image[channel].point(lambda x:x*intensity[inten_index]), band_image[colors[0]], band_image[colors[1]])
    elif channel == 1:
        bands = (band_image[colors[0]], band_image[channel].point(lambda x:x*intensity[inten_index]), band_image[colors[1]])
    else:
        bands = (band_image[colors[0]], band_image[colors[1]], band_image[channel].point(lambda x:x*intensity[inten_index]))
    # paste an image onto another one
    return Image.merge("RGB", bands)
    
def handle_image(channel, inten_index):
    text_wrapper = Image.new("RGB", (image.width, 50), color="black")
    draw_text(channel, inten_index, text_wrapper)
    new_image = Image.new("RGB", (image.width, image.height + 50)) # added 50 bcs text_wrapper height is 50
    new_image.paste(image, (0,0))
    # Add text wrapper image
    new_image.paste(text_wrapper, (0, image.height))
    return format_each_band_image(channel, inten_index, new_image.split())

images = [handle_image(channel, inten_index) for channel in [0,1,2] for inten_index in [0,1,2]]
first_image = images[0]

contact_sheet = Image.new(first_image.mode, (first_image.width*3, first_image.height*3))
x=0
y=0

for img in images:
    contact_sheet.paste(img, (x, y) )
    if x + first_image.width == contact_sheet.width:
        x = 0
        y = y + first_image.height
    else:
        x = x + first_image.width
        

contact_sheet = contact_sheet.resize((int(contact_sheet.width/2), int(contact_sheet.height/2) ))
display(contact_sheet)