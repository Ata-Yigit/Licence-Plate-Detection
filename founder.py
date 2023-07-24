import cv2 as cv
import numpy as np
import easyocr

img = cv.imread("C:/Users/user/Downloads/plaka5.jpeg")
img = cv.resize(img,(1200,1200))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
filtered = cv.bilateralFilter(gray,5,60,20)
edges = cv.Canny(filtered,60,200)
contours,_ = cv.findContours(edges.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
mask = np.zeros(gray.shape, np.uint8)
for cnt in contours:
    approx = cv.approxPolyDP(cnt,20, True)
    if len(approx) == 4 and cv.contourArea(cnt)>3000:
        new_img = cv.drawContours(mask, [approx],0,255, -1)
        new_img = cv.bitwise_and(gray, gray,mask=mask)

(x,y) = np.where(mask==255)
(x1,y1) = (np.min(x),np.min(y))
(x2,y2) = (np.max(x),np.max(y))
new_img = new_img[x1:x2,y1:y2]
new_img = cv.resize(new_img,(new_img.shape[1]*2,new_img.shape[0]*2))

reader = easyocr.Reader(['en'])
result = reader.readtext(new_img)
plate = ""
for r in result:
    plate += r[1]
    plate +=" "
print(plate)
cv.imshow("Plate",new_img)
cv.waitKey(0)
cv.destroyAllWindows()
