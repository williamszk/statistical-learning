
#include <stdio.h>


void main()
{
	unsigned int myhexnum = 0x10000000;

	printf("Hex: %x\t Dec: %d\n", myhexnum, myhexnum);

	// printf("sizeof: %d\n", sizeof(myhexnum));


	printf("Result 01: 0x%x\n", 0x00000001 + 0x00000001);

	printf("Result 02: 0x%x\n", 0x00000001 + 0x00000002);

	printf("Result 03: 0x%x\n", 0x00000001 + 0x00000010);

	printf("Result 04: 0x%x\n", 0x00000001 & 0x00000010);

	printf("Result 05: 0x%x\n", 0x00000010 & 0x00000010);

	printf("Result 06: 0x%x\n", 0x00000010 | 0x00000010);

	printf("Result 07: 0x%x\n", 0x00000011 | 0x00000010);

	printf("Result 08: 0x%x\n", 0x0000001a | 0x00000010);

	printf("Result 09: 0x%x\n", 0x0000001a | 0x0000001b);

	printf("Result 10: 0x%x\n", 0x0000001a | 0x0000001c);

	printf("Result 11: 0x%x\n", 0x0000001a ^ 0x0000001c);

	printf("Result 12: 0x%x\n", ~0x0000001a);

	printf("Result 13: 0x%x\n", 0x00000010 << 0x1);

	printf("Result 14: 0x%x\n", 0x00000010 << 0x2);

	printf("Result 15: 0x%x\n", 0x00000010 << 0x3);

	printf("Result 16: 0x%x\n", 0x00000010 >> 0x1);

	printf("Result 17: 0x%x\n", 0x00000010 >> 0x2);


}

