import cv2
import numpy as np
w = int(input("Enter image width: "))
h = int(input("Enter image height: "))
img = np.ones((h, w, 3), dtype=np.uint8) * 255
center = (w // 2, h // 2)         
radius = min(w, h) // 4           
cv2.circle(img, center, radius, (0, 0, 255), 3)  
cv2.imshow("Circle on White Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
