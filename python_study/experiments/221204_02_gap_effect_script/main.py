"""In the gap effect the objective is to learn something faster
by at random an alarm goes off and I need to stop everything and 
keep my eyes closed and wait for 10 seconds.
"""

import time
import random


def main():
    while True:
        time.sleep(1)
        print("waiting...")
        if random.random() > 0.8:
            print("\a")  # this will send a bell sound to stdout
            print("\a")
            time.sleep(10)
            print("\a")


if __name__ == "__main__":
    main()
