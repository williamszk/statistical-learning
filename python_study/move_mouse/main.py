import pyautogui
import time
import random


def main():
    while True:
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        pyautogui.moveTo(x, y)

        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print(f"Moved at {result} ({x}, {y})")
        time.sleep(60)


if __name__ == "__main__":
    main()
