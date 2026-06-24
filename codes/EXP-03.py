import cv2
import numpy as np

kernel = np.ones((25, 25), np.uint8)

img = cv2.imread(r"C:\Users\BHARATH\Downloads\sample.jpg")

if img is None:
    print("Error: Image not found. Check the file path.")
else:
    cv2.imshow("Original Image", img)
    cv2.waitKey(0)

    img = cv2.resize(img, (500, 500))
    cv2.imshow("Resized Image", img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()