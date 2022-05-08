#include <stdio.h>
#define LEN_ARR 2
#define LONG_SIZE 64
#define WORD_SIZE 128
#define HEX_SIZE 4
#define QTD_HEX_LONG 16

void printLargeInt(unsigned long *largeInt)
{
    printf("0x%016lX 0x%016lX\n", largeInt[0], largeInt[1]);
    // in 016, 16 means that we want at least 16 chars, and
    // complete with 0s
}

void incrementLargeInt(unsigned long *largeInt)
{
    unsigned long result = largeInt[1] + 0x0000000000000001;

    if (result < largeInt[1])
        largeInt[0] += 0x0000000000000001;

    largeInt[1] = result;
}

void decrementLargeInt(unsigned long *largeInt)
{
    unsigned long result = largeInt[1] - 0x0000000000000001;

    if (result > largeInt[1]) // we had underflow
        largeInt[0] -= 0x0000000000000001;

    largeInt[1] = result;

    // printf("Ran here! 0x%016lX\n", largeInt[1] - 0x0000000000000001);
}

/**
 * Implicitly changes the values of `outLargeInt` to include the sum of `largeIntA` and `largeIntB`.
 */
void addLargeInt(unsigned long *largeIntA, unsigned long *largeIntB, unsigned long *outLargeInt)
{
    unsigned long result0 = largeIntA[0] + largeIntB[0];
    unsigned long result1 = largeIntA[1] + largeIntB[1];

    if (result1 < largeIntA[1] || result1 < largeIntB[1])
    { // num1 is overflown
        result0 += 0x0000000000000001;
    }

    outLargeInt[0] = result0;
    outLargeInt[1] = result1;
}

void subLargeInt(unsigned long *largeIntA, unsigned long *largeIntB, unsigned long *outLargeInt)
{
    unsigned long result0 = largeIntA[0] - largeIntB[0];
    unsigned long result1 = largeIntA[1] - largeIntB[1];

    if (result1 > largeIntA[1])
    { // num1 is overflown
        result0 -= 0x0000000000000001;
    }

    outLargeInt[0] = result0;
    outLargeInt[1] = result1;
}

void andLogicalLargeInt(unsigned long *largeIntA, unsigned long *largeIntB, unsigned long *outLargeInt)
{
    unsigned long result0 = largeIntA[0] & largeIntB[0];
    unsigned long result1 = largeIntA[1] & largeIntB[1];

    outLargeInt[0] = result0;
    outLargeInt[1] = result1;
}

void orLogicalLargeInt(unsigned long *largeIntA, unsigned long *largeIntB, unsigned long *outLargeInt)
{
    unsigned long result0 = largeIntA[0] | largeIntB[0];
    unsigned long result1 = largeIntA[1] | largeIntB[1];

    outLargeInt[0] = result0;
    outLargeInt[1] = result1;
}

void xorLogicalLargeInt(unsigned long *largeIntA, unsigned long *largeIntB, unsigned long *outLargeInt)
{
    unsigned long result0 = largeIntA[0] ^ largeIntB[0];
    unsigned long result1 = largeIntA[1] ^ largeIntB[1];

    outLargeInt[0] = result0;
    outLargeInt[1] = result1;
}

void notLogicalLargeInt(unsigned long *largeInt)
{
    largeInt[0] = ~largeInt[0];
    largeInt[1] = ~largeInt[1];
}

void leftShiftLargeInt(unsigned long *outLargeInt, unsigned int shift)
{
    unsigned long newLargeInt0;
    unsigned long newLargeInt1;

    if (shift >= LONG_SIZE && shift < WORD_SIZE)
    {
        newLargeInt0 = outLargeInt[1] << shift - LONG_SIZE;
        newLargeInt1 = 0x0000000000000000;
    }
    else if (shift > 0 && shift < LONG_SIZE)
    {
        newLargeInt0 = outLargeInt[0] << shift | outLargeInt[1] >> LONG_SIZE - shift;
        newLargeInt1 = outLargeInt[1] << shift;
    }
    else if (shift == 0)
    {
        newLargeInt0 = outLargeInt[0];
        newLargeInt1 = outLargeInt[1];
    }

    outLargeInt[0] = newLargeInt0;
    outLargeInt[1] = newLargeInt1;
}

void rightShiftLargeInt(unsigned long *outLargeInt, unsigned int shift)
{
    unsigned long newLargeInt0;
    unsigned long newLargeInt1;

    if (shift >= LONG_SIZE && shift < WORD_SIZE)
    {
        newLargeInt0 = 0x0000000000000000;
        newLargeInt1 = outLargeInt[0] >> shift - LONG_SIZE;
    }
    else if (shift > 0 && shift < LONG_SIZE)
    {
        newLargeInt0 = outLargeInt[0] >> shift;
        newLargeInt1 = outLargeInt[1] >> shift | outLargeInt[0] << LONG_SIZE - shift;
    }
    else if (shift == 0)
    {
        newLargeInt0 = outLargeInt[0];
        newLargeInt1 = outLargeInt[1];
    }

    outLargeInt[0] = newLargeInt0;
    outLargeInt[1] = newLargeInt1;
}

/**
 * Returns 1 if `largeIntA` is smaller than `largeIntB`, 0 otherwise.
 */
int smallerLargeInt(unsigned long *largeIntA, unsigned long *largeIntB)
{
    if (largeIntA[0] < largeIntB[0])
        return 1;
    else if (largeIntA[0] == 0 && largeIntB[0] == 0)
        if (largeIntA[1] < largeIntB[1])
            return 1;
        else
            return 0;
    else
        return 0;
}

/**
 * Returns 1 if `largeIntA` is greater than `largeIntB`, 0 otherwise.
 */
int greaterLargeInt(unsigned long *largeIntA, unsigned long *largeIntB)
{
    if (largeIntA[0] > largeIntB[0])
        return 1;
    else if (largeIntA[0] == 0 && largeIntB[0] == 0)
        if (largeIntA[1] > largeIntB[1])
            return 1;
        else
            return 0;
    else
        return 0;
}

// equalLargeInt()

// notEqualLargeInt()

/**
 * Multiplies two large integers.
 *
 * For this implementation we can imagine that we have the following structure:
 *
 *      array A  ----------------(a), ----------------(b)
 *      array B  ----------------(c), ----------------(d)
 *
 * Each array is a large integer. Those arrays have 2 elements, where each element
 * is a unsingned long integer.
 *
 * In our implementation, we divide the calculation in 4 phases:
 * 1. (d) * (b), for this we need to make bit shift operations
 * 2. (d) * (a)
 * 3. (c) * (b)
 * 4. (a) * (c)
 *
 * For the phase 4. (a)*(c) we do not implement because they will gerate overflow values.
 * For (d) * (b), we need to implement bit shift operations to account for possible overflows.
 * Phase (d) * (a) and (c) * (b) are relatively similar, and they do not use bit shift operations
 * because if any overflow that happens in this phase cannot be solved by the multiplication
 * algorithm.
 *
 */
void multLargeInt(unsigned long *largeIntA, unsigned long *largeIntB, unsigned long *outLargeInt)
{
    int i, j;
    unsigned int shift;

    unsigned long holderM[LEN_ARR] = {
        0x0000000000000000,
        0x0000000000000000,
    };

    unsigned long holderN[LEN_ARR] = {
        0x0000000000000000,
        0x0000000000000000,
    };

    unsigned long selectorJ[LEN_ARR];
    unsigned long selectorK[LEN_ARR];
    unsigned long holderA[LEN_ARR];
    unsigned long holderB[LEN_ARR];

    // phase 1 (b) * (d)
    for (i = 0; i < QTD_HEX_LONG; i++)
    {
        if (i == 0)
        {
            shift = 0;
            selectorK[0] = 0x0000000000000000;
            selectorK[1] = 0x000000000000000F;
        }
        else
            shift = HEX_SIZE;

        leftShiftLargeInt(selectorK, shift);

        andLogicalLargeInt(largeIntB, selectorK, holderB);

        for (j = 0; j < QTD_HEX_LONG; j++)
        {
            if (j == 0)
            {
                shift = 0;
                selectorJ[0] = 0x0000000000000000;
                selectorJ[1] = 0x000000000000000F;
            }
            else
                shift = HEX_SIZE;

            leftShiftLargeInt(selectorJ, shift);

            andLogicalLargeInt(largeIntA, selectorJ, holderA);

            // this is used to make the numbers go to the left
            // e.g.: 0F00 -> 000F
            // we use this to safeguard from overflow (later we shift left again)
            rightShiftLargeInt(holderA, HEX_SIZE * j);
            rightShiftLargeInt(holderB, HEX_SIZE * i);

            holderN[0] = 0x0000000000000000;
            holderN[1] = 0x0000000000000000;

            holderN[1] = holderA[1] * holderB[1];

            leftShiftLargeInt(holderB, HEX_SIZE * i);

            // returning to he left
            // initial: 0F00 000F
            // apply shift left on both numbers
            // 000F * 000F = 00E1
            // then shift right by the correct amount
            // 00E1 -> E100
            // hence: 0F00 000F = E100
            leftShiftLargeInt(holderN, HEX_SIZE * (j + i));

            addLargeInt(holderM, holderN, holderM);
        }
    }

    // phase 2 (a) * (d)  and phase 3 (c) * (b)
    for (int phase = 2; phase <= 3; phase++)
    {
        for (i = 0; i < QTD_HEX_LONG; i++)
        {
            if (i == 0)
            {
                shift = 0;
                if (phase == 2)
                {
                    selectorK[0] = 0x0000000000000000;
                    selectorK[1] = 0x000000000000000F;
                }
                else if (phase == 3)
                {
                    selectorK[0] = 0x000000000000000F;
                    selectorK[1] = 0x0000000000000000;
                }
            }
            else
                shift = HEX_SIZE;

            leftShiftLargeInt(selectorK, shift);

            andLogicalLargeInt(largeIntB, selectorK, holderB);

            for (j = 0; j < QTD_HEX_LONG; j++)
            {
                if (j == 0)
                {
                    shift = 0;

                    if (phase == 2)
                    {
                        selectorJ[0] = 0x000000000000000F;
                        selectorJ[1] = 0x0000000000000000;
                    }
                    else if (phase == 3)
                    {
                        selectorJ[0] = 0x0000000000000000;
                        selectorJ[1] = 0x000000000000000F;
                    }
                }
                else
                    shift = HEX_SIZE;

                leftShiftLargeInt(selectorJ, shift);

                andLogicalLargeInt(largeIntA, selectorJ, holderA);

                holderN[0] = 0x0000000000000000;
                holderN[1] = 0x0000000000000000;

                if (phase == 2)
                {
                    holderN[0] = holderA[0] * holderB[1];
                }
                else if (phase == 3)
                {
                    holderN[0] = holderA[1] * holderB[0];
                }

                addLargeInt(holderM, holderN, holderM);
            }
        }
    }

    outLargeInt[0] = holderM[0];
    outLargeInt[1] = holderM[1];
}

void divLargeInt(unsigned long *largeIntA, unsigned long *largeIntB, unsigned long *outLargeInt)
{
    // the numerator must be greater than the denominator
    // otherwise the division is not possible
    if (smallerLargeInt(largeIntA, largeIntB))
    {
        outLargeInt[0] = 0;
        outLargeInt[1] = 0;
    } 
    else
    {

        


    }
}

// leftRotateLargeInt()

// rightRotateLargeInt()

// moduloLargeInt()

// euclideanAlgoLargeInt()

// gcdLargeInt()

