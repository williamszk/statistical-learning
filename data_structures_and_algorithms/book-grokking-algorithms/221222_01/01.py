

def find_position(elem, the_list):
    offset = 0
    while len(the_list) >= 1:
        # print(f"{the_list = }")
        # print(f"{offset = }")
        i = int(len(the_list)/2)
        if the_list[i] == elem:
            return i + offset
        elif the_list[i] < elem:
            offset += len(the_list[0:(i+1)])
            the_list = the_list[i+1:]
        else:
            the_list = the_list[0:i]

    return None


def main():
    elem =  9
    index = find_position(elem, [0,1,2,3,4,5,6,7,8,9,10])

    assert find_position(2, [0,1,2,3,4,5,6,7,8,9,10]) == 2
    assert find_position(1, [0,1,2,3,4,5,6,7,8,9,10]) == 1
    assert find_position(8, [0,1,2,3,4,5,6,7,8,9,10]) == 8
    assert find_position(9, [0,1,2,3,4,5,6,7,8,9,10]) == 9
    assert find_position(10, [0,1,2,3,4,5,6,7,8,9,10]) == 10

if __name__ == "__main__":
    main()