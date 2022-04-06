// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20350945#overview

#include <stdio.h>

void swap(int *pNum1, int *pNum2)
{
    int temp = *pNum1;
    *pNum1 = *pNum2;
    *pNum2 = temp;
}

void main()
{
    int num1 = 10;
    int num2 = -99;

    printf("num1 before: %d\n", num1);
    printf("num2 before: %d\n", num2);
    swap(&num1, &num2);

    printf("num1 before: %d\n", num1);
    printf("num2 before: %d\n", num2);
}