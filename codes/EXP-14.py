import cv2
import numpy as np

img1=cv2.imread(r"C:\Users\BHARATH\Downloads\OIP (2).jpg")

img2=cv2.imread(r"C:\Users\BHARATH\Downloads\OIP (1).jpg")

if img1 is None or img2 is None:
 print("Imagenotfound")
 exit()

img1=cv2.resize(img1,(800,800))

img2=cv2.resize(img2,(800,800))

pts1=np.array([[50,50],[200,50],[50,200],[200,200]],dtype=np.float32)

pts2=np.array([[100,100],[300,100],[100,300],[300,300]],dtype=np.float32)

H,status=cv2.findHomography(pts1,pts2)

dst=cv2.warpPerspective(img1,H,(img2.shape[1],img2.shape[0]))

cv2.imshow("img1",img1)

cv2.imshow("img2",img2)

cv2.imshow("dst",dst)

cv2.waitKey(0)

cv2.destroyAllWindows()
