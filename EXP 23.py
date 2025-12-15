import cv2
import numpy as np
img = cv2.imread("1.jpg")   
if img is None:
    print("Image not found!")
    exit()
img_small = cv2.resize(img, None, fx=2, fy=2)
kernel = np.ones((5, 5), np.uint8)   
tophat = cv2.morphologyEx(img_small, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Original (Small)", img_small)
cv2.imshow("Top-Hat Result", tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
