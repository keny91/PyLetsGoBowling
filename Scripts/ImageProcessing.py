import numpy as np
import cv2


def ExtractCannyEdges(theImage, th1=200, th2=300):
    outputImage = cv2.cvtColor(theImage, cv2.COLOR_BGR2GRAY)
    outputImage = cv2.Canny(outputImage, th1, th2)
    return outputImage
