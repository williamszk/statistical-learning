// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203436#questions

#include <stdio.h>

void main()
{
	int num;
	uint32_t pow;
	int result = 1;

	printf("Write the base number: ");
	scanf("%d", &num);

	printf("Write the power number: ");
	scanf("%d", &pow);

	for (int i = 0; i < pow; i++)
	{
		result *= num;	
	}
	
	printf("Result: %d\n", result);	
}

