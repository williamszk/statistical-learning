#include <stdio.h>
#include "../header.h"
#define LEN_ARR 2
#include <stdint.h>

void main()
{
    unsigned long largeIntA[LEN_ARR];
    unsigned long largeIntB[LEN_ARR];
    unsigned long outLargeInt[LEN_ARR];
    unsigned long expectedAnswer[LEN_ARR];

    printf("\n// ================ Test 1 ========================//\n");

    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x0000000000000000;

    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000000;

    printf("Input A: \t");
    printLargeInt(largeIntA);

    printf("Input B: \t");
    printLargeInt(largeIntB);

    addLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x0000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);


    printf("\n// ================ Test 2 ========================//\n");

    largeIntA[0] = 0xFFFFFFFFFFFFFFFF;
    largeIntA[1] = 0xFFFFFFFFFFFFFFFF;

    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000001;

    printf("Input A: \t");
    printLargeInt(largeIntA);

    printf("Input B: \t");
    printLargeInt(largeIntB);

    addLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x0000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);


    printf("\n// ================ Test 3 ========================//\n");

    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0xFFFFFFFFFFFFFFFF;

    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000001;

    printf("Input A: \t");
    printLargeInt(largeIntA);

    printf("Input B: \t");
    printLargeInt(largeIntB);

    addLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000001;
    expectedAnswer[1] = 0x0000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);


    printf("\n// ================ Test 4 ========================//\n");

    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0xFFFFFFFFFFFFFFFF;

    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000002;

    printf("Input A: \t");
    printLargeInt(largeIntA);

    printf("Input B: \t");
    printLargeInt(largeIntB);

    addLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000001;
    expectedAnswer[1] = 0x0000000000000001;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);




    printf("\n// ================ Test 5 ========================//\n");

    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x0000000000000001;

    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000001;

    printf("Input A: \t");
    printLargeInt(largeIntA);

    printf("Input B: \t");
    printLargeInt(largeIntB);

    addLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x0000000000000002;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 6 ========================//\n");

    largeIntA[0] = 0x0000000000000001;
    largeIntA[1] = 0x0000000000000001;

    largeIntB[0] = 0x0000000000000001;
    largeIntB[1] = 0x0000000000000001;

    printf("Input A: \t");
    printLargeInt(largeIntA);

    printf("Input B: \t");
    printLargeInt(largeIntB);

    addLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000002;
    expectedAnswer[1] = 0x0000000000000002;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 7 ========================//\n");

    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0xFFFFFFFFFFFFFFFF;

    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0xFFFFFFFFFFFFFFFF;

    printf("Input A: \t");
    printLargeInt(largeIntA);

    printf("Input B: \t");
    printLargeInt(largeIntB);

    addLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000001;
    expectedAnswer[1] = 0xFFFFFFFFFFFFFFFE;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

}