#include <stdio.h>

void printPtrArrLen5(int (*ptrArr)[5])
{
    for (int i=0; i<5; i++)
    {
        printf("%d  ", (*ptrArr)[i]);
    }
    printf("\n");
}

void main()
{
    // build a function where we pass a pointer of array of integers with size 5

    // how to create a pointer of array of ints of size 5
    // int (*ptrArr1)[5];
    int arr[] = {1,2,3,4,999};

    printPtrArrLen5(&arr);
    // this works!

}

// do I need to specify the number of itens in the array in the 
// parameter of the function printPtrArrLen5?