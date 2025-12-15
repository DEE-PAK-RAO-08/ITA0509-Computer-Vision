import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                     "haarcascade_frontalface_default.xml")
img = cv2.imread("23.jpg")   
if img is None:
    print("Image not found!")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
img_small = cv2.resize(img, None, fx=2, fy=2)
cv2.imshow("Face Detection", img_small)
cv2.waitKey(0)
cv2.destroyAllWindows()
