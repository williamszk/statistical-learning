import concurrent.futures

import time
start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return "Done sleeping..."

with concurrent.futures.ThreadPoolExecutor() as executor:
    future_01 = executor.submit(do_something, 1)
    future_02 = executor.submit(do_something, 1)
    print(future_01.result())
    print(future_02.result())

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 4)} second(s)")