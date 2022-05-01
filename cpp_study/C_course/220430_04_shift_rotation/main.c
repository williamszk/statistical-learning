#include <stdio.h>
#define LONG_SIZE 64

unsigned long rotateBitLeft(unsigned long data, int shift)
{
    unsigned long output;

    output = (data << shift) | (data >> (LONG_SIZE - shift));

    return output;
}

void main()
{

    unsigned long data = 0xF;

    printf("%d\n", sizeof(data));

    printf("0x%lx\n", data);

    unsigned long dataShifted = rotateBitLeft(data, 1);

    printf("0x%lx\n", dataShifted);

    unsigned long data2 = 0xF000000000000000;
    printf("0x%lx\n", data2);
    unsigned long dataShifted2 = rotateBitLeft(data2, 1);
    printf("0x%lx\n", dataShifted2); //e000000000000001

    printf("0x%lx\n", data2 >> 63);
}