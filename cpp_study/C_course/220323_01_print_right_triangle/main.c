// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24148036#overview
#include <stdio.h>

void main()
{
    int num, i, j;
    printf("Write a number: ");
    scanf("%d", &num);

    for (i = 1; i <= num; i++)
    {
        for (j = 1; j <= i; j++)
        {
            printf("%d", j);
        }
        printf("\n");
    }

}