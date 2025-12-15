import cv2
import numpy as np
img = cv2.imread("07.jpg")   
if img is None:
    print("Image not found!")
    exit()
rows, cols, ch = img.shape
pts1 = np.float32([[50, 50],
                   [cols - 50, 50],
                   [50, rows - 50],
                   [cols - 50, rows - 50]])
pts2 = np.float32([[0, 0],
                   [cols - 1, 0],
                   [0, rows - 1],
                   [cols - 1, rows - 1]])
M = cv2.getPerspectiveTransform(pts1, pts2)
persp = cv2.warpPerspective(img, M, (cols, rows))
img_small   = cv2.resize(img,   None, fx=0.5, fy=0.5)
persp_small = cv2.resize(persp, None, fx=0.5, fy=0.5)
cv2.imshow("Original Image (Small)", img_small)
cv2.imshow("Perspective Transformed (Small)", persp_small)
cv2.waitKey(0)
cv2.destroyAllWindows()
