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
TOGGLEKEY = KeyCode(char='s')
EXITKEY = KeyCode(char='q')


def click_golden_cookie():
    while running:
        screenshot = np.array(ImageGrab.grab())
        objectImage = cv2.imread('GoldenCookie.png')

        result = cv2.matchTemplate(screenshot, objectImage, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        locations = np.where(result >= threshold)

        for point in zip(*locations[::-1]):
            mouse.position = point
            mouse.click(Button.left, 1)

def clicker():
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


def toggle_event(key):
    global click, running
    if key == TOGGLEKEY:
        click = not click
    elif key == EXITKEY:
        running = False


clickingThread = threading.Thread(target=clicker)
clickingThread.start()
#goldenCookieThread = threading.Thread(target=GoldenCookie)
#goldenCookieThread.start()
listener = Listener(on_press=toggle_event)
listener.start()
listener.join()
clickingThread.join()
#goldenCookieThread.join()