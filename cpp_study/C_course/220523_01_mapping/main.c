// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30802576?start=15#questions
// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30802582#questions

#include <stdio.h>
#define SIZE 5

int main()
{
    int i;
    int sourceArr[] = {7, 7, 7, 5, 6, 9, 6, 7, 10, 7};
    int countArr[6] = {0};

    int lenArr = sizeof(sourceArr)/sizeof(sourceArr[0]);

    for (i = 0; i < lenArr; i++)
    {
       countArr[sourceArr[i] - SIZE] ++;
    }

    int maxIdx = 0;
    lenArr = sizeof(countArr)/sizeof(countArr[0]);
    for (i = 0; i < lenArr; i++)
        if (countArr[i] > countArr[maxIdx])
            maxIdx = i;

    int maxFreq = countArr[maxIdx];
    int maxVal = maxIdx + SIZE; 

    printf("The value of %d appeared most of the times. Total of %d appearances.", maxVal, maxFreq);

    return 0;
}