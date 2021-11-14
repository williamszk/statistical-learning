import threading
import time
start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done sleeping...")

# instante thread objects
list_threads = [threading.Thread(target=do_something, args=[1.5]) for _ in range(10)]

# start threads
[thread_instante.start() for thread_instante in list_threads]

# wait for threads to finish with join() method
[thread_instance.join() for thread_instance in list_threads]

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 4)} second(s)")