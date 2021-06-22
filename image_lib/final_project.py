import zipfile

from PIL import Image, ImageDraw
import pytesseract
import cv2 as cv
import numpy as np
from IPython.display import display

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!

# Open zip file and add all images
images = []
with zipfile.ZipFile('readonly/small_img.zip') as myzip:
    for i in range(len(myzip.infolist())):
        myzip.extract(myzip.infolist()[i].filename)
        images.append(myzip.infolist()[i].filename)

# Functions for detecting faces and msking contact sheet

thumb_size = (128, 128)


def show_faces(fname):
    cv_image = cv.imread(fname)
    pil_img = Image.open(fname)
    cv_image_gray = cv.cvtColor(cv_image, cv.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(cv_image_gray, 1.35) #last scalefactor 1.35
    
    face_list = []
    for x,y,w,h in faces:
        cropped = pil_img.crop((x, y, x + w, y + h))
        cropped.thumbnail(thumb_size)
        face_list.append(cropped)

    return face_list


def make_contact_sheet(face_list):

    w_each, h_each = thumb_size

    w_sheet = w_each * 5
    h_sheet = h_each * (len(face_list) // 5)
    if(len(face_list) % 5 != 0):
        h_sheet += h_each
    
    sheet = Image.new(face_list[0].mode, (w_sheet, h_sheet))
    
    x = 0
    y = 0
    
    for face in face_list:
        sheet.paste(face, (x, y) )
        
        if x + w_each == sheet.width:
            x = 0
            y += h_each
        else:
            x += w_each
    
    return sheet

def get_text(image):
    img = Image.open(image).convert('L')
    text = pytesseract.image_to_string(img)
    return text.lower()

def format_fdict(image):
    fdict_large_images = {}
    fdict_large_images['name'] = image
    fdict_large_images['img'] = Image.open(image)
    fdict_large_images['text'] = get_text(image)
    fdict_large_images['faces'] = show_faces(image)
    return fdict_large_images

# Use list comprehension
wrapper_all_contents = [format_fdict(image) for image in images]

# Search function
def search(name):
    for file in wrapper_all_contents:
        if name.lower() in file['text']:

            print("Results found in file " + file['name'])

            if len(file['faces']) == 0:
                print("But there were no faces in that file!")

            else:
                display(make_contact_sheet(file['faces']))

search('Christopher')