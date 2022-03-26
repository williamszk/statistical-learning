// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203386#overview

#include <stdio.h>

void main()
{
    int myNum;
    printf("Write a number:\n");
    scanf("%d", &myNum);

    int numPow2 = myNum * myNum;
    int numPow3 = numPow2 * myNum;
    printf("\n%d^2 = %d\n%d^3 = %d\n", myNum, numPow2, myNum, numPow3);

}