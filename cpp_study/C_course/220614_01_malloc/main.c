
// https://www.youtube.com/watch?v=SuBch2MZpZM&ab_channel=Log2Base2

#include <stdio.h>
#include <stdlib.h>

int main()
{

    int *ptr;

    // when we declare a int *ptr without assignment
    // what is inside of it?
    //
    *ptr; // strangely this does not give a segfault
    // printf("*ptr = %d\n", *ptr); // this gives segfault
    // check if the pointer it not a null pointer
    // if (*ptr != 0)
    //     printf("*ptr = %d\n", *ptr);  // this will also give segfault

    ptr = malloc(5 * sizeof(int));

    // *(ptr + 1)

    printf("*(ptr) = %d\n", *(ptr));
    printf("before assignment: *(ptr + 1) = %d\n", *(ptr + 1));
    *(ptr + 1) = 10;
    printf("after assignment: *(ptr + 1) = %d\n", *(ptr + 1));

    *(ptr + 2) = 20;
    *(ptr + 3) = 30;
    *(ptr + 4) = 40;
    *(ptr + 5) = 50;

    printf("(ptr + 5) = 0x%X\n", (ptr + 5));
    *(ptr + 6);

    printf("*(ptr + 6) = %d\n", *(ptr + 6));

    printf("(ptr + 6) = 0x%X\n", (ptr + 6));

    *(ptr + 6) = 60;

    printf("After asignment: *(ptr + 6) = %d\n", *(ptr + 6));

    return 0;
}
