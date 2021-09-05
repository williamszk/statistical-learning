#include <stdio.h>
#include <module.h>

int main() {
    // build a greedy algorithm for the following problem:
    // given an array [3, 4, -1, 2, -3, 0] and n = 4
    // find the largest sum of numbers in the array

    int arr1[] = {3, 4, -1, 2, -3, 0};
    int n = 4;
    int num_found = 0;
    // printf("%d\n", num_found);

    int len_arr1 = sizeof(arr1)/sizeof(int);

    // printf("len_arr1: %d\n", len_arr1);

    // print_array_int(int *array, int lenArray)
    print_array_int(arr1, len_arr1);

    for (int i = 0; i < len_arr1; i++){
        printf("%d\n", arr1[i]); 
    }

    // while(num_found <= n){
    //     for (int i = 0; i <= len_arr1; i++){
    //         printf("%d\n", arr1[i]); 
    //     } 
    // }


    return 0;
}

