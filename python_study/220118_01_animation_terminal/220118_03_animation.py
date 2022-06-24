"""
Another try to make animation
"""


import time


HORIZONTAL_DIM = 120
VERTICAL_DIM = 28
UP = '\033[F'
HORIZONTAL_BAR = "+"+"-"*HORIZONTAL_DIM+"+"+"\n"

counter = 1
list_strings_image = [" "]*VERTICAL_DIM
while True:
    
    list_n_space = [HORIZONTAL_DIM - len(x) - 2 for x in list_strings_image]

    list_strings_image[counter] = str(0)

    print(
        f"{HORIZONTAL_BAR}"
        f"| {list_strings_image[0]}{' '*list_n_space[0]} |\n"
        f"| {list_strings_image[1]}{' '*list_n_space[1]} |\n"
        f"| {list_strings_image[2]}{' '*list_n_space[2]} |\n"
        f"| {list_strings_image[3]}{' '*list_n_space[3]} |\n"
        f"| {list_strings_image[4]}{' '*list_n_space[4]} |\n"
        f"| {list_strings_image[5]}{' '*list_n_space[5]} |\n"
        f"| {list_strings_image[6]}{' '*list_n_space[6]} |\n"
        f"| {list_strings_image[7]}{' '*list_n_space[7]} |\n"
        f"| {list_strings_image[8]}{' '*list_n_space[8]} |\n"
        f"| {list_strings_image[9]}{' '*list_n_space[9]} |\n"
        f"| {list_strings_image[10]}{' '*list_n_space[10]} |\n"
        f"| {list_strings_image[11]}{' '*list_n_space[11]} |\n"
        f"| {list_strings_image[12]}{' '*list_n_space[12]} |\n"
        f"| {list_strings_image[13]}{' '*list_n_space[13]} |\n"
        f"| {list_strings_image[14]}{' '*list_n_space[14]} |\n"
        f"| {list_strings_image[15]}{' '*list_n_space[15]} |\n"
        f"| {list_strings_image[16]}{' '*list_n_space[16]} |\n"
        f"| {list_strings_image[17]}{' '*list_n_space[17]} |\n"
        f"| {list_strings_image[18]}{' '*list_n_space[18]} |\n"
        f"| {list_strings_image[19]}{' '*list_n_space[19]} |\n"
        f"| {list_strings_image[20]}{' '*list_n_space[20]} |\n"
        f"| {list_strings_image[21]}{' '*list_n_space[21]} |\n"
        f"| {list_strings_image[22]}{' '*list_n_space[22]} |\n"
        f"| {list_strings_image[23]}{' '*list_n_space[23]} |\n"
        f"| {list_strings_image[24]}{' '*list_n_space[24]} |\n"
        f"| {list_strings_image[25]}{' '*list_n_space[25]} |\n"
        f"| {list_strings_image[26]}{' '*list_n_space[26]} |\n"
        f"| {list_strings_image[27]}{' '*list_n_space[27]} |\n"
        f"{HORIZONTAL_BAR}", end="")

    time.sleep(0.5)
    print(UP*(VERTICAL_DIM+3))
    counter += 1


