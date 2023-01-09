import cv2
import numpy as np

a=5
print(a)
img=cv2.imread("C:/Users/Admin/Pictures/family.png")

cv2.imshow("Output",img)
cv2.waitKey(0)  

img=cv2.imread("C:/Users/Admin/Pictures/family.png")

imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imggray,(7,7),1)
cv2.imshow("Gray Image",imggray)
# cv2.waitKey(0)
cv2.imshow("Blur Image",imgBlur)
# cv2.waitKey(0)
imgCanny=cv2.Canny(img,200,200)
cv2.imshow("Canny Image",imgCanny)
# cv2.waitKey(0)

kernal=np.ones((150,150),np.uint8)
imgDialation=cv2.dilate(imgCanny,kernal,iterations=5)
cv2.imshow("Dilation Image",imgCanny)
# cv2.waitKey(0)
imgEroded=cv2.erode(imgDialation,kernal,iterations=5)
cv2.imshow("Eroded Image",imgCanny)
# cv2.waitKey(0)
print(img.shape)
imgResize=cv2.resize(img, (300,200))
cv2.imshow("Resized Image",imgResize)
# cv2.waitKey(0)
print(imgResize.shape)
imgCropped=img[0:200,100:]
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)
cv2.destroyAllWindows()




