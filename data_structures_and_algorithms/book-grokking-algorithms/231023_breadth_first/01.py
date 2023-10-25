# https://www.youtube.com/watch?v=KXJSjte_OAI&ab_channel=TomScott

# implement binary search
# the objective: find the index or if the number 13 exists in the list

from copy import deepcopy


def find_position_of_element_in_sorted_list(sorted_list, searched_value):
    """This is the non-recursive way of writing a binary search algorithm."""
    my_list = deepcopy(sorted_list)
    aux_idx_list = list(range(len(my_list)))
    while True:
        length_list = len(my_list)
        if length_list == 0:
            return False, None

        if length_list == 1:
            if my_list[0] == searched_value:
                the_index = aux_idx_list[0]
                return True, the_index
            else:
                return False, None

        index_middle_value = length_list // 2
        middle_value = my_list[index_middle_value]

        if searched_value < middle_value:
            # The number that we seek is on the left part.
            my_list = my_list[:index_middle_value]
            aux_idx_list = aux_idx_list[:index_middle_value]
        else:
            # The number that we seek is on the right part.
            my_list = my_list[index_middle_value:]
            aux_idx_list = aux_idx_list[index_middle_value:]


def find_position_of_element_in_sorted_list_recursive(sorted_list, searched_value):
    """This is the recursive way of writing a binary search algorithm."""
    my_list = deepcopy(sorted_list)
    aux_idx_list = list(range(len(my_list)))

    def foo(my_list, aux_idx_list):
        length_list = len(my_list)
        if length_list == 0:
            return False, None

        if length_list == 1:
            if my_list[0] == searched_value:
                the_index = aux_idx_list[0]
                return True, the_index
            else:
                return False, None

        else:
            index_middle_value = length_list // 2
            middle_value = my_list[index_middle_value]
            if searched_value < middle_value:
                my_list = my_list[:index_middle_value]
                aux_idx_list = aux_idx_list[:index_middle_value]
                return foo(my_list, aux_idx_list)
            else:
                my_list = my_list[index_middle_value:]
                aux_idx_list = aux_idx_list[index_middle_value:]
                return foo(my_list, aux_idx_list)

    return foo(my_list, aux_idx_list)


my_list = [49, 9, 20, 1, 50, 11, 4, 13, 3, 42, 8]


# first we need to sort the list
print("---- non-recursive 01 --------------------------------------------------")
my_list_2 = sorted(my_list)
searched_value = 13
ok, idx = find_position_of_element_in_sorted_list(my_list_2, searched_value)
print(my_list_2)
print(ok, idx, "; it should be 6")
print("---- non-recursive 02 --------------------------------------------------")
ok, idx = find_position_of_element_in_sorted_list(my_list_2, 50)
print(my_list_2)
print(ok, idx, "; it should be 10")
print("---- non-recursive 03 --------------------------------------------------")
ok, idx = find_position_of_element_in_sorted_list(my_list_2, 21)
print(my_list_2)
print(ok, idx, "; it should be None")
print("--- recursive 01 -------------------------------------------------------")
ok, idx = find_position_of_element_in_sorted_list_recursive(my_list_2, 50)
print(my_list_2)
print(ok, idx, "; it should be 10")
print("---- non-recursive 02 --------------------------------------------------")
ok, idx = find_position_of_element_in_sorted_list_recursive(my_list_2, 13)
print(my_list_2)
print(ok, idx, "; it should be 6")
print("---- non-recursive 03 --------------------------------------------------")
ok, idx = find_position_of_element_in_sorted_list_recursive(my_list_2, 21)
print(my_list_2)
print(ok, idx, "; it should be None")

# divide your list into two parts in the middle
# the left part has smaller values
# the right parts has larger values

# There is a recursive way of writing this algorithm.
# And there is a non-recursive way of writing it.


# Next episode:
# - Build a binary tree data structure.
# - Build a program that can find values in the binary tree.
