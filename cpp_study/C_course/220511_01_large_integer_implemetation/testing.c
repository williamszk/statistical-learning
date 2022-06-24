/**
 * The purpose of this module is to declare functions that will
 * be used for testing.
 * It needs to receive the observed result and the expected result.
 */

#include <stdio.h>
#include <stdint.h>

/**
 * @brief Compares two 128 bit integers and prints "."
 * otherwise prints "F".
 *
 * @param result A 128 bit vector integer of the obtained result.
 * @param expected A 128 bit vector of the expected result.
 */
void test_u128(uint32_t *result, uint32_t *expected)
{

    int holder = 1;

    int i;
    for (int i = 0; i < 4; i++)
    {
        holder *= result[i] == expected[i];
    }
    if (holder)
        printf(".");
    else
        printf("F");
    printf("\n");
    // given that this will not be used for the crypto system per se
    // we can use conditional statements
}

void test_int_u128(int result, int expected)
{
    if (result == expected)
        printf(".");
    else
        printf("F");
    printf("\n");
}
