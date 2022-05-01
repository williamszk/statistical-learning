#include <stdio.h>

// can we build a function that returns a pointer of an array?
// I think that we need to return also the size of the array that is returned

void printArr(int arr[], unsigned int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d  ", arr[i]);
    }
    printf("\n");
}


int *retArrInt()
{
    int myarr[] = {1, 2, 3, 4};

    int (*ptrMyArr)[4] = &myarr;

    return ptrMyArr;
}

void main()
{
    int *ptrMyArr = retArrInt();

    printArr(*ptrMyArr, 4);
}

// it didn't work
// I need to study more...