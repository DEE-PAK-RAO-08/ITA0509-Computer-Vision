import cv2

# Use raw string (r"...") to avoid path errors
image_path = r"C:\Users\LENOVO\Documents\C Vison\sample.jpg"

image = cv2.imread(image_path)

# Check if image loaded
if image is None:
    print("Image not found! Check the path.")
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
