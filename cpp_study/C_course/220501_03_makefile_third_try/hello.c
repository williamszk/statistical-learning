#include <stdio.h>
#include "header.h"
#include <unistd.h>

void hello()
{
    printf("\nI am in hello.c\n");
    printf("PID of hello.c is %d\n", getpid());
}