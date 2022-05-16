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

    printf("\n// ================ Tests for Not Operator ========================//\n");

    printf("\n// ================ Test A.1 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    not_operator_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    printf("Expected: \t");
    print_u128(expected);


    printf("\n// ================ Test A.2 ========================//\n");
    a[0] = 0x00000001;
    a[1] = 0x00000001;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    printf("Input: \t\t");
    print_u128(a);

    reset_out(out);

    not_operator_u128(out, a);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xfffffffe;
    expected[1] = 0xfffffffe;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Tests for XOR Operator ========================//\n");

    printf("\n// ================ Test B.1 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    reset_out(out);

    xor_operator_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);    

    printf("\n// ================ Test B.2 ========================//\n");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    reset_out(out);

    xor_operator_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test B.3 ========================//\n");
    a[0] = 0x000000f1;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    reset_out(out);

    xor_operator_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x000000f0;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);


    printf("\n// ================ Test B.4 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0xffffffff;
    b[3] = 0xfffffff1;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    reset_out(out);

    xor_operator_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x0000000e;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Tests for AND opeartor ========================//\n");


    printf("\n// ================ Test C.1 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    reset_out(out);

    and_operator_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xffffffff;
    expected[1] = 0xffffffff;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);    

    printf("\n// ================ Test C.2 ========================//\n");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    reset_out(out);

    and_operator_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test C.3 ========================//\n");
    a[0] = 0x000000f1;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    reset_out(out);

    and_operator_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);


    printf("\n// ================ Test C.4 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0xffffffff;
    b[3] = 0xfffffff1;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    reset_out(out);

    and_operator_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xffffffff;
    expected[1] = 0xffffffff;
    expected[2] = 0xffffffff;
    expected[3] = 0xfffffff1;

    printf("Expected: \t");
    print_u128(expected);


    printf("\n// ================ Tests for OR opeartor ========================//\n");


    printf("\n// ================ Test D.1 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    reset_out(out);

    or_operator_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xffffffff;
    expected[1] = 0xffffffff;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);    

    printf("\n// ================ Test D.2 ========================//\n");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    reset_out(out);

    or_operator_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);

    printf("\n// ================ Test D.3 ========================//\n");
    a[0] = 0x000000f1;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    reset_out(out);

    or_operator_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0x000000f1;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    printf("Expected: \t");
    print_u128(expected);


    printf("\n// ================ Test D.4 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0xffffffff;
    b[3] = 0xfffffff1;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    reset_out(out);

    or_operator_u128(out, a, b);

    printf("Result: \t");
    print_u128(out);

    expected[0] = 0xffffffff;
    expected[1] = 0xffffffff;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    printf("Expected: \t");
    print_u128(expected);


    return 0;
}
