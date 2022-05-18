"""
Build animation for moving things in the terminal
"""

import time

UP = '\033[F'
counter = 1
while True:
    print(
        "#####\n"
        f"# {counter} #\n"
        "#####\n", end="")

    time.sleep(2)

    print(UP*4)

    counter += 1

# it did not work
# I need a way to delete what was already printed on the screen

# https://stackoverflow.com/questions/66458877/how-to-print-new-output-at-top-of-terminal-in-python
#
# it worked now, I needed to use UP = '\033[F'
