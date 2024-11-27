from pynput.keyboard import Key, Controller
import time

Keyboard = Controller()

t=.99

time.sleep(1)

def prn(x):
    Keyboard.type(x)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)

nickNames = ["-__@__-"]

for y in range(10):
    for x in nickNames:
        prn("You there ??")
        time.sleep(t)
        prn(x)
        time.sleep(t)
        prn(":(")
        time.sleep(t)
        prn(".")
        time.sleep(t)
        prn(".")
        time.sleep(t)
    time.sleep(t)