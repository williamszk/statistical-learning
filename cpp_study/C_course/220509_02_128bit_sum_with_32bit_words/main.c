
#include <stdio.h>
#include <stdint.h>

void print_largeint(uint32_t *a)
{
    printf("0x%08x_%08x_%08x_%08x\n", a[3], a[2], a[1], a[0]);
}

void add_u128(uint32_t *out, uint32_t *a, uint32_t *b)
{
    // we use 32bit integer because we can still manage to use 64bit and just use
    // bitshift to know if happened some overflow
    uint64_t sum;

    sum = (uint64_t)a[0] + (uint64_t)b[0];
    out[0] = (uint32_t)sum;

    // sum is a 64 bit integer, and we can imagine that a[0] is the
    // first number by the right, it is the inverse thinking from the
    // array order
    sum = (uint64_t)a[1] + (uint64_t)b[1] + (uint64_t)(sum >> 32);
    out[1] = (uint32_t)sum;
    // the last term (uint64_t)(sum >> 32) is used to include the possible carry
    // or overflow of the previous sum

    sum = (uint64_t)a[2] + (uint64_t)b[2] + (uint64_t)(sum >> 32);
    out[2] = (uint32_t)sum;

    sum = (uint64_t)a[3] + (uint64_t)b[3] + (uint64_t)(sum >> 32);
    out[3] = (uint32_t)sum;

    // out[4] is used to store the possible carry that the sum may have
    out[4] = (uint32_t)(sum >> 32);
}

int main()
{
    printf("\n ================ Test 1 ======================== \n");
    uint32_t a[4] = {0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff};
    uint32_t b[4] = {0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff};
    uint32_t out[5]; // there are 5 slots for 32bit unsigned int, the right most slot is reserved to the carry or overflow
    add_u128(out, a, b);
    printf("Result: \t");
    print_largeint(out);
    uint32_t expected[4] = {0xfffffffe, 0xffffffff, 0xffffffff, 0xfffffffe};
    printf("Expected: \t");
    print_largeint(expected);

    printf("\n ================ Test 2 ======================== \n");
    printf("This is an example of overflow\n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0xffffffff;
    a[3] = 0xffffffff;
    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    out[5]; 
    add_u128(out, a, b);
    printf("Result: \t");
    print_largeint(out);
    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;
    printf("Expected: \t");
    print_largeint(expected);

    printf("\n ================ Test 3 ======================== \n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;
    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    out[5]; 
    add_u128(out, a, b);
    printf("Result: \t");
    print_largeint(out);
    expected[0] = 0x00000000;
    expected[1] = 0x00000000;
    expected[2] = 0x00000001;
    expected[3] = 0x00000000;
    printf("Expected: \t");
    print_largeint(expected);

    printf("\n ================ Test 4 ======================== \n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;
    b[0] = 0x00000002;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    out[5]; 
    add_u128(out, a, b);
    printf("Result: \t");
    print_largeint(out);
    expected[0] = 0x00000001;
    expected[1] = 0x00000000;
    expected[2] = 0x00000001;
    expected[3] = 0x00000000;
    printf("Expected: \t");
    print_largeint(expected);


    printf("\n ================ Test 5 ======================== \n");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000000;
    a[3] = 0x00000000;
    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    out[5]; 
    add_u128(out, a, b);
    printf("Result: \t");
    print_largeint(out);
    expected[0] = 0x00000002;
    expected[1] = 0x00000000;
    expected[2] = 0x00000000;
    expected[3] = 0x00000000;
    printf("Expected: \t");
    print_largeint(expected);


    printf("\n ================ Test 6 ======================== \n");
    a[0] = 0x00000001;
    a[1] = 0x00000000;
    a[2] = 0x00000001;
    a[3] = 0x00000000;
    b[0] = 0x00000001;
    b[1] = 0x00000000;
    b[2] = 0x00000001;
    b[3] = 0x00000000;

    out[5]; 
    add_u128(out, a, b);
    printf("Result: \t");
    print_largeint(out);
    expected[0] = 0x00000002;
    expected[1] = 0x00000000;
    expected[2] = 0x00000002;
    expected[3] = 0x00000000;
    printf("Expected: \t");
    print_largeint(expected);

    printf("\n ================ Test 7 ======================== \n");
    a[0] = 0xffffffff;
    a[1] = 0xffffffff;
    a[2] = 0x00000000;
    a[3] = 0x00000000;
    b[0] = 0xffffffff;
    b[1] = 0xffffffff;
    b[2] = 0x00000000;
    b[3] = 0x00000000;

    out[5]; 
    add_u128(out, a, b);
    printf("Result: \t");
    print_largeint(out);
    expected[0] = 0xfffffffe;
    expected[1] = 0xffffffff;
    expected[2] = 0x00000001;
    expected[3] = 0x00000000;
    printf("Expected: \t");
    print_largeint(expected);


    return 0;
}
