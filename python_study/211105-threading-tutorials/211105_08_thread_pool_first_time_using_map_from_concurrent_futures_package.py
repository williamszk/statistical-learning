# https://youtu.be/IEEhzQoKtQU?t=1352

import concurrent.futures

import time
start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done sleeping... for sec={seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds_list = [5,4,3,2,1]
    list_futures_instances = executor.map(do_something, seconds_list)

    for i in list_futures_instances:
        print(i)

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 4)} second(s)")