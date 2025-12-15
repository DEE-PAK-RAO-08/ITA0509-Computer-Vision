import cv2
cap = cv2.VideoCapture("videoplayback (1).mp4") 
if not cap.isOpened():
    print("Error: Could not open video")
    exit()
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()
if len(frames) == 0:
    print("Error: No frames found in video!")
    exit()
frames = frames[::-1]
h, w = frames[0].shape[:2]
out = cv2.VideoWriter("reverse.mp4",
                      cv2.VideoWriter_fourcc(*"mp4v"),
                      30, (w, h))
for f in frames:
    out.write(f)
out.release()
cap2 = cv2.VideoCapture("reverse.mp4")
while True:
    ret, frame = cap2.read()
    if not ret:
        break
    cv2.imshow("Reversed Video", frame)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cap2.release()
cv2.destroyAllWindows()

