import cv2
import numpy as np
img = cv2.imread("Rebel.jpg")
if img is None:
    print("Image not found!")
    exit()
kernel = np.ones((3, 3), np.uint8)
dilated = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
