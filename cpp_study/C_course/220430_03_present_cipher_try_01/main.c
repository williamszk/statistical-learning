// https://www.youtube.com/watch?v=tLa0IBpOE_I&ab_channel=CihangirTezcan

#include <stdio.h>

typedef struct string {
    char text[500];
} String;




void main()
{
    char plainText[] = "This is the PRESENT Cipher";

    printf("%d\n", sizeof(plainText[0]));

    // for testing, use just 1 simple text of 0s
    // 
    // block size = 64 bits = 8 bytes
    char plainText2[] = "00000000";
    // key length is 128 bits
    int keyLength = 128;
    // Rounds 31 = 1 1111b



    unsigned long myNum = 0b0000000000000001;

    printf("\n");

    unsigned long toBeRotated = 0b000000011111111;

    unsigned int data = 0xF;
    printf("0x%X\n", data);
    printf("0x%X\n", data >> 1);
    printf("0x%X\n", data << 28);
    printf("0x%X\n", data << 31);



}