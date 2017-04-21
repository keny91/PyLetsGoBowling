import pyautogui
import numpy as np
import time


def WaitLoop(numLoops=4, waitTimeperLoop=1):
    for i in list(range(numLoops))[::-1]:
        print(i + 1)
        time.sleep(waitTimeperLoop)


def SetKeyDown(theKey):
    print('Key is down: {}'.format(theKey))
    pyautogui.keyDown(theKey)
