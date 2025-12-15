import cv2
cap = cv2.VideoCapture("videoplayback.mp4")
speed = input("Enter speed (normal/slow/fast): ")
if speed == "normal":
    delay = 25
elif speed == "slow":
    delay = 100
elif speed == "fast":
    delay = 1
else:
    delay = 25
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video Playback", frame)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
