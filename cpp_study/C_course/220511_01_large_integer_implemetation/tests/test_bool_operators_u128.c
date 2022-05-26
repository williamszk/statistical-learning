#include <stdio.h>
#include <stdint.h>
#include "large_integer.h"
#include "testing.h"

/**
 * Resets to zero all values of the array out.
 *
 * It is so that we can use it in the next test.
 */
void reset_out(uint32_t *out)
{
    out[0] = 0;
    out[1] = 0;
    out[2] = 0;
    out[3] = 0;
    out[4] = 0;
}

int main()
{
    uint32_t a[4];
    uint32_t b[4];
    uint32_t out[5];
    uint32_t expected[4];

    printf("\n// ==== Tests for Not Operator ==== //\n");

    printf("1. \t");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    reset_out(out);

    not_operator_u128(out, a);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    test_u128(out, expected);

    printf("2. \t");
    a[0] = 0x00000001;
    a[1] = 0x00000001;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    reset_out(out);

    not_operator_u128(out, a);

    expected[0] = 0xfffffffe;
    expected[1] = 0xfffffffe;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    test_u128(out, expected);

    printf("\n// ==== Tests for XOR Operator ==== //\n");

    // ================================================== //
    printf("1. \t");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    xor_operator_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    // ================================================== //
    printf("2. \t");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    xor_operator_u128(out, a, b);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    // ================================================== //
    printf("3. \t");
    a[0] = 0x000000f1;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    xor_operator_u128(out, a, b);

    expected[0] = 0x000000f0;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    // ================================================== //
    printf("4. \t");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0xffffffff;
    b[3] = 0xfffffff1;

    reset_out(out);

    xor_operator_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x0000000e;

    test_u128(out, expected);

    printf("\n// ==== Tests for AND opeartor ==== //\n");

    // ================================================== //
    printf("1. \t");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    and_operator_u128(out, a, b);

    expected[0] = 0xffffffff;
    expected[1] = 0xffffffff;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    // ================================================== //
    printf("2. \t");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    and_operator_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    // ================================================== //
    printf("3. \t");
    a[0] = 0x000000f1;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    and_operator_u128(out, a, b);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    // ================================================== //
    printf("4. \t");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0xffffffff;
    b[3] = 0xfffffff1;

    reset_out(out);

    and_operator_u128(out, a, b);

    expected[0] = 0xffffffff;
    expected[1] = 0xffffffff;
    expected[2] = 0xffffffff;
    expected[3] = 0xfffffff1;

    test_u128(out, expected);

    printf("\n// ==== Tests for OR opeartor ==== //\n");

    // ================================================== //
    printf("1. \t");

    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    or_operator_u128(out, a, b);

    expected[0] = 0xffffffff;
    expected[1] = 0xffffffff;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    // ================================================== //
    printf("2. \t");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    or_operator_u128(out, a, b);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    // ================================================== //
    printf("3. \t");
    a[0] = 0x000000f1;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    or_operator_u128(out, a, b);

    expected[0] = 0x000000f1;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    // ================================================== //
    printf("4. \t");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0xffffffff;
    b[3] = 0xfffffff1;

    reset_out(out);

    or_operator_u128(out, a, b);

    expected[0] = 0xffffffff;
    expected[1] = 0xffffffff;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    test_u128(out, expected);

    return 0;
}
