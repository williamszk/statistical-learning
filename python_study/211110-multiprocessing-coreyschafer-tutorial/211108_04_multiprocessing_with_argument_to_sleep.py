# https://www.youtube.com/watch?v=fKl2JW_qrso&t=2s&ab_channel=CoreySchafer




import multiprocessing
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done sleeping...")

if __name__ == "__main__":

    processes_list =[]
    for _ in range(10):
        process = multiprocessing.Process(target=do_something, args=[5])
        process.start()
        processes_list.append(process)
        # process.join()
    
    for process in processes_list:
        process.join()

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} second(s)")

