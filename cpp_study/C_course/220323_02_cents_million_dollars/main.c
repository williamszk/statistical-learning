// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20350929#overview

#include <stdio.h>

void main()
{
    long totalCents = 0;
    int totalDays = 30;

    long centsToGain = 1;
    
    for (int i = 1; i <= totalDays; i++)
    {
        printf("%d\n", totalCents);
        totalCents += centsToGain;
        centsToGain += centsToGain;
    }
}