import cv2
import numpy as np
img = cv2.imread("pc.jpg")   
if img is None:
    print("Image not found!")
    exit()
img_small = cv2.resize(img, None, fx=0.3, fy=0.3)
kernel = np.ones((5, 5), np.uint8)   
dilated = cv2.dilate(img_small, kernel, iterations=1)
cv2.imshow("Original (Small)", img_small)
cv2.imshow("Dilated Image", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
