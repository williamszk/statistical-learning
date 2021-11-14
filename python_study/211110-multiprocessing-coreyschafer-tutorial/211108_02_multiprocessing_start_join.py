# https://www.youtube.com/watch?v=fKl2JW_qrso&t=2s&ab_channel=CoreySchafer




import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping...")

# https://stackoverflow.com/a/63588182/8782077
# I had a problem trying to run the program without the __name__ == "__main__"
if __name__ == "__main__":

    process1 = multiprocessing.Process(target=do_something)
    process2 = multiprocessing.Process(target=do_something)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} second(s)")

# In this script we see that the process took 1.33 seconds to run.

# Sleeping 1 second...
# Sleeping 1 second...
# Done sleeping...
# Done sleeping...
# Finished in 1.33 second(s)


