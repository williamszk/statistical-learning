#include <stdio.h>
#include "header.h"

void main()
{
    printf("\nI am in main.c\n");
    printf("\nCalling hello function");
    hello();
    printf("\nCalling add function\n");
    add(3,5);
    printf("\nBack in main.c\n");
}