// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20350941?start=15#overview

#include <stdio.h>

void swap(int num1, int num2)
{
    int temp;
    temp = num1;
    num1 = num2;
    num2 = temp;
}

void main()
{
    int num1 = 10;
    int num2 = -88;

    printf("num1 before swap = %d\n", num1);
    printf("num2 before swap = %d\n", num2);

    printf("\n");
    swap(num1, num2);

    printf("num1 after swap = %d\n", num1);
    printf("num2 after swap = %d\n", num2);

    // actually it seems that nothing happens
    // this is so because in C arguments are passed as values
    // and not as reference like in Python
    // the way that we change the objects in memory for num1 and num2
    // is using pointers
}