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
    largeIntA[1] = 0x0000000000000005;

    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000002;

    printf("Input A: \t");
    printLargeInt(largeIntA);

    printf("Input B: \t");
    printLargeInt(largeIntB);

    andLogicalLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x0000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);    


    printf("\n// ================ Test 2 ========================//\n");

    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x000000A000000005;

    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x000000B000000002;

    printf("Input A: \t");
    printLargeInt(largeIntA);

    printf("Input B: \t");
    printLargeInt(largeIntB);

    andLogicalLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x000000A000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);  

    printf("\n// ================ Test 3 ========================//\n");

    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x0000000000000005;

    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000002;

    printf("Input A: \t");
    printLargeInt(largeIntA);

    printf("Input B: \t");
    printLargeInt(largeIntB);

    orLogicalLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x0000000000000007;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 4 ========================//\n");

    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x0000000000000005;

    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000002;

    printf("Input A: \t");
    printLargeInt(largeIntA);

    printf("Input B: \t");
    printLargeInt(largeIntB);

    xorLogicalLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x0000000000000007;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 5 ========================//\n");

    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x0000000000000005;

    printf("Input: \t\t");
    printLargeInt(largeIntA);

    notLogicalLargeInt(largeIntA);

    printf("Result: \t");
    printLargeInt(largeIntA);

    expectedAnswer[0] = 0xFFFFFFFFFFFFFFFF;
    expectedAnswer[1] = 0xFFFFFFFFFFFFFFFA;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);
}