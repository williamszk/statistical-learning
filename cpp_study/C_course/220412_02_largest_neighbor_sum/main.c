// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25821684#overview

#include <stdio.h>
#include <limits.h>

// calculate the largest sum of two adjacent numbers
int calculateLargetSumTwoAdjacentNumbers(int *arr, int n)
{
    int sumAdj;
    int maxSum = INT_MIN;

    for (int i = 0; i <= n - 2; i++)
    {
        sumAdj = arr[i] + arr[i + 1];
        if (sumAdj > maxSum)
            maxSum = sumAdj;
    }

    return maxSum;
}

void main()
{
    int maxSum, lenArr;

    int arr1[] = {1, 4, 3, 7, 1};

    lenArr = sizeof(arr1) / sizeof(arr1[0]);

    maxSum = calculateLargetSumTwoAdjacentNumbers(arr1, lenArr);

    printf("The max sum of arr1 is: %d\n", maxSum);

    int arr2[] = {5, 7, 1, 5, 2};

    lenArr = sizeof(arr2) / sizeof(arr2[0]);

    maxSum = calculateLargetSumTwoAdjacentNumbers(arr2, lenArr);

    printf("The max sum of arr2 is: %d\n", maxSum);
}