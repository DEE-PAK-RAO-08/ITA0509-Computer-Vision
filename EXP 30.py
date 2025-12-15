import cv2
face_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades +
                                      "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                      "haarcascade_smile.xml")
img = cv2.imread("people.png")   
if img is None:
    print("Image not found!")
    exit()
img_small = cv2.resize(img, None, fx=0.6, fy=0.6)
gray = cv2.cvtColor(img_small, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img_small, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray  = gray[y:y+h, x:x+w]
    roi_color = img_small[y:y+h, x:x+w]
    smiles = smile_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.7,
        minNeighbors=22
    )
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
cv2.imshow("Smile Detection", img_small)
cv2.waitKey(0)
cv2.destroyAllWindows()
