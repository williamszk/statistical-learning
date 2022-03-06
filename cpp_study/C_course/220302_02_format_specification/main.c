#include <stdio.h>

int main()
{
    printf("I am %d year old.\n", 20);
    printf("Today I am %d year old. But next year I'll be %d years old.\n", 20, 21);
    printf("My average grade is %f.\n", 87.9);

    // we can change the number of characters after the point
    printf("My average grade is %.1f.\n", 87.9);
    return 0;
}