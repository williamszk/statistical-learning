#include <stdlib.h>
#include <stdio.h>
// defining null pointer

void g(int *ptr)
{
    ptr = malloc(4000);

    free(ptr);
}

void f(int *ptr1, int *ptr2)
{

    // if (ptr1 == 0)
    //     printf("B: ptr1 is a null pointer\n");

    ptr1 = malloc(2000);

    // if (ptr1 == 0)
    //     printf("C: ptr1 is a null pointer\n");
    // else
    //     printf("C: ptr1 is not a null pointer\n");

    g(ptr2);

    free(ptr1);
}

int main(void)
{
    int i;
    int *a[10];

    for (i = 0; i < 10; i++)
    {
        a[i] = malloc(1000);
    }

    int *p1 = 0;
    int *p2 = 0;
    int *p3 = 0;
    
    f(p1, p2);

    g(p3);

    for (i = 0; i < 10; i++)
    {
        free(a[i]);
    }

    if (p1 == 0)
        printf("A: p1 is a null pointer\n");

    free(p1);
    free(p2);
    free(p3);

    return 0;
}
