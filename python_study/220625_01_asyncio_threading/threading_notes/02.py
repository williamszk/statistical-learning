import threading
import time
start = time.perf_counter()

def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping...")

# create thread objects
thread_01 = threading.Thread(target=do_something)
thread_02 = threading.Thread(target=do_something)

# the start method will start the thread
# then it will be treated as a seperate task
thread_01.start()
thread_02.start()

# the join method will wait for the end of the thread
thread_01.join()
thread_02.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")
