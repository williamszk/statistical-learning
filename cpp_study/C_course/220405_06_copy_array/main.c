// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/26675246?start=15#overview

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
    int myarr[] = {1, 4, 2022};

    int anotherArr[3];

    printArr(myarr, 3);

    for (int i = 0; i < 3; i++)
    {
        anotherArr[i] = myarr[i];
    }

    printArr(anotherArr, 3);
}
