// Implement binary search
// The objective: find the index or if the number 13 exists in the list

#include <stdio.h>
#include <stdlib.h>

int find_position_of_element_in_sorted_list(int* sorted_list, int length, int* index_out){
    // return 0 if everything is ok
    // return -1 if we couldn't find the element
    // and include 0 as the out of the index

    // printf("%X\n", sorted_list);

    // for (int i=0;i<length;i++){
    //     printf("%d\n", sorted_list[i]);
    // }

    // create auxiliary array of indexes
    int* aux_index_arr = (int*)malloc(length*sizeof(int));

    // for (int i=0;i<length;i++){
    //     printf("%d\n", aux_index_arr[i]);
    // }

    free(aux_index_arr);
    return 0;
}

// Is there a way to do recursion in C?


int main(){

    // my_list = [49, 9, 20, 1, 50, 11, 4, 13, 3, 42, 8]
    // sorted list: [1, 3, 4, 8, 9, 11, 13, 20, 42, 49, 50]
    int my_list[11] = {49, 9, 20, 1, 50, 11, 4, 13, 3, 42, 8};
    int my_list_2[11] = {1, 3, 4, 8, 9, 11, 13, 20, 42, 49, 50};

    int index_out = 0;
    int status = find_position_of_element_in_sorted_list(my_list_2, 11, &index_out);



    return 0;
}