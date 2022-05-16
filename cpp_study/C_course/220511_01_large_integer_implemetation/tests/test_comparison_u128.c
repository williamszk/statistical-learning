#include <stdio.h>
#include <stdint.h>
#include "large_integer.h"

/**
 * Resets to zero all values of the array out.
 *
 * It is so that we can use it in the next test.
 */

int main()
{
    uint32_t a[4];
    uint32_t b[4];
    int result;
    int expected;

    printf("\n// ================ Tests for Greater ========================//\n");

    printf("\n// ================ Test A.1 ========================//\n");
    a[0] = 0x00000002;
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

    result = greater_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 1;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Test A.2 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x20000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x10000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    result = greater_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 1;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Test A.3 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x10000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x20000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    result = greater_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 0;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Test A.4 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000020;
    a[3] = 0x10000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000010;
    b[3] = 0x10000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    result = greater_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 1;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Test A.5 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000021;
    a[3] = 0x10000000;

    b[0] = 0xffffffff;
    b[1] = 0x00000000;
    b[2] = 0x00000020;
    b[3] = 0x10000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    result = greater_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 1;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Test A.6 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0x00000000;
    a[2] = 0x00000021;
    a[3] = 0x10000000;

    b[0] = 0xffffffff;
    b[1] = 0x00000000;
    b[2] = 0x00000021;
    b[3] = 0x10000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    result = greater_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 0;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Tests for Less-Than ========================//\n");

    printf("\n// ================ Test B.1 ========================//\n");
    a[0] = 0x00000002;
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

    result = less_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 0;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Test B.2 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x20000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x10000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    result = less_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 0;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Test B.3 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x10000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x20000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    result = less_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 1;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Test B.4 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000020;
    a[3] = 0x10000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000010;
    b[3] = 0x10000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    result = less_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 0;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Test B.5 ========================//\n");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000021;
    a[3] = 0x10000000;

    b[0] = 0xffffffff;
    b[1] = 0x00000000;
    b[2] = 0x00000020;
    b[3] = 0x10000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    result = less_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 0;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Test B.6 ========================//\n");
    a[0] = 0xffffffff;
    a[1] = 0x00000000;
    a[2] = 0x00000021;
    a[3] = 0x10000000;

    b[0] = 0xffffffff;
    b[1] = 0x00000000;
    b[2] = 0x00000021;
    b[3] = 0x10000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    result = less_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 0;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Tests for Equal ========================//\n");

    
    printf("\n// ================ Test C.1 ========================//\n");
    a[0] = 0x00000001;
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

    result = equal_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 1;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Test C.2 ========================//\n");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x02000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x02000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    result = equal_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 1;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Test C.2 ========================//\n");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x02000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x02000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    result = equal_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 1;

    printf("Expected: \t");
    printf("%d\n", expected);

    printf("\n// ================ Test C.3 ========================//\n");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x02000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x02000000;

    printf("Input a: \t");
    print_u128(a);

    printf("Input b: \t");
    print_u128(b);

    result = equal_u128(a, b);

    printf("Result: \t");
    printf("%d\n", result);

    expected = 0;

    printf("Expected: \t");
    printf("%d\n", expected);

    return 0;
}
