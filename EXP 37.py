import cv2
import numpy as np
def subtract_foreground_by_color(img, lower_hsv, upper_hsv):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    fg_mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    bg_mask = cv2.bitwise_not(fg_mask)
    result = cv2.bitwise_and(img, img, mask=bg_mask)
    return result
img = cv2.imread("images (2).jpg")   
if img is None:
    print("Image not found!")
    exit()
lower_fg = np.array([35, 40, 40])     
upper_fg = np.array([85, 255, 255])   
output = subtract_foreground_by_color(img, lower_fg, upper_fg)
img_small    = cv2.resize(img,    None, fx=2, fy=2)
output_small = cv2.resize(output, None, fx=2, fy=2)
cv2.imshow("Original (Small)", img_small)
cv2.imshow("Foreground Removed (Small)", output_small)
cv2.waitKey(0)
cv2.destroyAllWindows()
