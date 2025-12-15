import cv2
import numpy as np
img = cv2.imread("mx.webp")  
if img is None:
    print("Image not found!")
    exit()
img_small = cv2.resize(img, None, fx=0.5, fy=0.5)
kernel = np.ones((5, 5), np.uint8)  
opened = cv2.morphologyEx(img_small, cv2.MORPH_OPEN, kernel)
cv2.imshow("Original (Small)", img_small)
cv2.imshow("Opening Result", opened)
cv2.waitKey(0)
cv2.destroyAllWindows()
