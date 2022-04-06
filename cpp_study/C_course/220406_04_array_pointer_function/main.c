// do I need to specify the number of itens in the array in the 
// parameter of the function printPtrArrLen5?

#include <stdio.h>


void printArrPtrLenAny(int (*ptrArr)[])
{
    for (int i=0; i<10; i++)
    {
        printf("%d   ", (*ptrArr)[i]);
    }
    printf("\n");
}


void main()
{
    int arr[] = {1,2,3,4,5};

    printArrPtrLenAny(&arr);
}
// output:
// 1   2   3   4   5   32765   1661635584   707662347   0   0 
// this works