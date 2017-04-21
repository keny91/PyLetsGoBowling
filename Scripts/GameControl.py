import pyautogui
import numpy as np
import time


def WaitLoop(numLoops=4, waitTimeperLoop=1):
    for i in list(range(numLoops))[::-1]:
        print(i + 1)
        time.sleep(waitTimeperLoop)


## Press a key outside this environment -> NOT COMPATIBLE WITH THE DIRECTX inputs
def SetKeyDown(theKey):
    print('Key is down: {}'.format(theKey))
    pyautogui.keyDown(theKey)
