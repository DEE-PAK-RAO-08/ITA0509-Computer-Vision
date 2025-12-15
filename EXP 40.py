import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def extract_text_from_video(video_path, frame_step=30):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video!")
        return ""
    all_text = []
    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_idx % frame_step == 0:
            frame_small = cv2.resize(frame, None, fx=0.5, fy=0.5)
            gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            if text.strip():
                print(f"--- Frame {frame_idx} ---")
                print(text)
                all_text.append(text)
        frame_idx += 1
    cap.release()
    return "\n".join(all_text)
text = extract_text_from_video("back.mp4", frame_step=30)
print("\n==== FINAL TEXT FROM VIDEO ====\n")
print(text)
