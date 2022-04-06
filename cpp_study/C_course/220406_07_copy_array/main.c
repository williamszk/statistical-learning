#include <stdio.h>

void printArr(int arr[], unsigned int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d  ", arr[i]);
    }
    printf("\n");
}

void copyArr(int originalArr[], int n, int (*copyArr)[])
{
    for (int i=0;i<n;i++)
    {
        (*copyArr)[i] = originalArr[i];
    }
}


// build a function that can copy an array to another array
void main()
{
    int arr[] = {1,2,3,4,5,6,7, 99, 87};
    int lenArr = sizeof(arr)/sizeof(arr[0]);
    int arrCopy[lenArr];

    copyArr(arr, lenArr, &arrCopy);

    printf("The original array: \t");
    printArr(arr, lenArr);

    printf("The copied array: \t");
    printArr(arrCopy, lenArr);

}
// this works!


// to pass a pointer of an array
// we use: int (*copyArr)[]
// but I read that we can just pass int *arr
// am I doing to much work here?