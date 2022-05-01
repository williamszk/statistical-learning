// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25741738#overview

#include <stdio.h>

int classifySortedArr(int *arr, int n)
{
    /*
    1: really sorted
    2: sorted
    3: not sorted
    */
    int existEqual = 0;
    for (int i = 0; i < n - 1; i++)
    {
        if (arr[i] > arr[i + 1])
            // there is one case of unsorted, so the array is whole unsorted
            return 3;
        else if (arr[i] == arr[i + 1])
            // there is one case of equal values
            existEqual = 1;
    }
    // if the program reach here, it means that the array or is sorted or reall sorted
    if (existEqual == 1)
        return 2;
    else
        return 1;
}

void printClassSorted(int classSort)
{
    if (classSort == 1)
        printf("The arrays is Really Sorted.\n");
    else if (classSort == 2)
        printf("The arrays is Sorted.\n");
    else if (classSort == 3)
        printf("The arrays is Not Sorted.\n");
    else
        printf("This class is not recognized.\n");
}

void main()
{
    int lenArr;
    int classSort;

    int arr1[] = {1, 2, 5, 7, 10}; // should return "Really sorted"
    lenArr = sizeof(arr1) / sizeof(arr1[0]);
    classSort = classifySortedArr(arr1, lenArr);
    printf("arr1: ");
    printClassSorted(classSort);

    int arr2[] = {1, 2, 2, 5, 10}; // "Sorted"

    lenArr = sizeof(arr2) / sizeof(arr2[0]);
    classSort = classifySortedArr(arr2, lenArr);
    printf("arr2: ");
    printClassSorted(classSort);

    int arr3[] = {1, 2, 5, 3, 10}; // "Not sorted"
    lenArr = sizeof(arr3) / sizeof(arr3[0]);
    classSort = classifySortedArr(arr3, lenArr);
    printf("arr3: ");
    printClassSorted(classSort);
}