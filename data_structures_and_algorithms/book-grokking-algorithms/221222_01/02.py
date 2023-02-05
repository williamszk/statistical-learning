from typing import Callable


def find_position(elem, the_list):
    offset = 0
    while len(the_list) >= 1:
        i = int(len(the_list) / 2)
        if the_list[i] == elem:
            return i + offset
        elif the_list[i] < elem:
            offset += len(the_list[0 : (i + 1)])
            the_list = the_list[i + 1 :]
        else:
            the_list = the_list[0:i]

    return None


def sample_perf_test(find_function: Callable, n=1000, loops=100):
    # print("======================================================")
    # print(f"Executing sample performance test: {n=}, {loops=}")
    from time import perf_counter

    start = perf_counter()
    for _ in range(loops):
        assert find_function(0, list(range(n))) == 0
        assert find_function(1, list(range(n))) == 1
        assert find_function(2, list(range(n))) == 2
        assert find_function(8, list(range(n))) == 8
        assert find_function(9, list(range(n))) == 9
        assert find_function(10, list(range(n))) == 10
    elapsed_time = perf_counter() - start
    # print(f"Elapsed time: {elapsed_time}")

    return {
        "n": n,
        "loops": loops,
        "elapsed_time": elapsed_time,
    }


def gen_n_candidates():
    n_candidates = []

    i = 100
    while i < 10e9:
        n_candidates.append(i)
        i = i * 2

    return n_candidates

def setup_logging():
    import logging
    from datetime import datetime

    time_now = str(datetime.now()).split(".")[0].replace(":", "-")
    logging.basicConfig(
        filename=f"logs/{time_now}.log", encoding="utf-8", level=logging.DEBUG,
        format="%(message)s", 
    )


def main():
    import logging
    setup_logging()
    n_candidates = gen_n_candidates()
    logging.info("[")
    for n in n_candidates:
        logging.info(str(sample_perf_test(find_position, n=n, loops=100))+",")
    logging.info("]")


if __name__ == "__main__":
    main()
