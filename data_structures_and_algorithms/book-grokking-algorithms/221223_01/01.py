import time
import logging
from datetime import datetime
import inspect


def log_perf(func):
    """This is a higher order function that will measure the time of execution
    and save it into a file. The configuration of logging must be done before
    running this decorator.
    """

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        output = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start
        logging.info(f"{inspect.stack()[1][3]};{len(args[0])=};{elapsed_time=}")
        return output

    return wrapper


def setup_logging():
    time_now = str(datetime.now()).split(".")[0].replace(":", "-")
    logging.basicConfig(
        filename=f"logs/{time_now}.log",
        encoding="utf-8",
        level=logging.DEBUG,
        format="%(message)s",
    )


@log_perf
def binary_search(a_list, p):
    left = 0
    right = len(a_list) - 1
    while left <= right:
        mid = (right + left) // 2
        if a_list[mid] == p:
            return mid
        elif mid < p:
            left = mid + 1
        else:  # mid > p
            right = mid - 1
    return None


@log_perf
def naive_search(a_list, p):
    for num in a_list:
        if a_list[num] == p:
            return num
    return None


def main():
    setup_logging()
    list01 = list(range(100))
    binary_search(list01, 2)
    naive_search(list01, 2)


if __name__ == "__main__":
    main()
