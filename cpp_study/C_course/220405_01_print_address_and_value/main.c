// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20893824#overview

#include <stdio.h>

void main()
{
    int grade1 = 10, grade2 = -2;

    printf("%d\t%p\n", grade1, &grade1);
    printf("%d\t%p\n", grade2, &grade2);
}