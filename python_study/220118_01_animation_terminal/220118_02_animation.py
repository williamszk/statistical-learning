"""
Another try to make animation
"""


import time


HORIZONTAL_DIM = 100
UP = '\033[F'
HORIZONTAL_BAR = "+"+"-"*HORIZONTAL_DIM+"+"+"\n"

counter = 1
while True:
    
    substance = str(counter)
    n_spaces = HORIZONTAL_DIM - len(substance) - 2

    print(
        f"{HORIZONTAL_BAR}"
        f"| {counter}{' '*n_spaces} |\n"
        f"{HORIZONTAL_BAR}", end="")

    time.sleep(2)
    print(UP*4)
    counter += 1


