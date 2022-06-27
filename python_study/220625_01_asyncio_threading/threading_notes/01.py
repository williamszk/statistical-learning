# some of those notes are based on the the other project
# 211105_threading 

import time

start = time.perf_counter()

def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping...")

do_something()
do_something()

finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} second(s)")


# continue with the exploration