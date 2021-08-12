#include <stdio.h>

int main(){
    int holder;
    int i;

    // sorting problem
    int array1[] = {3,5,2,6,8,2};

    int lenArray1 = sizeof(array1)/sizeof(int);
    // printf("lenArray1 = %d\n",lenArray1);

    // insertion sort
    int order = 1;
    while(order == 1){
        order = 0;
        for (i = 0; i < lenArray1-1; i++ ){
            if (array1[i] > array1[i+1]){
                order = 1;
                holder = array1[i+1];
                array1[i+1] = array1[i];
                array1[i] = holder;
                printf("We exchanged places of %d and %d\n", array1[i], array1[i+1]);
            } 
        }    
    }

    void printArray(int *array){

        int sizeArray = sizeof(array)/sieof(int);
        printf("{");
        for (int j; j < sizeArray; j++){
            printf("%d, ",array[j]);
        }
        printf("}");

    }


    // int insertionSort(){
    //     // do stuff
    //     return 0;
    // }


    return 0;
}