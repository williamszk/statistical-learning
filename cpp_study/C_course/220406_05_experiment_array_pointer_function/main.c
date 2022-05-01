

#include <stdio.h>

void printPtrArr(int (*ptrArr)[], int n)
{

    for (int i = 0; i < n; i++)
    {
        printf("%d   ", (*ptrArr)[i]);
    }
    printf("\n");

}


void main()
{
    int arr[] = {1,2,3,4,5,6,98};

    int lenArr = sizeof(arr)/sizeof(arr[0]);

    printPtrArr(&arr, lenArr);
}
// this works