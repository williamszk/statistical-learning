// furthermore is there a situation where we can declare the pointer
// without assigning nothing to it?

#include <stdio.h>

void main()
{
    int *ptrA;

    printf("%p\n", ptrA); // (nil)
    // printf("%d\n", ptrA); // this will give a warning and return 0
    printf("%d\n", *ptrA); // this will compile, but give this error: Segmentation fault (core dumped)
}

// this is interesting
// and it works