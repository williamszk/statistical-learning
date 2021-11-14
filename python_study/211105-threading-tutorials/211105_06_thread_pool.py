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

    # we can manipulate the threads in the order that they were completed
    for f in concurrent.futures.as_completed(list_futures_instances):
        print(f.result())

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 4)} second(s)")