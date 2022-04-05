// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20620482#overview

#include <stdio.h>

void findMinMax(int num1, int num2, int *pMax, int *pMin)
{
    if (num1 > num2)
    {
        *pMax = num1;
        *pMin = num2;
    }
    else
    {
        *pMax = num2;
        *pMin = num1;
    }
}

void main()
{
    int num1 = 10, num2 = -98;
    int min, max;
    // int *pMin, *pMax;

    findMinMax(num1, num2, &min, &max);
    
    printf("Max = %d; Min = %d;\n", min, max);
}