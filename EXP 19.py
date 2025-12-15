import cv2
import numpy as np
img = cv2.imread("oto.jpeg")  
if img is None:
    print("Image not found!")
    exit()
img_small = cv2.resize(img, None, fx=0.5, fy=0.5)
gray = cv2.cvtColor(img_small, cv2.COLOR_BGR2GRAY)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
sobel_final = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
cv2.imshow("Original (Small)", img_small)
cv2.imshow("Sobel X", sobel_x)
cv2.imshow("Sobel Y", sobel_y)
cv2.imshow("Sobel Combined", sobel_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
