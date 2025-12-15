import cv2
img = cv2.imread("1280.jpg")
if img is None:
    print("Image not found!")
    exit()
small = cv2.resize(img, None, fx=0.5, fy=0.5)
large = cv2.resize(img, None, fx=2.0, fy=2.0)
cv2.imshow("Original Image", img)
cv2.imshow("Smaller Image (50%)", small)
cv2.imshow("Larger Image (200%)", large)
cv2.waitKey(0)
cv2.destroyAllWindows()
