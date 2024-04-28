import threading
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode
import numpy as np
import cv2
import time
from PIL import ImageGrab

click = False
running = True
mouse = MouseController()
ToggleKey = KeyCode(char='q')
ExitKey = KeyCode(char='e')

#def GoldenCookie():
#    while running:
#        screenshot = np.array(ImageGrab.grab())
#        objectImage = cv2.imread('GoldenCookie.png')
#
#        result = cv2.matchTemplate(screenshot, objectImage, cv2.TM_CCOEFF_NORMED)
#        threshold = 0.8
#        locations = np.where(result >= threshold)
#
#        for point in zip(*locations[::-1]):
#            mouse.position = point
#            mouse.click(Button.left, 1)

def Clicker():
    loopTime = time.time()

    while running:
        if click:
            mouse.position = (387, 566)
            mouse.click(Button.left, 1)

        cv2.waitKey(1)
        currentTime = time.time()
        fps = 1 / (currentTime - loopTime + 1e-6)
        print(f'FPS: {fps:.2f}')
        loopTime = currentTime


def ToggleEvent(key):
    global click, running
    if key == ToggleKey:
        click = not click
    elif key == ExitKey:
        running = False


clickingThread = threading.Thread(target=Clicker)
clickingThread.start()
#goldenCookieThread = threading.Thread(target=GoldenCookie)
#goldenCookieThread.start()
listener = Listener(on_press=ToggleEvent)
listener.start()
listener.join()
clickingThread.join()
#goldenCookieThread.join()