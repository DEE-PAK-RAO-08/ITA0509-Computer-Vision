import cv2
import numpy as np
img = cv2.imread("06.jpg")      
if img is None:
    print("Original image not found!")
    exit()
wm = cv2.imread("es.png", cv2.IMREAD_UNCHANGED)  
if wm is None:
    print("Watermark image not found!")
    exit()
h_img, w_img = img.shape[:2]
scale = 0.2
new_w = int(w_img * scale)
wm = cv2.resize(wm, (new_w, int(wm.shape[0] * new_w / wm.shape[1])))
if wm.shape[2] == 4:
    wm_bgr = wm[:, :, :3]
    alpha = wm[:, :, 3] / 255.0
else:
    wm_bgr = wm
    alpha = np.ones(wm_bgr.shape[:2], dtype=float)
h_wm, w_wm = wm_bgr.shape[:2]
x = w_img - w_wm - 10   
y = h_img - h_wm - 10   
roi = img[y:y+h_wm, x:x+w_wm]
for c in range(3):  
    roi[:, :, c] = (alpha * wm_bgr[:, :, c] + (1 - alpha) * roi[:, :, c])
img[y:y+h_wm, x:x+w_wm] = roi
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("watermarked_output.jpg", img)
