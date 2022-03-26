// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24147982#overview

#include <stdio.h>

void main()
{
    int num, i;
    printf("Write a number: ");
    scanf("%d", &num);

    for (i = 1; i <= num; i++)
    {
        printf("%d\n", i);
    }
    for (i = num; i >= 1; i--)
    {
        printf("%d\n", i);
    }

}