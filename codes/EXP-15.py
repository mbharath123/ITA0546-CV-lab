import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\BHARATH\Downloads\OIP (1).jpg")

# Source points (corners in original image)
src_pts = np.float32([
    [100, 100],
    [400, 100],
    [100, 400],
    [400, 400]
])

# Destination points
dst_pts = np.float32([
    [0, 0],
    [300, 0],
    [0, 300],
    [300, 300]
])

# Compute transformation matrix using DLT
H = cv2.getPerspectiveTransform(src_pts, dst_pts)

# Apply perspective transformation
transformed = cv2.warpPerspective(img, H, (300, 300))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Transformed Image", transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()