#include <stdio.h>
#include "../header.h"
#define LEN_ARR 2

void main()
{
    unsigned long largeIntA[LEN_ARR];
    unsigned long largeIntB[LEN_ARR];
    unsigned long outLargeInt[LEN_ARR];
    unsigned long expectedAnswer[LEN_ARR];

    printf("\n// ================ Test 1 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x0000000000000015;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000002;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    divLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x000000000000002A;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);  

    printf("------------- !!! Wrong !!! -------------\n");
}