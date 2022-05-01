// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/26675246?start=15#overview

#include <stdio.h>

void printElemArr(int *arr, unsigned int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%d  ", arr[i]);
    }
    printf("\n");
}

void printElemArrJustArr(int *arr)
{
    // this does not work properly
    int i;
    int n = sizeof(arr) / sizeof(arr[0]);
    for (i = 0; i < n; i++)
    {
        printf("%d  ", arr[i]);
    }
    printf("\n");
}

void copyArray(int dates[], int *newArrDate[])
{
    for (int i = 0; i < 3; i++)
    {
        *newArrDate[i] = dates[i];
    }
}

void main()
{
    int newArraDate[3]; // an array to store the new data

    int myOrigDate[] = {1, 4, 2022};
    printf("Original date: %d-%d-%d\n", myOrigDate[0], myOrigDate[1], myOrigDate[2]);

    // copyArray(myOrigDate, newArraDate);
    printElemArr(&myOrigDate, 3);
    printElemArrJustArr(&myOrigDate);

    copyArray(myOrigDate, &newArraDate);
}