import cv2
text = input("Enter text to display: ")
img = cv2.imread("20.jpg")   
if img is None:
    print("Image not found!")
    exit()
img_small = cv2.resize(img, None, fx=0.5, fy=0.5)   
pos = (50, 50)
cv2.putText(img_small, text, pos,
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 0, 255), 2)   
cv2.imshow("Image with User Text (Small)", img_small)
cv2.waitKey(0)
cv2.destroyAllWindows()
