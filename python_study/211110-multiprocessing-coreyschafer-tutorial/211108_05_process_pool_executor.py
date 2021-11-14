# https://www.youtube.com/watch?v=fKl2JW_qrso&t=2s&ab_channel=CoreySchafer

import concurrent.futures # process pool executor
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return "Done sleeping..."

if __name__ == "__main__":

    with concurrent.futures.ProcessPoolExecutor() as executor:
        future_object = executor.submit(do_something, 5)
        print(future_object.result())

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} second(s)")



