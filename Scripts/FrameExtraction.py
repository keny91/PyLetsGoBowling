from PIL import ImageGrab
import numpy as np
import cv2


def getFrame():
    printScreen_pil = ImageGrab.grab()  # ImageGrab only works for windows. Might need an alternative
    # printScreen_numpy = np.array(printScreen_pil.getdata(), dtype='uint8') \
    # .reshape((printScreen_pil.size[1], printScreen_pil.size[0], 3))
    return np.array(printScreen_pil)


def getFrameFromSquare(bbox=(0, 40, 800, 640)):
    printScreen_pil = ImageGrab.grab(bbox)  # ImageGrab only works for windows. Might need an alternative
    # printScreen_numpy = np.array(printScreen_pil.getdata(), dtype='uint8') \
    #     .reshape((printScreen_pil.size[1], printScreen_pil.size[0], 3))
    return np.array(printScreen_pil)


def MaskRoadROI(image, PolygonPoints):
    # initialize the mask as all 0s as a same size image
    mask = np.zeros_like(image)
    # fill the shape with 1s (255)
    cv2.fillPoly(mask, PolygonPoints, 255)
    # apply mask to the image; do and AND bit operation:
    # 1 & 1 = 1; 1 & 0 = 0; 0 & 0 = 0
    masked = cv2.bitwise_and(image, mask)
    return masked
