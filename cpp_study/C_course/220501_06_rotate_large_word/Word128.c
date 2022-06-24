#include <stdio.h>
#include "header.h"
#define LONG_SIZE 64
#define WORD128 128

void printWor128(Word128 arr)
{
    printf("0x%lX 0x%lX\n", arr.A0, arr.A1);
}

Word128 shiftLeftWord128(Word128 arr, int shift)
{
    Word128 arrOut;

    unsigned long newA0;
    unsigned long newA1;

    if (shift >= LONG_SIZE && shift < WORD128)
    {
        newA0 = arr.A1 << shift - LONG_SIZE;
        newA1 = 0x0;
    }
    else if (shift >= 0 && shift < LONG_SIZE)
    {
        newA0 = arr.A0 << shift | arr.A1 >> LONG_SIZE - shift;
        newA1 = arr.A1 << shift;
    } 

    arrOut.A0 = newA0;
    arrOut.A1 = newA1;

    return arrOut;
}

Word128 shiftRightWord128(Word128 arr, int shift)
{
    Word128 arrOut;
    unsigned long newA0;
    unsigned long newA1;

    if (shift >= LONG_SIZE && shift < WORD128)
    {
        newA0 = 0x0;
        newA1 = arr.A0 >> shift - LONG_SIZE;
    }
    else if (shift >= 0 && shift < LONG_SIZE)
    {
        newA0 = arr.A0 >> shift;
        newA1 = arr.A1 >> shift | arr.A0 << LONG_SIZE - shift;
    }

    arrOut.A0 = newA0;
    arrOut.A1 = newA1;

    return arrOut;
}

Word128 applyOrWord128(Word128 arrA, Word128 arrB)
{
    Word128 arrC;

    arrC.A0 = arrA.A0 | arrB.A0;
    arrC.A1 = arrA.A1 | arrB.A1;

    return arrC;
}

Word128 rotateLeftWord128(Word128 arr, int shift)
{
    Word128 arrA = shiftLeftWord128(arr, shift);

    Word128 arrB = shiftRightWord128(arr, WORD128 - shift);

    Word128 arrC = applyOrWord128(arrA, arrB);

    return arrC;
}