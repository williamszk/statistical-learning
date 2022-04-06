#include <stdio.h>


void main()
{
    int myNum = 'F';

    // if we print a char as int it will be converted according to the ascii table
    printf("%d\n", myNum); // 70

    printf("%d\n", 'A'); // 65
}