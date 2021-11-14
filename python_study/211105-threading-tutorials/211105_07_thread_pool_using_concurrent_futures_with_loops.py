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

    list_futures_instances = [
        executor.submit(do_something, sec) for sec in seconds_list]

    # for f in concurrent.futures.as_completed(list_futures_instances):
    #     print(f.result())

    # here we needed to wait all 5 seconds for the result to be printed
    print([f.result() for f in list_futures_instances])


finish = time.perf_counter()

print(f"Finished in {round(finish - start, 4)} second(s)")