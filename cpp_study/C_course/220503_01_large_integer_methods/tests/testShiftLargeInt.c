#include <stdio.h>
#include "../header.h"
#define LEN_ARR 2

void main()
{
    unsigned long largeInt[LEN_ARR];
    unsigned int shift;
    unsigned long outLargeInt[LEN_ARR];
    unsigned long expectedAnswer[LEN_ARR];

    printf("\n// ================ Test 1 ========================//\n");

    largeInt[0] = 0x0000000000000000;
    largeInt[1] = 0x0000000000000005;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    leftShiftLargeInt(largeInt, 1);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x000000000000000A;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 2 ========================//\n");

    largeInt[0] = 0x0000000000000000;
    largeInt[1] = 0xF000000000000000;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    leftShiftLargeInt(largeInt, 1);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0x0000000000000001;
    expectedAnswer[1] = 0xE000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 3 ========================//\n");

    largeInt[0] = 0x0000000000000000;
    largeInt[1] = 0xF000000000000000;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    leftShiftLargeInt(largeInt, 2);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0x0000000000000003;
    expectedAnswer[1] = 0xC000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 4 ========================//\n");

    largeInt[0] = 0x0000000000000000;
    largeInt[1] = 0xF000000000000000;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    leftShiftLargeInt(largeInt, 3);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0x0000000000000007;
    expectedAnswer[1] = 0x8000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 5 ========================//\n");

    largeInt[0] = 0x000000000000000F;
    largeInt[1] = 0xF000000000000000;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    leftShiftLargeInt(largeInt, 1);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0x000000000000001F;
    expectedAnswer[1] = 0xE000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 6 ========================//\n");

    largeInt[0] = 0x000000000000000F;
    largeInt[1] = 0xF000000000000000;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    leftShiftLargeInt(largeInt, 3);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0x000000000000007F;
    expectedAnswer[1] = 0x8000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 7 ========================//\n");

    largeInt[0] = 0xC000000000000000;
    largeInt[1] = 0xF00000000000000F;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    leftShiftLargeInt(largeInt, 64);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0xF00000000000000F;
    expectedAnswer[1] = 0x0000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 8 ========================//\n");

    largeInt[0] = 0xC000000000000000;
    largeInt[1] = 0xF00000000000000F;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    leftShiftLargeInt(largeInt, 63);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0x7800000000000007;
    expectedAnswer[1] = 0x8000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 9 ========================//\n");

    largeInt[0] = 0xC000000000000000;
    largeInt[1] = 0xF00000000000000F;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    leftShiftLargeInt(largeInt, 65);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0xE00000000000001E;
    expectedAnswer[1] = 0x0000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);


    printf("\n// ================ Test 10 ========================//\n");

    largeInt[0] = 0x000000000000000F;
    largeInt[1] = 0xF000000000000000;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    rightShiftLargeInt(largeInt, 1);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0x0000000000000007;
    expectedAnswer[1] = 0xF800000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 11 ========================//\n");

    largeInt[0] = 0x000000000000000F;
    largeInt[1] = 0xF000000000000000;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    rightShiftLargeInt(largeInt, 4);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0xFF00000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);


    printf("\n// ================ Test 12 ========================//\n");

    largeInt[0] = 0xC000000000000000;
    largeInt[1] = 0xF00000000000000F;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    rightShiftLargeInt(largeInt, 127);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x0000000000000001;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 13 ========================//\n");

    largeInt[0] = 0xC000000000000000;
    largeInt[1] = 0xF00000000000000F;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    rightShiftLargeInt(largeInt, 65);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x6000000000000000;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 14 ========================//\n");

    largeInt[0] = 0xF00000000000000F;
    largeInt[1] = 0xF00000000000000F;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    rightShiftLargeInt(largeInt, 65);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0x0000000000000000;
    expectedAnswer[1] = 0x7800000000000007;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 15 ========================//\n");

    largeInt[0] = 0xF000000000000001;
    largeInt[1] = 0xF00000000000000F;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    leftShiftLargeInt(largeInt, 0);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0xF000000000000001;
    expectedAnswer[1] = 0xF00000000000000F;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

    printf("\n// ================ Test 16 ========================//\n");

    largeInt[0] = 0xFB00000000000001;
    largeInt[1] = 0xF0000000000000AF;

    printf("Input: \t\t");
    printLargeInt(largeInt);

    rightShiftLargeInt(largeInt, 0);

    printf("Result: \t");
    printLargeInt(largeInt);

    expectedAnswer[0] = 0xFB00000000000001;
    expectedAnswer[1] = 0xF0000000000000AF;

    printf("Expected: \t");
    printLargeInt(expectedAnswer);

}