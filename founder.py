import cv2 as cv

img = cv.imread("C:/Users/user/Downloads/plaka4.jpg")
img = cv.resize(img,(1600,900))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
filtered = cv.bilateralFilter(gray,20,60,20)
edges = cv.Canny(filtered,60,200)
contours,_ = cv.findContours(edges.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    approx = cv.approxPolyDP(cnt,20, True)
    if len(approx) == 4 and cv.contourArea(cnt)>3000:
        img = cv.drawContours(img, [approx], -1, (0,255,0), 3)
cv.imshow("Plate",img)
cv.waitKey(0)
cv.destroyAllWindows()