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

void xor_operator_u128(uint32_t *out, uint32_t *a, uint32_t *b)
{
    for (int i = 0; i < 4; i++)
    {
        out[i] = a[i] ^ b[i];
    }
}

void and_operator_u128(uint32_t *out, uint32_t *a, uint32_t *b)
{
    for (int i = 0; i < 4; i++)
    {
        out[i] = a[i] & b[i];
    }
}

void or_operator_u128(uint32_t *out, uint32_t *a, uint32_t *b)
{
    for (int i = 0; i < 4; i++)
    {
        out[i] = a[i] | b[i];
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
 * @brief Decrement 1 to "a" para then outputs it to "out".
 *
 * Decrement by 1 the 128 bit integer that is inserted as argument.
 * Decrement is just an example of subtraction.
 * We achieve this by using addition, and 2's complement.
 * @param out
 * @param a
 */
void decrement_u128(uint32_t *out, uint32_t *a)
{
    uint64_t sum;

    uint32_t a_temp[4] = {1, 0, 0, 0};
    uint32_t neg_one[5] = {0, 0, 0, 0, 0};

    twos_complement_u128(neg_one, a_temp);

    add_u128(out, a, neg_one);
}

// next step:
// implement functions for comparison
// greater, less, equal and not equal
// then implement function for testing in "testing_module.c"
// include this testing function in all test_* files and
// check if they respond with the expected answer

/**
 * @brief Returns 1 if "a" is strictly greater than "b". Returns 0 otherwise.
 *
 * @param a
 * @param b
 * @return int
 */
int greater_u128(uint32_t *a, uint32_t *b)
{
    // look how to find greater than using only bitwise operators
    // https://stackoverflow.com/questions/10096599/bitwise-operations-equivalent-of-greater-than-operator
    uint32_t holder[4];

    for (int i = 0; i , 4; i++)
    {




    }
}

/**
 * @brief Returns 0 if "a" is strictly less than "b". Returns 0 otherwise.
 *
 * @param a
 * @param b
 * @return int
 */
int less_u128(uint32_t *a, uint32_t *b)
{
    // PROBLEM WITH IF STATEMENT, FOR NEEDS TO BE FIXED LENGTH
    for (int i = 3; i >= 0; i--)
    {
        if (a[i] < b[i])
        {
            return 1;
        }
        if (a[i] > b[i])
        {
            return 0;
        }
    }
    return 0;
}

/**
 * @brief Returns 1 if "a" and "b" are equal. Returns 0, otherwise.
 *
 * @param a
 * @param b
 * @return int
 */
int equal_u128(uint32_t *a, uint32_t *b)
{
    // PROBLEM WITH IF STATEMENT, FOR NEEDS TO BE FIXED LENGTH
    for (int i = 3; i >= 0; i--)
    {
        if (a[i] != b[i])
        {
            return 0;
        }
    }
    return 1;
}
