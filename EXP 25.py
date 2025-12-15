import cv2
import numpy as np
scene = cv2.imread("10.jpg")       
template = cv2.imread("watch.png") 
if scene is None:
    print("Scene image not found!")
    exit()
if template is None:
    print("Template image not found!")
    exit()
scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template_gray = cv2.resize(template_gray, None, fx=0.4, fy=0.4) 
scene_edges    = cv2.Canny(scene_gray,    50, 150)
template_edges = cv2.Canny(template_gray, 50, 150)
h, w = template_edges.shape[:2]
result = cv2.matchTemplate(scene_edges, template_edges, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print("Best match score:", max_val)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
detected = scene.copy()
cv2.rectangle(detected, top_left, bottom_right, (0, 0, 255), 2)
scene_small    = cv2.resize(scene,    None, fx=2, fy=2)
detected_small = cv2.resize(detected, None, fx=2, fy=2)
cv2.imshow("Original Scene (Small)", scene_small)
cv2.imshow("Watch Detected (Small)", detected_small)
cv2.waitKey(0)
cv2.destroyAllWindows()
