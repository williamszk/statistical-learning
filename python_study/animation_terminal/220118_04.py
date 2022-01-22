"""
Another try to make animation
"""


import time
import numpy as np


HORIZONTAL_DIM = 120
VERTICAL_DIM = 28
UP = '\033[F'
HORIZONTAL_BAR = "+"+"-"*HORIZONTAL_DIM+"+"+"\n"



def pacman_animation():
    
    list_strings_image_00 = [
        "              #####        ",
        "           ###     ###     ",
        "        ###           ##   ",
        "      ##      ###       ## ",
        "    ##        ###     ##   ",
        "  ##                ##     ",
        " ##               ##       ",
        " ##             ##         ",
        " ##               ##       ",
        "  ##                ##     ",
        "    ##                ##   ",
        "      ##                ## ",
        "        ###           ##   ",
        "           ###     ###     ",
        "              #####        ",
    ]

    list_motion_lists = [list_strings_image_00]
    return list_motion_lists


counter = 1
list_strings_image = [" "]*VERTICAL_DIM
while True:
    
    # list_strings_image = [" "]*VERTICAL_DIM
    # list_strings_image[counter] = " "*int(np.floor(counter**2)) + str(0)

    list_motion_lists_pacman = pacman_animation()
    # the first image, index = 0
    first_image = list_motion_lists_pacman[0]
    for i in range(len(list_strings_image)):
        if i == len(first_image):
            break
        list_strings_image[i] = " "*counter + first_image[i]

    list_n_space = [HORIZONTAL_DIM - len(x) - 2 for x in list_strings_image]

    print(f"{HORIZONTAL_BAR}", end="")
    for i in range(VERTICAL_DIM):
        print(f"| {list_strings_image[i]}{' '*list_n_space[i]} |\n", end="")
    print(f"{HORIZONTAL_BAR}", end="")

    time.sleep(0.5)
    print(UP*(VERTICAL_DIM+3))
    counter += 1


