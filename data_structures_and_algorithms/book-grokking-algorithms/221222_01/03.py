def find_position(elem, the_list):
    offset = 0
    while len(the_list) >= 1:
        print(f"{len(the_list) = }")
        i = int(len(the_list) / 2)
        if the_list[i] == elem:
            return i + offset
        elif the_list[i] < elem:
            offset += len(the_list[0 : (i + 1)])
            the_list = the_list[i + 1 :]
        else:
            the_list = the_list[0:i]

    return None


def main():
    assert find_position(2, list(range(1000))) == 2


if __name__ == "__main__":
    main()
