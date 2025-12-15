import cv2
import numpy as np
w = int(input("Enter image width: "))
h = int(input("Enter image height: "))
img = np.ones((h, w, 3), dtype=np.uint8) * 255
cv2.rectangle(img, (50, 50), (w-50, h-50), (255, 0, 0), 3)  
cv2.imshow("Rectangle on White Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
