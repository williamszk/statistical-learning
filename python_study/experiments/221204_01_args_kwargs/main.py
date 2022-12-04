def main():
    foo(1, 2, 3, a=1, b=2, c=3)


def foo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


if __name__ == "__main__":
    main()

# args: (1, 2, 3)
# kwargs: {'a': 1, 'b': 2, 'c': 3}