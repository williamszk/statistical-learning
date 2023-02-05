"""In the gap effect the objective is to learn something faster
by at random an alarm goes off and I need to stop everything and 
keep my eyes closed and wait for 10 seconds.
"""

import time
import random
import chime
from datetime import datetime

def main():
    print("Start gap reminder!")
    chime.theme("mario")
    counter = 0
    while True:
        counter += 1
        time.sleep(60)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if random.random() > 0.8:
            chime.info()
            print(f"Gap!  ...  {current_time}")
            time.sleep(15)
            chime.info()
            time.sleep(0.2)
            chime.info()
        else:
            print(f"waiting... {current_time} - minutes in session {counter}")

        if counter == 30:
            print("Reached 30 minute session. Take a break!")
            chime.success()



if __name__ == "__main__":
    main()
