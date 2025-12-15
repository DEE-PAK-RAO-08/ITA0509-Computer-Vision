import cv2
img = cv2.imread("sample.jpg", 0) 
if img is None:
    print("Error: Image not found. Check filename!")
    exit()
equalized = cv2.equalizeHist(img)
cv2.imshow("Original Image", img)
cv2.imshow("Histogram Equalized Image", equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
