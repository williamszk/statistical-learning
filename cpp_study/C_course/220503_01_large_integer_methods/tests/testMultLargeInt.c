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

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x000000000000002A;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 2 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x0000000000000015;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x000000000000000A;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x00000000000000D2;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 3 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x000000000000000F;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x000000000000000F;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x00000000000000E1;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 4 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x00000000000000FF;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x000000000000000F;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x0000000000000EF1;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 5 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x0000000000000FFF;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x000000000000000F;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x000000000000EFF1;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 6 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x000000000000FFFF;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x000000000000000F;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x00000000000EFFF1;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 7 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x000000000000000F;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x000000000000001F;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x00000000000001D1;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    // printf("------------- !!! Wrong !!! -------------\n");

    printf("\n// ================ Test 8 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0xF000000000000001;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000001;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0xF000000000000001;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 9 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x1111111111111111;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000002;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x2222222222222222;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 10 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x000000000000000A;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000FF2;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x0000000000009F74;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 11 ========================//\n");
    largeIntA[0] = 0x1000000000000000;
    largeIntA[1] = 0x0000000000000000;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000001;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x1000000000000000;
    expectedAnswer[1] = 0x0000000000000000;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 12 ========================//\n");
    largeIntA[0] = 0x1111111111111111;
    largeIntA[1] = 0x0000000000000000;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000002;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x2222222222222222;
    expectedAnswer[1] = 0x0000000000000000;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 13 ========================//\n");
    printf("// There is overflow\n");
    largeIntA[0] = 0xFFFFFFFFFFFFFFFF;
    largeIntA[1] = 0x0000000000000000;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000002;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0xFFFFFFFFFFFFFFFE;
    expectedAnswer[1] = 0x0000000000000000;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 14 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x0000000000000002;
    largeIntB[0] = 0x5555555555555555;
    largeIntB[1] = 0x0000000000000000;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0xAAAAAAAAAAAAAAAA;
    expectedAnswer[1] = 0x0000000000000000;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    // printf("------------- !!! Wrong !!! -------------\n");

    printf("\n// ================ Test 15 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0xF000000000000000;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000002;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000001;
    expectedAnswer[1] = 0xE000000000000000;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);


    printf("\n// ================ Test 16 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0xF000000000000000;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0xF000000000000000;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0xE100000000000000;
    expectedAnswer[1] = 0x0000000000000000;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 17 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x2000000000000000;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x1000000000000000;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0200000000000000;
    expectedAnswer[1] = 0x0000000000000000;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 18 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x2000000000000000;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000022;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000004;
    expectedAnswer[1] = 0x4000000000000000;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 19 ========================//\n");
    largeIntA[0] = 0x000000000000000A;
    largeIntA[1] = 0x0000000000000000;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000002;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x0000000000000014;
    expectedAnswer[1] = 0x0000000000000000;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 20 ========================//\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x0000000000000002;
    largeIntB[0] = 0x0AAA000000000000;
    largeIntB[1] = 0x0000000000000000;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x1554000000000000;
    expectedAnswer[1] = 0x0000000000000000;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    // printf("------------- !!! Wrong !!! -------------\n");

    printf("\n// ================ Test 21 ========================//\n");
    printf("// The is overflow\n");
    largeIntA[0] = 0x000000000000000A;
    largeIntA[1] = 0x000000000000000A;
    largeIntB[0] = 0x000000000000000A;
    largeIntB[1] = 0x000000000000000A;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x00000000000000C8;
    expectedAnswer[1] = 0x0000000000000064;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    // printf("------------- !!! Wrong !!! -------------\n");

    printf("\n// ================ Test 22 ========================//\n");
    printf("// The is overflow\n");
    largeIntA[0] = 0x0AAA000000000000;
    largeIntA[1] = 0x000000000000000A;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x000000000000000A;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    multLargeInt(largeIntA, largeIntB, outLargeInt);

    printf("Result: \t");
    printLargeInt(outLargeInt);

    expectedAnswer[0] = 0x6AA4000000000000;
    expectedAnswer[1] = 0x0000000000000064;
    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    // printf("------------- !!! Wrong !!! -------------\n");
}