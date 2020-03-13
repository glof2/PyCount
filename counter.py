from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


def sendkeys(number):
    for num in str(number):
        keyboard.press(num)
        keyboard.release(num)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


number = int(input("Input the current number: ")) + 1
delay = int(input("Input the delay: "))
howmanynumbers = int(input("Input how long: "))
time.sleep(2)
while howmanynumbers:
    sendkeys(number)
    number += 1
    howmanynumbers -= 1
    time.sleep(delay)
