// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203754#overview

#include <stdio.h>

void main()
{
    char name[] = "William Suzuki";

    int arrLen = sizeof(name) / sizeof(name[0]);

    for (int i = 0; i < arrLen; i++)
    {
        printf("%c", name[i]);
    }
    printf("##");
    printf("\n");
}