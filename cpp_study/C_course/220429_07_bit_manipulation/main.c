#include <stdio.h>

void main()
{

	printf("Result 01: %d\n", 0b0101);

	printf("Result 02: %d\n", 0b1111);

	printf("Result 03: %d\n", 0b0001 & 0b0001);
	
	printf("Result 05: %d\n", 0b1011 & 0b1000);
	
	unsigned int num1 = 0b1000;

	printf("Result 05: %d\n", num1);

	printf("Result 06: %d\n", 0b1001 | 0b1011);

	printf("Result 07: %d\n", 0b1001 ^ 0b1011);

	printf("Result 08: %d\n", 0b0001 << 1);

	printf("Result 09: %d\n", 0b0001 << 2);

	printf("Result 10: %d\n", 0b0001 << 3);

	printf("Result 11: %d\n", 0b1000 >> 1 );

}



