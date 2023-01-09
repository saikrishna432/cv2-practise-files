import cv2
import numpy as np

width,height=250,350

img=cv2.imread("C:/Users/Admin/Pictures/four_kings.jpg")
pts1=np.float32([[810,72],[1202,213],[600,657],[984,802]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1, pts2)
imgOutput=cv2.warpPerspective(img, matrix, (width,height))

# cv2.imshow("image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)



