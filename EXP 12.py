import cv2
img = cv2.imread("a6.jpg")
if img is None:
    print("Image not found!")
    exit()
original_small = cv2.resize(img, None, fx=0.2, fy=0.2)
rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
rotated_small = cv2.resize(rotated, None, fx=0.2, fy=0.2)
cv2.imshow("Original Image (Resized)", original_small)
cv2.imshow("270° Clockwise Rotated (Resized)", rotated_small)
cv2.waitKey(0)
cv2.destroyAllWindows()
