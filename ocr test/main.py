import cv2
import pytesseract
from PIL import Image

img = cv2.imread('ex1.png')
img2 = cv2.imread('bn1.png')
text = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
text2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

#tex1 = pytesseract.image_to_string(text)
#print(tex1)

tex2= pytesseract.image_to_string(text2, lang='ben')
print(tex2)

cv2.imshow('Result', img)
cv2.imshow('Result', img2)
#tex= pytesseract.image_to_string(Image.open('bn1.png'), lang='ben')
cv2.waitKey(0)
