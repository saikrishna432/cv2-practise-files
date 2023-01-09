import cv2
import numpy as np

print(5)
img=cv2.imread("C:/Users/Admin/Pictures/family.png")
img=cv2.resize(img,(300,250))

imgHor=np.hstack((img,img))
imgVer=np.vstack((img,img))
cv2.imshow("Horizontal stake",imgHor)
cv2.imshow("Vertical stake",imgVer)
cv2.waitKey(0)
cv2.destroyAllWindows()

# For stacking images
# def stakeImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0],list)
#     width = imgArray[0][0].shape[1]
#     height =  imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range(0,rows):
#             for y in range(0,cols):
#                 if imgArray[x][y].shape[:2]==imgArray[0][0].shape[:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y],(0,0),None,        )
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y],imgArray[0][0]     )
#                 if len(imgArray[x][y].shape)==2:
#                     imgArray[x][y]=cv2.cvtColor(----, ----code)
#         imageBlack = np.zeros((height,width,3),np.uint8)
#         hor=[imageBlank]*rows
#         hor_con = [imageBlack]*rows
#         for x in range(0,rows):
#             hor[x]=np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0,rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x]=cv2.resize(imgArray[x],(0,0),None,scale,sca.....)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x],(imgArray[0].shape[1]))
#             if len(imgArray[x].shape)==2:
#                 imgArray[x]=cv2.cvtcolour(imgArray)
#         hor = np.hstack(imgArray)
#         ver = hor
#     return ver


                
                
                
                
                