import cv2
import matplotlib.pyplot as plt
def show_color_histogram(path):
    img = cv2.imread(path)
    b, g, r = cv2.split(img)
    plt.plot(cv2.calcHist([b], [0], None, [256], [0,256]), color='b')
    plt.plot(cv2.calcHist([g], [0], None, [256], [0,256]), color='g')
    plt.plot(cv2.calcHist([r], [0], None, [256], [0,256]), color='r')
    plt.title("RGB Histogram")
    plt.xlabel("Intensity")
    plt.ylabel("Pixel Count")
    plt.show()
show_color_histogram("sample.jpg")
