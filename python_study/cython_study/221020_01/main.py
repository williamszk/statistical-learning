import hello  # type: ignore
import hello2
import time

import integrate
import integrate_comp # type: ignore

def main():
    num_loop = 3000

    start = time.perf_counter()
    for _ in range(num_loop):
        hello.say_hello_to("Bob")
    elapsed_time = time.perf_counter() - start
    print(f"Test 1 for python: {elapsed_time}")

    start = time.perf_counter()
    for _ in range(num_loop):
        hello2.say_hello_to("Alice")
    elapsed_time_2 = time.perf_counter() - start

    print(f"Test 1 for cython: {elapsed_time_2}")

    print("=====================================")
    num_loop = 3000

    start = time.perf_counter()
    for _ in range(num_loop):
        integrate.integrate_f(0, 100, 100)
    elapsed_time = time.perf_counter() - start
    print(f"Test 2 for python: {elapsed_time}")

    start = time.perf_counter()
    for _ in range(num_loop):
        integrate_comp.integrate_f(0, 100, 100)
    elapsed_time_2 = time.perf_counter() - start
    print(f"Test 2 for cython: {elapsed_time_2}")



if __name__ == "__main__":
    main()