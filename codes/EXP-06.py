import cv2
image=cv2.imread(r"C:\Users\BHARATH\Downloads\ironman-hd-kbv6pf978cawvv0r.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,threshold1=30,threshold2=100)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
