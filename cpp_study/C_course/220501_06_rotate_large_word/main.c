#include <stdio.h>
#include "header.h"

void main()
{
    printf("\n// ================ Experiment 1 ========================//\n");
    Word128 key01 = {
        .A0 = 0x000000000000000F,
        .A1 = 0xF000000000000000,
    };
    printf("Original: \t");
    printWor128(key01);

    Word128 key01out = shiftLeftWord128(key01, 3);
    printf("After: \t\t");
    printWor128(key01out);
    printf("Expected: \t0x7F 0x8000000000000000\n");

    printf("\n// ================ Experiment 2 ========================//\n");
    printf("// Experiment with shift right with large word (128 bits) //\n");
    Word128 key02 = {
        .A0 = 0x000000000000000F,
        .A1 = 0xF000000000000000,
    };
    printf("Original: \t");
    printWor128(key02);

    Word128 key02out = shiftRightWord128(key02, 1);
    printf("After: \t\t");
    printWor128(key02out);
    printf("Expected: \t0x7 0xF800000000000000\n");


    printf("\n// ================ Experiment 3 ========================//\n");
    Word128 key03 = {
        .A0 = 0x000000000000000F,
        .A1 = 0xF000000000000000,
    };
    printf("Original: \t");
    printWor128(key03);

    Word128 key03out = shiftRightWord128(key03, 4);
    printf("After: \t\t");
    printWor128(key03out);
    printf("Expected: \t0x0 0xFF00000000000000\n");

    printf("\n// ================ Experiment 4 ========================//\n");
    printf("// Experiment with OR operator with large word (128 bits) //\n");
    
    Word128 key04A = {
        .A0 = 0x0000000000000007,
        .A1 = 0x000000000000000C,
    };

    Word128 key04B = {
        .A0 = 0x0000000000000008,
        .A1 = 0x000000000000000C,
    };

    Word128 key04C = applyOrWord128(key04A, key04B);
    printf("Result: \t");
    printWor128(key04C);
    printf("Expected: \t0xF 0xC\n");


    printf("\n// ================ Experiment 5 ========================//\n");
    printf("// Experiment with OR operator with large word (128 bits) //\n");
    
    Word128 key05A = {
        .A0 = 0xA000000000000000,
        .A1 = 0x0000000000000003,
    };

    Word128 key05B = {
        .A0 = 0x8000000000000000,
        .A1 = 0x000000000000000A,
    };

    Word128 key05C = applyOrWord128(key05A, key05B);
    printf("Result: \t");
    printWor128(key05C);
    printf("Expected: \t0xA000000000000000 0xB\n");


    printf("\n// ================ Experiment 6 ========================//\n");
    Word128 key06 = {
        .A0 = 0xF000000000000000,
        .A1 = 0xF000000000000000,
    };
    printf("Original: \t");
    printWor128(key06);

    Word128 key06out = rotateLeftWord128(key06, 1);
    printf("After: \t\t");
    printWor128(key06out);
    printf("Expected: \t0xE000000000000001 0xE000000000000001\n");


    printf("\n// ================ Experiment 7 ========================//\n");
    Word128 key07 = {
        .A0 = 0xC000000000000000,
        .A1 = 0xF00000000000000F,
    };
    printf("Original: \t");
    printWor128(key07);

    Word128 key07out = rotateLeftWord128(key07, 1);
    printf("After: \t\t");
    printWor128(key07out);
    printf("Expected: \t0x8000000000000001 0xE00000000000001F\n");


    printf("\n// ================ Experiment 8 ========================//\n");
    printf("// Experiment with rotation (128 bits word) //\n");
    Word128 key08 = {
        .A0 = 0xC000000000000000,
        .A1 = 0xF00000000000000F,
    };
    printf("Original: \t");
    printWor128(key08);

    Word128 key08out = rotateLeftWord128(key08, 3);
    printf("After: \t\t");
    printWor128(key08out);
    printf("Expected: \t0x7 0x800000000000007E\n");


    printf("\n// ================ Experiment 9 ========================//\n");
    Word128 key09 = {
        .A0 = 0xC000000000000000,
        .A1 = 0xF00000000000000F,
    };
    printf("Original: \t");
    printWor128(key09);

    Word128 key09out = shiftRightWord128(key09, 127);
    printf("After: \t\t");
    printWor128(key09out);
    printf("Expected: \t0x0 0x1\n");

    printf("\n// ================ Experiment 10 ========================//\n");
    Word128 key10 = {
        .A0 = 0xC000000000000000,
        .A1 = 0xF00000000000000F,
    };
    printf("Original: \t");
    printWor128(key10);

    Word128 key10out = shiftLeftWord128(key10, 64);
    printf("After: \t\t");
    printWor128(key10out);
    printf("Expected: \t0xF00000000000000F 0x0\n");


    printf("\n// ================ Experiment 11 ========================//\n");
    Word128 key11 = {
        .A0 = 0xC000000000000000,
        .A1 = 0xF00000000000000F,
    };
    printf("Original: \t");
    printWor128(key11);

    Word128 key11out = shiftLeftWord128(key11, 63);
    printf("After: \t\t");
    printWor128(key11out);
    printf("Expected: \t0x7800000000000007 0x8000000000000000\n");

    printf("\n// ================ Experiment 12 ========================//\n");
    Word128 key12 = {
        .A0 = 0xC000000000000000,
        .A1 = 0xF00000000000000F,
    };
    printf("Original: \t");
    printWor128(key12);

    Word128 key12out = shiftLeftWord128(key12, 65);
    printf("After: \t\t");
    printWor128(key12out);
    printf("Expected: \t0xE00000000000001E 0x0\n");

    printf("\n// ================ Experiment 13 ========================//\n");
    Word128 key13 = {
        .A0 = 0xC000000000000000,
        .A1 = 0xF00000000000000F,
    };
    printf("Original: \t");
    printWor128(key13);

    Word128 key13out = shiftRightWord128(key13, 65);
    printf("After: \t\t");
    printWor128(key13out);
    printf("Expected: \t0x0 0x6000000000000000\n");

    printf("\n// ================ Experiment 14 ========================//\n");
    Word128 key14 = {
        .A0 = 0xF00000000000000F,
        .A1 = 0xF00000000000000F,
    };
    printf("Original: \t");
    printWor128(key14);

    Word128 key14out = shiftRightWord128(key14, 65);
    printf("After: \t\t");
    printWor128(key14out);
    printf("Expected: \t0x0 0x7800000000000007\n");

    printf("\n// ================ Experiment 15 ========================//\n");
    printf("// Experiment with rotation (128 bits word) //\n");
    Word128 key15 = {
        .A0 = 0xC000000000000000,
        .A1 = 0xF00000000000000F,
    };
    printf("Original: \t");
    printWor128(key15);

    Word128 key15out = rotateLeftWord128(key15, 1);
    printf("After: \t\t");
    printWor128(key15out);
    printf("Expected: \t0x8000000000000001 0xE00000000000001F\n");

}
