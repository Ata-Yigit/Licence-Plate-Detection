import cv2 as cv
import numpy as np
import easyocr

img = cv.imread("C:/Users/user/Downloads/plakaa.jpg")
img = cv.resize(img,(img.shape[1]*2,img.shape[0]*2))
gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cascade = cv.CascadeClassifier('C:/Users/user/Downloads/haarcascade_russian_plate_number.xml')
plates = cascade.detectMultiScale(gray, 1.2, 5)
print('Number of detected license plates:', len(plates))
for (x, y, w, h) in plates:
    new_img = img[y:y+h,x:x+w]
    new_img = cv.resize(new_img,(new_img.shape[1]*4,new_img.shape[0]*4))
gray = cv.cvtColor(new_img , cv.COLOR_BGR2GRAY)
thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
reader = easyocr.Reader(['en'])
result = reader.readtext(thresh)
plate = ""
for r in result:
    plate += r[1]
    plate +=" "
print(plate)
cv.imshow("Plate",thresh)
cv.waitKey(0)
cv.destroyAllWindows()
