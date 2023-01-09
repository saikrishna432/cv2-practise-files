
import cv2
import numpy as np



## Vedios work
cap=cv2.VideoCapture(0)
cap.set(10,15)
#cap=cv2.VideoCapture("C:/Users/Admin/Desktop/upendar projects/object detection/data/Cars_On_Highway.mp4")


while True:
    success, img2=cap.read()
    #print(success)
    cv2.imshow("Vedio",img2)
    #cv2.waitKey(10)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#cv2.destroyAllWindows()
#cap.release()