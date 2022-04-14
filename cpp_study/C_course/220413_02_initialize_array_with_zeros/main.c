//
#include <stdio.h>

void main()
{
    int i;
    int arrStore[100] = {0}; // this will initialize all elements to 0
    // check this claim
    for (i = 0; i < 100; i++)
    {
        printf("%d - %d\n", i, arrStore[i]);
    }
    // verified it is true
}