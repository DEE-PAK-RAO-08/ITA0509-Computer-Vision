import cv2
import numpy as np
def subtract_background_by_color(img, lower_hsv, upper_hsv):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    bg_mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    fg_mask = cv2.bitwise_not(bg_mask)
    result = cv2.bitwise_and(img, img, mask=fg_mask)
    return result
img = cv2.imread("images (1).jpg")  
if img is None:
    print("Image not found!")
    exit()
lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])
output = subtract_background_by_color(img, lower_green, upper_green)
img_small = cv2.resize(img, None, fx=2, fy=2)
out_small = cv2.resize(output, None, fx=2, fy=2)
cv2.imshow("Original", img_small)
cv2.imshow("Background Removed", out_small)
cv2.waitKey(0)
cv2.destroyAllWindows()
