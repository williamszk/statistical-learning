#include <stdio.h>
#include "module.h"

int main(){

    int myArray[] = {4,5,3,2,5,6};

    int lenArray = sizeof(myArray)/sizeof(int);
    printArrayInt(myArray, lenArray);   


    return 0;
}