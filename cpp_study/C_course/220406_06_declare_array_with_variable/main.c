

#include <stdio.h>

void printArr(int arr[], unsigned int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d  ", arr[i]);
    }
    printf("\n");
}

void main()
{
    int i;

    int arr[] = {1,2,2,3,3,99};

    int n = sizeof(arr)/sizeof(arr[0]);

    int arr2[n]; // we can pass a variable to specify the size of the array

    for (i =0; i<n;i++)
    {
        arr2[i] = i;
    }

    printArr(arr2, n);
}

// this works!