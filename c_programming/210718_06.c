#include <stdio.h>

void printArray(int *array, int lenArray){
    printf("{");
    for (int j; j < lenArray; j++){
        if (j < lenArray-1){
            printf("%d, ",array[j]);
        } else {
            printf("%d",array[j]);
        }
    }
    printf("}\n");
}


int main(){
    int array1[] = {3,5,2,6,8,2};
    int lenArray = sizeof(array1)/sizeof(int);
    
    printArray(array1, lenArray);

    return 0;
}