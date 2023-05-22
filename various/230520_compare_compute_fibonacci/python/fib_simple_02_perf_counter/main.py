from time import perf_counter


def main():
    # 1 1 2 3 5 8 13 21 34 55 89 144
    # 0 1 2 3 4 5  6  7  8  9 10  11
    # answer = fib(3)
    # print(f"{answer}: this should be 3")
    # answer = fib(6)
    # print(f"{answer}: this should be 13")
    # answer = fib(10)
    # print(f"{answer}: this should be 89")
    # answer = fib(9)
    # print(f"{answer}: this should be 55")
    # answer = fib(11)
    # print(f"{answer}: this should be 144")

    # real test
    start = perf_counter()

    for _ in range(1_000_000):
        answer = fib(40)

    print(f"{answer}; elapsed_time: {perf_counter() - start}s")


def fib(idx):
    if idx == 0:
        return 1
    elif idx == 1:
        return 1
    else:
        val_t_2 = 1
        val_t_1 = 1
        cur = 0
        for _ in range(2, idx + 1):
            cur = val_t_1 + val_t_2
            val_t_2 = val_t_1
            val_t_1 = cur

        return cur


if __name__ == "__main__":
    main()
