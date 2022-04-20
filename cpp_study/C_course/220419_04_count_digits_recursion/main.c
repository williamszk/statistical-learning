// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20436713#overview

#include <stdio.h>

uint32_t countDigits(uint32_t n)
{
    if (n < 10) return 1;

    uint32_t remainder = n/10;

    return countDigits(remainder) + 1;
}

void main()
{
    printf("%d:\t%d\n", 32, countDigits(32));
    printf("%d:\t%d\n", 323, countDigits(324));
    printf("%d:\t%d\n", 4532, countDigits(4532));
    printf("%d:\t%d\n", 334562, countDigits(334562));
    printf("%d:\t%d\n", 3267842, countDigits(3267842));
}