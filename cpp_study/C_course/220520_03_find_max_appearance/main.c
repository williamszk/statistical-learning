// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30802562?start=15#questions

#include <stdio.h>

int main()
{
    int i;

    int sourceArr[] = {0, 5, 4, 9, 5, 8, 2, 3, 1, 5, 4, 9, 5, 5, 2, 7, 6, 5, 4, 1, 5, 9, 9, 9, 9, 8, 9, 9, 9};
    int arrCnt[10] = {0};

    int lenArr = sizeof(sourceArr) / sizeof(sourceArr[0]);

    for (i = 0; i < lenArr; i++)
    {
        arrCnt[sourceArr[i]]++;
    }

    // find the value that appears most in frequency
    lenArr = sizeof(arrCnt) / sizeof(arrCnt[0]);
    int maxIdx = 0;
    for (i = 1; i < lenArr; i++)
        if (arrCnt[i] > arrCnt[maxIdx])
            maxIdx = i;

    printf("The value of %d appeared most of the times. Total of %d appearances.", maxIdx, arrCnt[maxIdx]);

    return 0;
}
