// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203104#overview
#include <stdio.h>

void main()
{
    int num1, num2, num3;
    printf("Write thre numbers:\n");
    printf("num1: ");
    scanf("%d", &num1);
    printf("num2: ");
    scanf("%d", &num2);
    printf("num3: ");
    scanf("%d", &num3);

    if (num1 > num2)
    {
        if (num2 > num3)
        {
            printf("%d is the largest and %d smallest\n", num1, num3);
        }
        else // num3 > num2
        {
            if (num3 > num1)
            {
                printf("%d is the largest and %d smallest\n", num3, num2);
            }
            else
            {
                printf("%d is the largest and %d smallest\n", num1, num2);
            }
        }
    }
    else // num2 > num1
    {
        if (num2 > num3)
        {
            if (num1 > num3)
            {
                printf("%d is the largest and %d smallest\n", num2, num3);
            }
            else // num3 > num1
            {
                printf("%d is the largest and %d smallest\n", num2, num1);
            }
        }
        else // num3 > num2
        {
            printf("%d is the largest and %d smallest\n", num3, num1);
        }
    }
}