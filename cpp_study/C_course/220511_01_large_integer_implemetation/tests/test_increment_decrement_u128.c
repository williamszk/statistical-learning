#include <stdio.h>
#include <stdint.h>
#include "large_integer.h"

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
    uint32_t out[5];
    uint32_t expected[4];

    printf("\n// ================ Tests for Increment ========================//\n");

    printf("\n// ================ Test A.1 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    increment_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000001;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test A.2 ========================//\n");

    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    increment_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test A.3 ========================//\n");

    a[0] = 0x00000000;
    a[1] = 0xf0000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    increment_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000001;
    expected[1] = 0xf0000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test A.4 ========================//\n");

    a[0] = 0x0000000f;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    increment_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000010;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test A.5 ========================//\n");
    printf("// An example of total overflow\n");

    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    increment_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Tests for Two's Complement ========================//\n");

    printf("\n// ================ Test B.1 ========================//\n");

    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000001;
    a[3] = 0x00000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    twos_complement_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    printf("Expected: \t");
    print_u128(expected);

    // printf("// Wrong answer\n");

    printf("\n// ================ Test B.2 ========================//\n");

    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    twos_complement_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    // printf("// Wrong answer\n");

    printf("\n// ================ Test B.3 ========================//\n");

    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    twos_complement_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xffffffff;
    expected[1] = 0xffffffff;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    printf("Expected: \t");
    print_u128(expected);

    // printf("// Wrong answer\n");

    printf("\n// ================ Tests for Decrement ========================//\n");

    printf("\n// ================ Test C.1 ========================//\n");

    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000001;
    a[3] = 0x00000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    decrement_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xffffffff;
    expected[1] = 0xffffffff;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    // printf("// Wrong answer\n");

    printf("\n// ================ Test C.2 ========================//\n");
    printf("// There should be underflow\n");

    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    decrement_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xffffffff;
    expected[1] = 0xffffffff;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    printf("Expected: \t");
    print_u128(expected);

    // printf("// Wrong answer\n");

    printf("\n// ================ Test C.2 ========================//\n");
    printf("// There should be underflow\n");

    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    decrement_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xffffffff;
    expected[1] = 0xffffffff;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test C.3 ========================//\n");

    a[0] = 0x00000003;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x10000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    decrement_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xffffffff;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x10000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test C.4 ========================//\n");
    // printf("// There should be underflow\n");

    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x10000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    decrement_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xfffffffe;
    expected[1] = 0xffffffff;
    expected[2] = 0x00000000;
    expected[3] = 0x10000000;

    printf("Expected: \t");
    print_u128(expected);

    return 0;
}
