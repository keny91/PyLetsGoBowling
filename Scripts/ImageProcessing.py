import numpy as np
import cv2


def ExtractCannyEdges(theImage, th1=200, th2=300):
    outputImage = cv2.cvtColor(theImage, cv2.COLOR_BGR2GRAY)
    outputImage = cv2.Canny(outputImage, th1, th2)
    return outputImage


def SobelFilterX(theImage, thesize=5):
    # sobelx = cv2.Sobel(theImage, cv2.CV_64F, 1, 0, ksize=thesize)
    sobelx = cv2.Sobel(theImage, cv2.CV_8U, 1, 0, ksize=thesize)
    # is this necessary?
    abs_sobelx = np.absolute(sobelx)
    outputImage = cv2.cvtColor(abs_sobelx, cv2.COLOR_BGR2GRAY)
    return outputImage


def DrawLines(image, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(image, (coords[0], coords[1]), (coords[2], coords[3]), [255, 255, 255], 3)

    except:
        pass

