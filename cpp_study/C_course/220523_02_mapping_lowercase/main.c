// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30802610#questions

#include <stdio.h>

int main()
{
    int i;
    int sourceArr[] = {'b', 'k', 'i', 'b', 'r', 'b', 'k', 'z', 'm'};

    int countArr[26] = {0};

    int lenArr = sizeof(sourceArr) / sizeof(sourceArr[0]);
    for (i = 0; i < lenArr; i++)
    {
        countArr[sourceArr[i] - 'a']++;
    }

    int maxIdx = 0;
    lenArr = sizeof(countArr) / sizeof(countArr[0]);
    for (i = 0; i < lenArr; i++)
        if (countArr[i] > countArr[maxIdx])
            maxIdx = i;

    int maxFreq = countArr[maxIdx];
    int maxChar = maxIdx + 'a';

    printf("The letter '%c' appeared most of the times. Total of %d appearances.", maxChar, maxFreq);

    return 0;
}