// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24168502#overview

#include <stdio.h>

#define SIZE 10

void main()
{
	int i, j;
	int hold;
	int multTable[SIZE][SIZE];
	for (i = 1; i <= SIZE; i++)
	{
		for (j = 1; j <= SIZE; j++)
		{
			multTable[i - 1][j - 1] = i * j;
		}
	}

	printf("Number:");
	for (i = 1; i <= SIZE; i++)
	{
		if (i < SIZE)
		{
			printf("  ");
		}

		else
		{
			printf(" ");
		}

		printf("(%d)", i);
	}
	printf("\n");

	for (i = 1; i <= SIZE; i++)
	{
		if (i < SIZE)
			printf("   ");
		else
			printf("  ");
		printf("(%d)", i);

		for (j = 1; j <= SIZE; j++)
		{
			hold = multTable[i - 1][j - 1];

			printf("%5d", hold);
		}
		printf("\n");
	}
}