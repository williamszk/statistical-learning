"""In the gap effect the objective is to learn something faster
by at random an alarm goes off and I need to stop everything and 
keep my eyes closed and wait for 10 seconds.
"""

import time
import random
import chime


def main():
    chime.theme("mario")
    while True:
        time.sleep(1)
        print("waiting...")
        if random.random() > 0.8:
            chime.info()
            time.sleep(10)
            chime.info()
            time.sleep(0.2)
            chime.info()


if __name__ == "__main__":
    main()
