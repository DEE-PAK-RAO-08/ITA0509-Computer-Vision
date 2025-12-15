import cv2
import numpy as np
img = cv2.imread("a3.jpg")
if img is None:
    print("Image not found!")
    exit()
rows, cols, ch = img.shape
pts1 = np.float32([[0, 0],
                   [cols - 1, 0],
                   [0, rows - 1]])
pts2 = np.float32([[0, 0],
                   [int(0.8 * (cols - 1)), int(0.2 * rows)],
                   [int(0.2 * cols), int(0.9 * (rows - 1))]])
M = cv2.getAffineTransform(pts1, pts2)
affine_img = cv2.warpAffine(img, M, (cols, rows))
img_small = cv2.resize(img, None, fx=0.5, fy=0.5)
affine_small = cv2.resize(affine_img, None, fx=0.5, fy=0.5)
cv2.imshow("Original Image (Small)", img_small)
cv2.imshow("Affine Transformed Image (Small)", affine_small)
cv2.waitKey(0)
cv2.destroyAllWindows()


