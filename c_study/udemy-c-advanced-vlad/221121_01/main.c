#include <stdio.h>

int main()
{
    int grade1 = 80;
    int grade2 = 100;

    printf("grade1 value: %d; addr: %p\n", grade1, &grade1);
    printf("grade2 value: %d; addr: %p\n", grade2, &grade2);

    return 0;
}