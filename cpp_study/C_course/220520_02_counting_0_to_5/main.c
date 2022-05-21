// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30802556#questions

#include <stdio.h>

int main()
{
    int i;

    int arr[] = {0, 5, 4, 2, 1, 3, 2, 0};

    int arrCnt[6] = {0};

    int lenArr = sizeof(arr) / sizeof(arr[0]);

    for (i = 0; i < lenArr; i++)
    {
        arrCnt[arr[i]]++;
    }

    lenArr = sizeof(arrCnt) / sizeof(arrCnt[0]);

    printf("Frequency table:\n");

    for (i = 0; i < lenArr; i++)
    {
        printf("%d : %d\n", i, arrCnt[i]);
    }

    return 0;
}