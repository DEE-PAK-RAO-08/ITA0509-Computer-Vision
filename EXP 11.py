import cv2
img = cv2.imread("Wall.jpg")
if img is None:
    print("Image not found!")
    exit()
rotated = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow("Original Image", img)
cv2.imshow("Rotated 180 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
