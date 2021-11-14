# example with 10 threads
# the thread object has methods start and join
# these methods are expressions but they return None

import threading
import time
start = time.perf_counter()

def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping...")

# instante thread objects
list_threads = [threading.Thread(target=do_something) for _ in range(10)]

# start threads
[thread_instante.start() for thread_instante in list_threads]

# wait for threads to finish with join() method
[thread_instance.join() for thread_instance in list_threads]

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")

