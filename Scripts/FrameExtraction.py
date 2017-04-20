from PIL import ImageGrab
import numpy as np


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
