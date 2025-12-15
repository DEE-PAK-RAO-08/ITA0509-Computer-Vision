import cv2
car_cascade = cv2.CascadeClassifier("cars.xml")  
if car_cascade.empty():
    print("Error: Could not load cascade file!")
    exit()
cap = cv2.VideoCapture("small.mp4")  
if not cap.isOpened():
    print("Error: Could not open video!")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_small = cv2.resize(frame, None, fx=0.6, fy=0.6)
    gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame_small, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("Vehicle Detection", frame_small)
    if cv2.waitKey(20) & 0xFF == 27:  
        break
cap.release()
cv2.destroyAllWindows()
