#include <stdio.h>
#define LONG_SIZE 64

typedef struct word128{
    unsigned long A0;
    unsigned long A1;
} Word128;

Word128 shiftLeftWord128(Word128 arr, int shift)
{
    Word128 arrOut;

    unsigned long newA0 = arr.A0 << shift | arr.A1 >> LONG_SIZE - shift;
    unsigned long newA1 = arr.A1 << shift;
    
    arrOut.A0 = newA0;
    arrOut.A1 = newA1;

    return arrOut;
}

void printWor128(Word128 arr)
{
    printf("0x%lX 0x%lX\n", arr.A0, arr.A1);
}

void main()
{

    printf("\n// ================ Experiment 1 ========================//\n");
    Word128 key01 = {
        .A0 = 0x0000000000000000,
        .A1 = 0xF000000000000000,
    };
    printf("Original: \t");
    printWor128(key01);

    Word128 key01out = shiftLeftWord128(key01, 1);
    printf("After: \t\t");
    printWor128(key01out);
    printf("Expected: \t0x1 0xE000000000000000\n");

    printf("\n// ================ Experiment 2 ========================//\n");
    Word128 key02 = {
        .A0 = 0x0000000000000000,
        .A1 = 0xF000000000000000,
    };
    printf("Original: \t");
    printWor128(key02);

    Word128 key02out = shiftLeftWord128(key02, 2);
    printf("After: \t\t");
    printWor128(key02out);
    printf("Expected: \t0x3 0xC000000000000000\n");


    printf("\n// ================ Experiment 3 ========================//\n");
    Word128 key03 = {
        .A0 = 0x0000000000000000,
        .A1 = 0xF000000000000000,
    };
    printf("Original: \t");
    printWor128(key03);

    Word128 key03out = shiftLeftWord128(key03, 3);
    printf("After: \t\t");
    printWor128(key03out);
    printf("Expected: \t0x7 0x8000000000000000\n");

    printf("\n// ================ Experiment 4 ========================//\n");
    Word128 key04 = {
        .A0 = 0x000000000000000F,
        .A1 = 0xF000000000000000,
    };
    printf("Original: \t");
    printWor128(key04);

    Word128 key04out = shiftLeftWord128(key04, 1);
    printf("After: \t\t");
    printWor128(key04out);
    printf("Expected: \t0x1F 0xE000000000000000\n");

    printf("\n// ================ Experiment 5 ========================//\n");
    Word128 key05 = {
        .A0 = 0x000000000000000F,
        .A1 = 0xF000000000000000,
    };
    printf("Original: \t");
    printWor128(key05);

    Word128 key05out = shiftLeftWord128(key05, 3);
    printf("After: \t\t");
    printWor128(key05out);
    printf("Expected: \t0x7F 0x8000000000000000\n");

}