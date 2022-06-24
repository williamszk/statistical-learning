#include <stdio.h>
#include "../header.h"
#define LEN_ARR 2

void main()
{
    unsigned long myLargeInt[LEN_ARR];
    unsigned long expectedAnswer[LEN_ARR];

    printf("\n// ================ Test 1 ========================//\n");
    myLargeInt[0] = 0x0000000000000001;
    myLargeInt[1] = 0x0000000000000000;

    printf("Input: \t\t");
    printLargeInt(myLargeInt);

    decrementLargeInt(myLargeInt);

    printf("Result: \t");
    printLargeInt(myLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0xFFFFFFFFFFFFFFFF;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 2 ========================//\n");
    myLargeInt[0] = 0x1000000000000000;
    myLargeInt[1] = 0x0000000000000003;

    printf("Input: \t\t");
    printLargeInt(myLargeInt);

    decrementLargeInt(myLargeInt);

    printf("Result: \t");
    printLargeInt(myLargeInt);

    expectedAnswer[0] = 0x1000000000000000;
    expectedAnswer[1] = 0x0000000000000002;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 3 ========================//\n");
    myLargeInt[0] = 0x1000000000000000;
    myLargeInt[1] = 0xFFFFFFFFFFFFFFFF;

    printf("Input: \t\t");
    printLargeInt(myLargeInt);

    decrementLargeInt(myLargeInt);

    printf("Result: \t");
    printLargeInt(myLargeInt);

    expectedAnswer[0] = 0x1000000000000000;
    expectedAnswer[1] = 0xFFFFFFFFFFFFFFFE;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 4 ========================//\n");
    printf("// An example of total underflow\n");
    myLargeInt[0] = 0x0000000000000000;
    myLargeInt[1] = 0x0000000000000000;

    printf("Input: \t\t");
    printLargeInt(myLargeInt);

    decrementLargeInt(myLargeInt);

    printf("Result: \t");
    printLargeInt(myLargeInt);

    expectedAnswer[0] = 0xFFFFFFFFFFFFFFFF;
    expectedAnswer[1] = 0xFFFFFFFFFFFFFFFF;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);
}