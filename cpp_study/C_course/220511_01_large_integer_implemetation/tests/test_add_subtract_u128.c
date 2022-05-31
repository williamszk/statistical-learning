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
    uint32_t b[4];
    uint32_t out[5];
    uint32_t expected[4];

    printf("\n// ================ Tests for Addition ========================//\n");

    printf("\n// ================ Test A.1 ========================//\n");
    printf("This is an example of overflow\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0xffffffff;
    b[3] = 0xffffffff;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    add_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xfffffffe;
    expected[1] = 0xffffffff;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test A.2 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);
    reset_out(out);

    add_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test A.3 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);
    reset_out(out);

    add_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000001;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test A.4 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000002;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);
    reset_out(out);

    add_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0x00000001;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test A.5 ========================//\n");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);
    reset_out(out);

    add_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000002;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test A.6 ========================//\n");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000001;
    a[3] = 0x00000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000001;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);
    reset_out(out);

    add_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000002;
    expected[1] = 0x00000000;
    expected[2] = 0x00000002;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test A.7 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);
    reset_out(out);

    add_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xfffffffe;
    expected[1] = 0xffffffff;
    expected[2] = 0x00000001;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Tests for Subtract ========================//\n");

    printf("\n// ================ Test B.1 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.2 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xfffffffe;
    expected[1] = 0xffffffff;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.3 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xfffffffe;
    expected[1] = 0xffffffff;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.4 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000002;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xfffffffd;
    expected[1] = 0xffffffff;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.5 ========================//\n");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.6 ========================//\n");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000001;
    a[3] = 0x00000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000001;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.7 ========================//\n");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000001;
    a[3] = 0x00000002;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000001;
    b[3] = 0x00000001;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000001;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.8 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.9 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000001;
    a[3] = 0x00000000;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.10 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000002;
    a[3] = 0xf0000000;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0x00000001;
    expected[3] = 0xf0000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.11 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0xf0000000;

    b[0] = 0x0000000f;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xfffffff1;
    expected[1] = 0xffffffff;
    expected[2] = 0xffffffff;
    expected[3] = 0xefffffff;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.12 ========================//\n");
    printf("// This is a case of underflow\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0xffffffff;
    b[3] = 0xffffffff;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.13 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0xf0000000;

    b[0] = 0x0000000f;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xfffffff1;
    expected[1] = 0xffffffff;
    expected[2] = 0xffffffff;
    expected[3] = 0xefffffff;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.14 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0xffffffff;
    b[3] = 0xffffffff;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.15 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input A: \t");
    print_u128(a);

    printf("Input B: \t");
    print_u128(b);

    reset_out(out);

    sub_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0xfffffffe;
    expected[3] = 0xffffffff;

    printf("Expected: \t");
    print_u128(expected);

    return 0;
}
