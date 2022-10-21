import integrate 
import integrate1 # type: ignore
import integrate2 # type: ignore
import time

def main():
    num_loop = 3000
    start = time.perf_counter()
    for _ in range(num_loop):
        integrate.integrate_f(0, 100, 1000)
    elapsed_time = time.perf_counter() - start
    print(f"python  : {elapsed_time: <10}")

    start = time.perf_counter()
    for _ in range(num_loop):
        integrate1.integrate_f(0, 100, 1000)
    elapsed_time = time.perf_counter() - start
    print(f"cython 1: {elapsed_time: <10}")

    start = time.perf_counter()
    for _ in range(num_loop):
        integrate2.integrate_f(0, 100, 1000)
    elapsed_time = time.perf_counter() - start
    print(f"cython 2: {elapsed_time:_<10}")

if __name__ == "__main__":
    main()