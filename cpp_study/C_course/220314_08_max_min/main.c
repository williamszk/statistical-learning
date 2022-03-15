// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203110#overview

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

    int max = num1;
    int min = num2;

    if (num1 < num2)
    {
        max = num2;
        min = num1;
    }
    if (max < num3){
        max = num3;
    }
    if (num3 < min){
        min = num3;
    }
    printf("%d is the largest and %d smallest\n", max, min);
}