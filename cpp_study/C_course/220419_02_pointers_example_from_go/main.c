// example inspired by a course in go

#include <stdio.h>

void passByValue(int x)
{
    x++;
    printf("%d\n", x);
}

void passByReference(int *y)
{
    // *y++; // this will give the wrong answer...

    *y = *y + 1; // this works...
    // we can't use the abbreviation of *y++ in the case of pointers
    // in Go we can.

    printf("%d\n", *y);
}


void main()
{
    int x = 0;

    passByValue(x);

    printf("Global value: %d\n", x);

    passByReference(&x);

    printf("Global value: %d\n", x);
}