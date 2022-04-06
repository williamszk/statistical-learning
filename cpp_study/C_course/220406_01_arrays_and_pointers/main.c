#include <stdio.h>

void printArr(int arr[], unsigned int n)
{
    // we can pass an array as an argument to a function
    for (int i = 0; i < n; i++)
    {
        printf("%d  ", arr[i]);
    }
    printf("\n");
}

void main()
{
    // how can we build a pointer for array?
    int arr1[] = {1,2,3,4,5};

    int (*ptrArr1)[5] = &arr1;
    // prtArr1 is a pointer to an array of ints of size 5

    printArr(*ptrArr1, 5);
    // this works
}