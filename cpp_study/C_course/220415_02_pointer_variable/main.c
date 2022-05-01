
#include <stdio.h>

void main()
{
    int x = 2;

    int *a = &x;
    int *b = &x;

    printf("*a: %d\t*b: %d\n", *a, *b);

    *b = 99;
    printf("*a: %d\t*b: %d\n", *a, *b);
}