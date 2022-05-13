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

    printf("\n// ================ Tests for Increment ========================//\n");

    printf("\n// ================ Test 1 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0xffffffff;
    b[3] = 0xffffffff;

    printf("Input: \t\t");
    print_u128(a);

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






    return 0;
}
