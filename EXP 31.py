import cv2
img = cv2.imread("62.webp")  
if img is None:
    print("Image not found!")
    exit()
img_small = cv2.resize(img, None, fx=0.4, fy=0.4)
gray = cv2.cvtColor(img_small, cv2.COLOR_BGR2GRAY)
thresh_val = 120
_, segmented = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)
cv2.imshow("Original (Small)", img_small)
cv2.imshow(f"Segmented (Threshold = {thresh_val})", segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()
