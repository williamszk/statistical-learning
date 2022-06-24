#include <stdio.h>
#include "../header.h"
#define LEN_ARR 2

void main()
{
    unsigned long largeIntA[LEN_ARR];
    unsigned long largeIntB[LEN_ARR];
    int output;
    int expectedAnswer;

    printf("\n// ================ Test 1 ========================//\n");
    printf("// Smaller\n");
    largeIntA[0] = 0x1000000000000000;
    largeIntA[1] = 0x0000000000000000;
    largeIntB[0] = 0x2000000000000000;
    largeIntB[1] = 0x0000000000000000;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    output = smallerLargeInt(largeIntA, largeIntB);

    printf("Result: \t");
    printf("%d\n", output);

    expectedAnswer = 1;
    printf("Expected: \t");
    printf("%d\n", expectedAnswer);

    printf("\n// ================ Test 2 ========================//\n");
    printf("// Smaller\n");
    largeIntA[0] = 0xF000000000000000;
    largeIntA[1] = 0x0000000000000000;
    largeIntB[0] = 0xA000000000000000;
    largeIntB[1] = 0x0000000000000000;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    output = smallerLargeInt(largeIntA, largeIntB);

    printf("Result: \t");
    printf("%d\n", output);

    expectedAnswer = 0;
    printf("Expected: \t");
    printf("%d\n", expectedAnswer);

    printf("\n// ================ Test 3 ========================//\n");
    printf("// Smaller\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x000000000000000A;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x000000000000000F;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    output = smallerLargeInt(largeIntA, largeIntB);

    printf("Result: \t");
    printf("%d\n", output);

    expectedAnswer = 1;
    printf("Expected: \t");
    printf("%d\n", expectedAnswer);

    printf("\n// ================ Test 4 ========================//\n");
    printf("// Smaller\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0xA000000000000000;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000000;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    output = smallerLargeInt(largeIntA, largeIntB);

    printf("Result: \t");
    printf("%d\n", output);

    expectedAnswer = 0;
    printf("Expected: \t");
    printf("%d\n", expectedAnswer);

    printf("\n// ================ Test 5 ========================//\n");
    printf("// Smaller\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0xAAAAAAAAAAAAAAA9;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0xAAAAAAAAAAAAAAAA;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    output = smallerLargeInt(largeIntA, largeIntB);

    printf("Result: \t");
    printf("%d\n", output);

    expectedAnswer = 1;
    printf("Expected: \t");
    printf("%d\n", expectedAnswer);

    printf("\n// ================ Test 6 ========================//\n");
    printf("// Smaller\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x0000000000000000;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000000;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    output = smallerLargeInt(largeIntA, largeIntB);

    printf("Result: \t");
    printf("%d\n", output);

    expectedAnswer = 0;
    printf("Expected: \t");
    printf("%d\n", expectedAnswer);

    printf("\n// ================ Test 7 ========================//\n");
    printf("// Greater\n");
    largeIntA[0] = 0x1000000000000000;
    largeIntA[1] = 0x0000000000000000;
    largeIntB[0] = 0x2000000000000000;
    largeIntB[1] = 0x0000000000000000;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    output = greaterLargeInt(largeIntA, largeIntB);

    printf("Result: \t");
    printf("%d\n", output);

    expectedAnswer = 0;
    printf("Expected: \t");
    printf("%d\n", expectedAnswer);

    printf("\n// ================ Test 8 ========================//\n");
    printf("// Greater\n");
    largeIntA[0] = 0xF000000000000000;
    largeIntA[1] = 0x0000000000000000;
    largeIntB[0] = 0xA000000000000000;
    largeIntB[1] = 0x0000000000000000;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    output = greaterLargeInt(largeIntA, largeIntB);

    printf("Result: \t");
    printf("%d\n", output);

    expectedAnswer = 1;
    printf("Expected: \t");
    printf("%d\n", expectedAnswer);

    printf("\n// ================ Test 9 ========================//\n");
    printf("// Greater\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0x000000000000000A;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x000000000000000F;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    output = greaterLargeInt(largeIntA, largeIntB);

    printf("Result: \t");
    printf("%d\n", output);

    expectedAnswer = 0;
    printf("Expected: \t");
    printf("%d\n", expectedAnswer);

    printf("\n// ================ Test 10 ========================//\n");
    printf("// Greater\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0xA000000000000000;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0x0000000000000000;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    output = greaterLargeInt(largeIntA, largeIntB);

    printf("Result: \t");
    printf("%d\n", output);

    expectedAnswer = 1;
    printf("Expected: \t");
    printf("%d\n", expectedAnswer);

    printf("\n// ================ Test 10 ========================//\n");
    printf("// Greater\n");
    largeIntA[0] = 0x0000000000000000;
    largeIntA[1] = 0xAAAAAAAAAAAAAAA9;
    largeIntB[0] = 0x0000000000000000;
    largeIntB[1] = 0xAAAAAAAAAAAAAAAA;

    printf("Input A: \t");
    printLargeInt(largeIntA);
    printf("Input B: \t");
    printLargeInt(largeIntB);

    output = greaterLargeInt(largeIntA, largeIntB);

    printf("Result: \t");
    printf("%d\n", output);

    expectedAnswer = 0;
    printf("Expected: \t");
    printf("%d\n", expectedAnswer);
}