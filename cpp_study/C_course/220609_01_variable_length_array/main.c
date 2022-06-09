/**
 * In this experiment we try to see if we can use a variable to declare the size of
 * an array.
 * In C89 standard we can't but in C99 we can.
 */

#include <stdio.h>

int main()
{
    int len = 10;

    int myArr[10] = {0};

    for (int i = 0; i < len; i++)
    {
        printf("%d\n", myArr[i]);
    }

    return 0;
}

// we can use a variable to determine the size of an array
// so maybe we are using C99

// let's try to compile this code with C89
// gcc -Wall main.c
// gcc -Wall -std=c89 main.c
// For sure we are using C99
// or even C11

// we got the following errors:
// main.c: In function ‘main’:
// main.c:15:5: error: ‘for’ loop initial declarations are only allowed in C99 or C11 mode
//    15 |     for (int i = 0; i < len; i++)
//       |     ^~~
// main.c:15:5: note: use option ‘-std=c99’, ‘-std=gnu99’, ‘-std=c11’ or ‘-std=gnu11’ to compile your code
// main.c: At top level:
// main.c:23:1: error: C++ style comments are not allowed in ISO C90
//    23 | // we can use a variable to determine the size of an array
//       | ^
// main.c:23:1: note: (this will be reported only once per input file)

// gcc -Wall -std=c11 main.c