import shutil
import time

MIN_STREAM_LENGTH = 6  # The shortest vertical stream length
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAM_CHARS = ["0", "1"]
DENSITY = 0.02  # Density can range from 0.0 to 1.0
WIDTH = shutil.get_terminal_size()[0]

# to adjust for a weird behavior on Windows, we subtract one column from the width
WIDTH -= 1


def main(name):
    digital_stream()


def digital_stream():
    print("Digital Stream")
    print("Press ctrl-c to quit")
    time.sleep(2)  # Pause at the start to let user read credits and instruction to quit

    columns = [0] * WIDTH
    print("debug: ", columns)
    print("debug len of columns: ", len(columns))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('There pythonista')

# stopped at:
# https://youtu.be/BwMkYYpok9I?t=496
