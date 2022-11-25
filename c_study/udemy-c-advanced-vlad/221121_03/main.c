#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(void)
{

    int grades[3] = {100, 80, 90};

    for (int i = 0; i < 3; i++)
    {
        printf("value: %d; addr: %p\n", grades[i], &grades[i]);
    }

    // pointer arithmetic

    printf("address of array: %p\n", grades); // it is the same as the &grades[0]

    printf("address of array+1: %p\n", grades + 1); // it will sum 4

    // we can loop through the addresses of the array using pointer arithmetic
    for (int i = 0; i < 3; i++)
    {
        printf("value: %d; addr: %p\n", *(grades + i), (grades + i));
        // the +1 will move the pointer in 4 positions
    }

    // What happens if we use float instead of int?
    // They move in 4 steps also
    puts("The case of Float:");
    float arr[3] = {1.2, 2.3, 3.4};
    for (int i = 0; i < 3; i++)
    {
        printf("value: %f; addr: %p\n", *(arr + i), (arr + i));
    }
    printf("Size of float: %d\n", sizeof(arr[0])); // 4

    // Let's try using the int64_t
    puts("The case of Int 64:");
    int64_t arr2[3] = {1, 2, 3};
    for (int i = 0; i < 3; i++)
    // value: 1; addr: 0xffffcbe0
    // value: 2; addr: 0xffffcbe8
    // value: 3; addr: 0xffffcbf0
    // They move in 8 slots 
    {
        printf("value: %d; addr: %p\n", *(arr2 + i), (arr2 + i));
    }
    printf("Size of int64_t: %d\n", sizeof(arr2[0])); // 8

    int a = 10;
    int *ptr;
    ptr = &a;
    printf("size of pointer: %ld\n", sizeof(ptr));

    return EXIT_SUCCESS;
}