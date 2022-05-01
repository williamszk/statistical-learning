// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30424720#overview
#include <stdio.h>
#include <stdlib.h>

void printTwoClosestToZero(int *arr, int n)
{
    int i;
    int currElem;
    int closest, semiClosest;
    if (abs(arr[0]) < abs(arr[1]))
    {
        closest = arr[0];
        semiClosest = arr[1];
    }
    else
    {
        closest = arr[1];
        semiClosest = arr[0];
    }

    for (i = 2; i < n; i++)
    {
        currElem = arr[i];

        if (abs(currElem) < abs(closest))
        {
            semiClosest = closest;
            closest = currElem;
        }
        else if (abs(currElem) < abs(semiClosest))
            semiClosest = currElem;
    }

    printf("The closest element to zero is %d and the second most close is %d.\n", closest, semiClosest);
}

void main()
{
    int arrLen;
    int myArr[] = {1, 5, -8, 8, -4, -2, 3, -3};
    arrLen = sizeof(myArr) / sizeof(myArr[0]);

    printTwoClosestToZero(myArr, arrLen);
    // the closest is 1
    // the second closes is -2

    int myArr2[] = {10, 20, -20, 9, -8};
    arrLen = sizeof(myArr2) / sizeof(myArr2[0]);
    printTwoClosestToZero(myArr2, arrLen);
    // the closest is -8
    // the second closest is 9
}