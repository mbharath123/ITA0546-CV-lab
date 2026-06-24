import cv2
import numpy as np

im_src=cv2.imread(r"C:\Users\BHARATH\Downloads\OIP.jpg")

im_dst=cv2.imread(r"C:\Users\BHARATH\Downloads\4200559.jpg")

if im_src is None or im_dst is None:
 print("Imagenotfound")
 exit()

im_src=cv2.resize(im_src,(800,800))

im_dst=cv2.resize(im_dst,(800,800))

pts_src=np.float32([[0,0],[799,0],[799,799],[0,799]])

pts_dst=np.float32([[150,100],[650,150],[600,700],[100,650]])

h,status=cv2.findHomography(pts_src,pts_dst)

im_out=cv2.warpPerspective(im_src,h,(800,800))

cv2.imshow("SourceImage",im_src)

cv2.imshow("DestinationImage",im_dst)

cv2.imshow("WarpedSourceImage",im_out)

cv2.waitKey(0)

cv2.destroyAllWindows()
