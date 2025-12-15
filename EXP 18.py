import cv2
import numpy as np
img = cv2.imread("95.jpg")  
if img is None:
    print("Image not found!")
    exit()
img_small = cv2.resize(img, None, fx=0.1, fy=0.1)
gray = cv2.cvtColor(img_small, cv2.COLOR_BGR2GRAY)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)
sobel_combined = cv2.addWeighted(sobelx, 0.1, sobely, 0.1, 0)
cv2.imshow("Original (Small)", img_small)
cv2.imshow("Sobel X (Small)", sobelx)
cv2.imshow("Sobel Y (Small)", sobely)
cv2.imshow("Sobel Combined (Small)", sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
