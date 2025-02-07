import pytesseract
from pytesseract import Output
from PIL import Image
import cv2 as cv
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR/tesseract.exe"
lang=pytesseract.get_languages()
print(lang)

image = cv.imread("persian-standard-font.jpg", 0)
image_rgb = cv.imread("persian-standard-font.jpg")

#img_blur = cv.medianBlur(image,3)
#_,img_thresh = cv.threshold(img_blur, 50, 255, cv.THRESH_BINARY)

cv.imshow('image1',image)

#تشخیص متن
img_text = pytesseract.image_to_string(image,lang='fas')
print(img_text)

#تشخیص حرف به حرف

text_boxes = pytesseract.image_to_boxes(image)
print(text_boxes)

text_boxes_list = text_boxes.split('\n')

image_rgb = cv.imread("persian-standard-font.jpg")
w,h,c = image_rgb.shape
for box_coords in text_boxes_list:
    box_coords = box_coords.split(' ')
    if box_coords[0]:
        print(box_coords)
        x1 = int(box_coords[1])
        y1 = int(box_coords[2])
        x2 = int(box_coords[3])
        y2 = int(box_coords[4])
        cv.rectangle(image_rgb, (x1,w-y1), (x2,w-y2), (0,0,255), 2)
cv.imshow('img-rgb',image_rgb)

#تشخیص کلمه به کلمه

img_data = pytesseract.image_to_data(image, output_type=Output.DICT)



image_rgb1 = cv.imread("persian-standard-font.jpg")
w,h,c = image_rgb.shape

for index,text in enumerate(img_data['text']):
    if text:
        x1= int(img_data['left'][index])
        y1= int(img_data['top'][index])
        x2 = x1 + int(img_data['width'][index])
        y2 = y1 + int(img_data['height'][index])
        cv.rectangle(image_rgb1, (x1, y1), (x2, y2), (255,0,0), 2)

cv.imshow('image_rgb1',image_rgb1)



cv.waitKey(0)
cv.destroyAllWindows()