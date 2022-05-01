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
    // can we pass the values of the array to a pointer without specifying its size?

    int arr1[] = {1, 2, 3, 4, 5};
    int(*ptrArrEx1)[] = &arr1; // this will break the code
    // the code will send warnings
    // we should specify the number of elements in the array
    printArr(&ptrArrEx1, 5);
}
// this doesn't work...

// is there a situation where we can declare a pointer of an array
// without specifying the number of elements in the array?

// furthermore is there a situation where we can declare the pointer
// without assigning nothing to it?