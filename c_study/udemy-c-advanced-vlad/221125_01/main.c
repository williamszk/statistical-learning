#include <stdio.h>

void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int main()
{
    int a = 18;
    int b = 23;

    printf("before: a=%d, b=%d\n", a, b);
    swap(&a, &b);
    printf("after: a=%d, b=%d\n", a, b);

    return 0;
}
