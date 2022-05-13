#include <stdio.h>

void print_u128(uint32_t *a)
{
    printf("0x%08x_%08x_%08x_%08x\n", a[3], a[2], a[1], a[0]);
}

void increment_u128(uint32_t *out, uint32_t *a)
{
    uint64_t sum;

    sum = (uint64_t)a[0] + 1;
    out[0] = (uint32_t)sum;

    for (int i = 1; i <= 3; i++)
    {
        sum = (uint64_t)a[i] + (uint64_t)(sum >> 32);
        out[i] = (uint32_t)sum;
    }
}

void not_operator_u128(uint32_t *out, uint32_t *a)
{
    for (int i = 0; i < 4; i++)
    {
        out[i] = ~a[i];
    }
}

void twos_complement_u128(uint32_t *out, uint32_t *a)
{
    uint32_t out_temp_1[5] = {0, 0, 0, 0, 0};

    not_operator_u128(out_temp_1, a);

    increment_u128(out, out_temp_1);
}

void add_u128(uint32_t *out, uint32_t *a, uint32_t *b)
{
    uint64_t sum;

    sum = (uint64_t)a[0] + (uint64_t)b[0];
    out[0] = (uint32_t)sum;

    sum = (uint64_t)a[1] + (uint64_t)b[1] + (uint64_t)(sum >> 32);
    out[1] = (uint32_t)sum;

    sum = (uint64_t)a[2] + (uint64_t)b[2] + (uint64_t)(sum >> 32);
    out[2] = (uint32_t)sum;

    sum = (uint64_t)a[3] + (uint64_t)b[3] + (uint64_t)(sum >> 32);
    out[3] = (uint32_t)sum;

    out[4] = (uint32_t)(sum >> 32);
}

/**
 * Decrement by 1 the 128 bit integer that is inserted as argument.
 * 
 * Decrement is just an example of subtraction.
 * We achieve this by using addition, and 2's complement.
*/
void decrement_u128(uint32_t *out, uint32_t *a)
{
    uint64_t sum;

    uint32_t a_temp_1[4] = {1, 0, 0, 0};
    uint32_t out_temp_1[5] = {0, 0, 0, 0, 0};

    twos_complement_u128(out_temp_1, a_temp_1);

    add_u128(out, a, out_temp_1);
}

// next step: 
// implement functions for comparison
// greater, lesser, equal and not equal
// then implement function for testing in "testing_module.c"
// include this testing function in all test_* files and 
// check if they respond with the expected answer