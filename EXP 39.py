import cv2
def play_video_reverse_slow(video_path, slow_factor=2):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video!")
        return
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    if len(frames) == 0:
        print("Error: No frames in video!")
        return
    frames = frames[::-1]
    delay = int(40 * slow_factor)  

    for frame in frames:
        cv2.imshow("Reverse Slow Motion", frame)
        if cv2.waitKey(delay) & 0xFF == 27:  
            break
    cv2.destroyAllWindows()
play_video_reverse_slow("small.mp4", slow_factor=3)  
