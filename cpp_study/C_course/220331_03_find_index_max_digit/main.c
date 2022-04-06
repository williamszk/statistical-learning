// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203700#overview

#include <stdio.h>

void main()
{

    int maxDigit = 0;
    int indexMaxDigit;
    int i = 0;
    int digits[] = {1, 3, 4, 7, 5};

    int lenArr = sizeof(digits) / sizeof(int);

    for (i = 0; i < lenArr; i++)
    {
        if (maxDigit < digits[i])
        {
            maxDigit = digits[i];
        }
    }

    printf("The max digit is: %d\n", maxDigit);

    for (i = 0; i < lenArr; i++)
    {
        if (maxDigit == digits[i])
        {
            indexMaxDigit = i;
        }
    }

    printf("The index of the max digit is: %d\n", indexMaxDigit);
}