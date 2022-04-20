// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20350957#overview

#include <stdio.h>

uint32_t sumArithProgression(uint32_t n)
{
    if (n == 0)
        return 0;
    if (n == 1)
        return 1;

    return sumArithProgression(n - 1) + n;
}

void main()
{
    printf("%d:\t%d\n", 2, sumArithProgression(2));
    printf("%d:\t%d\n", 3, sumArithProgression(3));
    printf("%d:\t%d\n", 4, sumArithProgression(4));
    printf("%d:\t%d\n", 5, sumArithProgression(5));
    printf("%d:\t%d\n", 6, sumArithProgression(6)); // the argument is converted to uint32_t automatically
}