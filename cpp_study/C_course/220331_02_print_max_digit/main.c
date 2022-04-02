// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203688#overview

#include <stdio.h>

void main()
{
    int i;
    int maxDigit = 0;
    int telDigits[9];

    for (i = 0; i < 9; i++)
    {
        printf("Write the digit of your telephone number (%d/9): ", i + 1);
        scanf("%d", &telDigits[i]);
    }

    printf("Your telphone number is: ");
    for (i = 0; i < 9; i++)
    {
        printf("%d ", telDigits[i]);
    }
    printf("\n");

    for (i = 0; i < 9; i++)
    {
        if (maxDigit < telDigits[i])
        {
            maxDigit = telDigits[i];
        }
    }

    printf("The max digit is: %d\n", maxDigit);
}