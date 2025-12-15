import numpy as np
import cv2
def create_colored_corners():
    h = int(input("Enter image height: "))
    w = int(input("Enter image width  : "))
    img = 255 * np.ones((h, w, 3), dtype=np.uint8)
    bh, bw = h // 10, w // 10
    img[0:bh, 0:bw] = (0, 0, 0)
    img[0:bh, w-bw:w] = (255, 0, 0)
    img[h-bh:h, 0:bw] = (0, 255, 0)
    img[h-bh:h, w-bw:w] = (0, 0, 255)
    cv2.imshow("Colored Corner Boxes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
create_colored_corners()
