import cv2
import numpy as np
image =cv2.imread(r"C:\Users\BHARATH\Downloads\ironman-hd-kbv6pf978cawvv0r.jpg")
kernel=np.ones((5,5),np.uint8)
erode_image=cv2.erode(image,kernel,iterations=1)
cv2.imshow('original image',image)
cv2.imshow('erode image', erode_image)
cv2.waitKey(0)
cv2.destroyAllWindows()