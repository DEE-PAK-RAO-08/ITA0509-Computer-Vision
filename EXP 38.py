import cv2
def count_faces(image_path):
    # Load Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found!")
        return 0
    img_small = cv2.resize(img, None, fx=0.2, fy=0.2)
    gray = cv2.cvtColor(img_small, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img_small, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("Faces Detected", img_small)
    print("Number of faces detected:", len(faces))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return len(faces)
count_faces("88.jpg")   
