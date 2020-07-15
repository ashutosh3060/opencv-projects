# coding: utf-8

# Install Libraries
! pip install Pillow
! pip install pytesseract

# Import Libraries
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # reading tesseract file from the installed path

# load test images
im_1 = Image.open("motiv_quote.png")
im_2 = Image.open("i_can_read.png")
text_1 = pytesseract.image_to_string(im_1, lang="eng")
text_2 = pytesseract.image_to_string(im_2, lang="eng")

# print the text from the test images
print(text_1)
print(text_2)
