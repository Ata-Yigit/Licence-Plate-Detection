import cv2 as cv
import numpy as np
import easyocr

img = cv.imread("C:/Users/user/Downloads/plaka3.jpg")
img = cv.resize(img,(1600,900))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
filtered = cv.bilateralFilter(gray,20,60,20)
edges = cv.Canny(filtered,60,200)
contours,_ = cv.findContours(edges.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
mask = np.zeros(gray.shape, np.uint8)
for cnt in contours:
    approx = cv.approxPolyDP(cnt,20, True)
    if len(approx) == 4 and cv.contourArea(cnt)>3000:
        x,y,z,w = approx
        new_img = cv.drawContours(mask, [approx],0,255, -1)
        new_img = cv.bitwise_and(gray, gray,mask=mask)
reader = easyocr.Reader(['en'])
result = reader.readtext(new_img)
for r in result:
    print(r[1])
cv.imshow("Plate",new_img)
cv.waitKey(0)
cv.destroyAllWindows()
