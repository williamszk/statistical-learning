#include <stdio.h>
#include <stdint.h>
#include "large_integer.h"
#include "testing.h"

// 101011 / 101 = 1000
// 0x2B / 0x5 = 0x8

// this is a case of overflow
// ffff * f = e fff1

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

    printf("\n// ==== Tests for Multiplication ==== //\n");
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

    mult_u128(out, a, b);

    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0xfffffffe;
    expected[3] = 0xffffffff;

    test_u128(out, expected);

    printf("2. \t");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;

    b[0] = 0x0000000f;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0xfffffff1;
    expected[1] = 0xffffffff;
    expected[2] = 0xffffffff;
    expected[3] = 0xffffffff;

    test_u128(out, expected);

    printf("3. \t");
    a[0] = 0x00000015;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000002;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x0000002a;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("4. \t");
    a[0] = 0x00000015;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x0000000a;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x000000d2;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("5. \t");
    a[0] = 0x0000000f;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x0000000f;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x000000e1;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("6. \t");
    a[0] = 0x000000ff;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x0000000f;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000ef1;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("7. \t");
    a[0] = 0x000000ff;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x0000000f;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000ef1;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("8. \t");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0xffffffff;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0xffffffff;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("9. \t");
    a[0] = 0x00000001;
    a[1] = 0xf0000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000001;
    expected[1] = 0xf0000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("10. \t");
    a[0] = 0x11111111;
    a[1] = 0x11111111;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000002;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x22222222;
    expected[1] = 0x22222222;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("11. \t");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000ff2;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000002;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("12. \t");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x11111111;
    a[3] = 0x11111111;

    b[0] = 0x00000002;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x22222222;
    expected[3] = 0x22222222;

    test_u128(out, expected);

    printf("12. \t");
    a[0] = 0x00000002;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000002;
    b[1] = 0x00000000;
    b[2] = 0xffffffff;
    b[3] = 0xffffffff;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000004;
    expected[1] = 0x00000000;
    expected[2] = 0xfffffffe;
    expected[3] = 0xffffffff;

    test_u128(out, expected);

    printf("13. \t");
    a[0] = 0x00000000;
    a[1] = 0xf0000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000000;
    b[1] = 0xf0000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0xe1000000;

    test_u128(out, expected);

    printf("14. \t");
    a[0] = 0x00000000;
    a[1] = 0xf0000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000002;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0xe0000000;
    expected[2] = 0x00000001;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("15. \t");
    a[0] = 0x00000000;
    a[1] = 0x20000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000000;
    b[1] = 0x10000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x02000000;

    test_u128(out, expected);


    printf("16. \t");
    a[0] = 0x00000000;
    a[1] = 0x20000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000022;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x40000000;
    expected[2] = 0x00000004;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("17. \t");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x0000000a;
    a[3] = 0x00000000;

    b[0] = 0x00000002;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000014;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("18. \t");
    a[0] = 0x00000002;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x0aaa0000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x15540000;

    test_u128(out, expected);


    printf("19. \t");
    a[0] = 0x0000000a;
    a[1] = 0x00000000;
    a[2] = 0x0000000a;
    a[3] = 0x00000000;

    b[0] = 0x0000000a;
    b[1] = 0x00000000;
    b[2] = 0x0000000a;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000064;
    expected[1] = 0x00000000;
    expected[2] = 0x000000c8;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("20. \t");
    a[0] = 0x0000000a;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x0aaa0000;

    b[0] = 0x0000000a;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    mult_u128(out, a, b);

    expected[0] = 0x00000064;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x6aa40000;

    test_u128(out, expected);

    // ============================================================================= //
    printf("\n// ==== Tests for Division ==== //\n");
    
    printf("1. \t");
    a[0] = 0x00000004;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000002;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0x00000002;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("2. \t");
    a[0] = 0xf0000000;
    a[1] = 0xf0000000;
    a[2] = 0xf0000000;
    a[3] = 0xf0000000;

    b[0] = 0xf0000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0x00000001;
    expected[1] = 0x00000001;
    expected[2] = 0x00000001;
    expected[3] = 0x00000001;

    test_u128(out, expected);

    printf("3. \t");
    a[0] = 0xe0000000;
    a[1] = 0xf0000000;
    a[2] = 0xf0000000;
    a[3] = 0xf0000000;

    b[0] = 0xf0000000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x00000001;
    expected[2] = 0x00000001;
    expected[3] = 0x00000001;

    test_u128(out, expected);

    printf("4. \t");
    a[0] = 0x00e00000;
    a[1] = 0x00e00000;
    a[2] = 0x00e00000;
    a[3] = 0x00e00000;

    b[0] = 0x000e0000;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0x00000010;
    expected[1] = 0x00000010;
    expected[2] = 0x00000010;
    expected[3] = 0x00000010;

    test_u128(out, expected);

    printf("5. \t");
    a[0] = 0xffffffff;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000000;
    b[1] = 0x00000002;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);


    printf("6. \t");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000005;

    b[0] = 0x00000002;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);
    div_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x80000000;
    expected[3] = 0x00000002;

    test_u128(out, expected);

    printf("7. \t");
    a[0] = 0xffffffff;
    a[1] = 0x000000f0;
    a[2] = 0x00000000;
    a[3] = 0x00000000;

    b[0] = 0x00000000;
    b[1] = 0x00000002;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0x00000078;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("8. \t");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0xe0000000;
    a[3] = 0x00000000;

    b[0] = 0x00000000;
    b[1] = 0x00000002;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0x00000000;
    expected[1] = 0x70000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("9. \t");
    // this is a case of non-rational division
    a[0] = 0xa0000000;
    a[1] = 0xa0000000;
    a[2] = 0xa0000000;
    a[3] = 0xa0000000;

    b[0] = 0x00000000;
    b[1] = 0x00000030;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0xadffffff;
    expected[1] = 0x58aaaaaa;
    expected[2] = 0x03555555;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("10. \t");
    // this is a case of non-rational division
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0xa0000000;
    a[3] = 0xa0000000;

    b[0] = 0x00000000;
    b[1] = 0x00000030;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0xaaaaaaaa;
    expected[1] = 0x58aaaaaa;
    expected[2] = 0x03555555;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("11. \t");
    // this is a case of non-rational division
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0xa0000000;

    b[0] = 0x00000003;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0x55555555;
    expected[1] = 0x55555555;
    expected[2] = 0x55555555;
    expected[3] = 0x35555555;

    test_u128(out, expected);

    printf("12. \t");
    // this is a case of non-rational division
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0xBE910000;
    a[3] = 0x640F10CC;

    b[0] = 0x00000003;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);
    expected[0] = 0x55555555;
    expected[1] = 0x55555555;
    expected[2] = 0xEA305555;
    expected[3] = 0x215A5AEE;

    test_u128(out, expected);
    print_u128(out);
    print_u128(expected);

    printf("13. \t");
    // this is a case of non-rational division
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0xa0000000;

    b[0] = 0x00000000;
    b[1] = 0x00000003;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0x55555555;
    expected[1] = 0x55555555;
    expected[2] = 0x35555555;
    expected[3] = 0x00000000;

    test_u128(out, expected);


    printf("14. \t");
    // this is a case of non-rational division
    a[0] = 0x10000000;
    a[1] = 0x10000000;
    a[2] = 0x10000000;
    a[3] = 0x10000000;

    b[0] = 0x00000000;
    b[1] = 0x00000003;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0xafffffff;
    expected[1] = 0x5aaaaaaa;
    expected[2] = 0x05555555;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("15. \t");
    // this is a case of non-rational division
    a[0] = 0x10000000;
    a[1] = 0x10000000;
    a[2] = 0x10000000;
    a[3] = 0x10000000;

    b[0] = 0x00000003;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    // expected[0] = 0x05555555;
    // expected[1] = 0xb0000000;
    // expected[2] = 0x5aaaaaaa;
    // expected[3] = 0x05555555;

    expected[0] = 0x05555554;
    expected[1] = 0xb0000000;
    expected[2] = 0x5aaaaaaa;
    expected[3] = 0x05555555;

    test_u128(out, expected);
    print_u128(out);
    print_u128(expected);


    printf("16. \t");
    a[0] = 0x00000000;
    a[1] = 0x00000010;
    a[2] = 0x00000010;
    a[3] = 0x00000010;

    b[0] = 0x00000000;
    b[1] = 0x00000003;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0xaaaaaaaf;
    expected[1] = 0x5555555a;
    expected[2] = 0x00000005;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("17. \t");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0xd0000000;

    b[0] = 0x00000000;
    b[1] = 0x00000003;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0x55555555;
    expected[1] = 0x55555555;
    expected[2] = 0x45555555;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("18. \t");
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0xd0000000;
    a[3] = 0xd0000000;

    b[0] = 0x00000000;
    b[1] = 0x00000003;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0xaaaaaaaa;
    expected[1] = 0x9aaaaaaa;
    expected[2] = 0x45555555;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("19. \t");
    a[0] = 0x00000000;
    a[1] = 0x00000001;
    a[2] = 0xd0000000;
    a[3] = 0xd0000000;

    b[0] = 0x00000000;
    b[1] = 0x00000003;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0xaaaaaaaa;
    expected[1] = 0x9aaaaaaa;
    expected[2] = 0x45555555;
    expected[3] = 0x00000000;

    test_u128(out, expected);

    printf("20. \t");
    // this is a case of non-rational division
    a[0] = 0x00000000;
    a[1] = 0x10000000;
    a[2] = 0x10000000;
    a[3] = 0x10000000;

    b[0] = 0x00000003;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0xffffffff;
    expected[1] = 0xafffffff;
    expected[2] = 0x5aaaaaaa;
    expected[3] = 0x05555555;

    test_u128(out, expected);
    print_u128(out);
    print_u128(expected);

    printf("21. \t");
    // this is a case of non-rational division
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x10000000;
    a[3] = 0x10000000;

    b[0] = 0x00000003;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0xaaaaaaaa;
    expected[1] = 0xaaaaaaaa;
    expected[2] = 0x5aaaaaaa;
    expected[3] = 0x05555555;

    test_u128(out, expected);
    print_u128(out);
    print_u128(expected);

    printf("22. \t");
    // this is a case of non-rational division
    a[0] = 0x00000000;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x10000000;

    b[0] = 0x00000003;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    reset_out(out);

    div_u128(out, a, b);

    expected[0] = 0x55555555;
    expected[1] = 0x55555555;
    expected[2] = 0x55555555;
    expected[3] = 0x05555555;

    test_u128(out, expected);
    print_u128(out);
    print_u128(expected);
}
