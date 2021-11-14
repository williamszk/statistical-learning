import concurrent.futures

import time
start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return "Done sleeping..."

with concurrent.futures.ThreadPoolExecutor() as executor:
    list_futures_instances = [
        executor.submit(do_something, 1) for _ in range(10)]

    print([future_instance.result() for future_instance in  list_futures_instances])


finish = time.perf_counter()

print(f"Finished in {round(finish - start, 4)} second(s)")