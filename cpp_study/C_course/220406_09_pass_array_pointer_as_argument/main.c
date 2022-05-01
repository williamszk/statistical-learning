// to pass a pointer of an array
// we use: int (*copyArr)[]
// but I read that we can just pass int *arr
// am I doing to much work here?

#include <stdio.h>

void printArr(int *arr, int n)
{
    // there is a difference between passing an array to a function
    // and passing the pointer of an array to a function

    // I've read the passing "int arr[]" is equivalent to use int "*arr"
    // let's experiment to see
    // https://stackoverflow.com/questions/6638729/when-do-we-need-to-pass-the-size-of-array-as-a-parameter

    for (int i = 0; i < n; i++)
    {
        printf("%d  ", arr[i]);
    }
    printf("\n");
}

void printArrAlter(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d  ", arr[i]);
    }
    printf("\n");
}

void main()
{
    int arr[] = {1, 2, 3, 4, 5};

    int lenArr = sizeof(arr) / sizeof(arr[0]);

    printArr(arr, lenArr); // this works!

    printArrAlter(arr, lenArr); // this works!
}

// this works!