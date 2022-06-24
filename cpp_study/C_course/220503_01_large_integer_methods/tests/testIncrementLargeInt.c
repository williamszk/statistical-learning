#include <stdio.h>
#include "../header.h"
#define LEN_ARR 2

void main()
{
    unsigned long myLargeInt[LEN_ARR];
    unsigned long expectedAnswer[LEN_ARR];

    printf("\n// ================ Test 1 ========================//\n");
    myLargeInt[0] = 0x0000000000000000;
    myLargeInt[1] = 0xFFFFFFFFFFFFFFFF;

    printf("Input: \t\t");
    printLargeInt(myLargeInt);

    incrementLargeInt(myLargeInt);

    printf("Result: \t");
    printLargeInt(myLargeInt);

    expectedAnswer[0] = 0x0000000000000001;
    expectedAnswer[1] = 0x0000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 2 ========================//\n");
    myLargeInt[0] = 0x0000000000000000;
    myLargeInt[1] = 0x0000000000000000;

    printf("Input: \t\t");
    printLargeInt(myLargeInt);

    incrementLargeInt(myLargeInt);

    printf("Result: \t");
    printLargeInt(myLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x0000000000000001;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 3 ========================//\n");
    myLargeInt[0] = 0x0000000000000000;
    myLargeInt[1] = 0xF000000000000000;

    printf("Input: \t\t");
    printLargeInt(myLargeInt);

    incrementLargeInt(myLargeInt);

    printf("Result: \t");
    printLargeInt(myLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0xF000000000000001;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 4 ========================//\n");
    myLargeInt[0] = 0x0000000000000000;
    myLargeInt[1] = 0x000000000000000F;

    printf("Input: \t\t");
    printLargeInt(myLargeInt);

    incrementLargeInt(myLargeInt);

    printf("Result: \t");
    printLargeInt(myLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x0000000000000010;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);


    printf("\n// ================ Test 5 ========================//\n");
    printf("// An example of total overflow\n");
    myLargeInt[0] = 0xFFFFFFFFFFFFFFFF;
    myLargeInt[1] = 0xFFFFFFFFFFFFFFFF;

    printf("Input: \t\t");
    printLargeInt(myLargeInt);

    incrementLargeInt(myLargeInt);

    printf("Result: \t");
    printLargeInt(myLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x0000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);
}
