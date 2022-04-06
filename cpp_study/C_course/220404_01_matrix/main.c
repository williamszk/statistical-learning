// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24168484#overview

#include <stdio.h>

void main()
{
	int i, j;
	int hold;
	double holdDouble;

	int mat[2][3] = {{1, 2, 3},
					 {4, 5, 6}};

	double mat2[3][2] = {{1.2, 0.5},
						 {5.2, 1.0},
						 {3.3, 4.4}};

	// initialization with incomplete internal curly brackets
	int mat3[2][3] = {{5, 6}, {7}};
	// C pads empty values with 0.
	// 5 6 0
	// 7 0 0

	//   5  6  0
	//   7  0  0

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			hold = mat3[i][j];
			if (hold >= 10)
			{
				printf(" ");
			}
			else
			{
				printf("  ");
			}
			printf("%d", hold);
		}
		printf("\n");
	}
	printf("-------------\n");

	int mat4[4][3] = {{1, 2}, {4, 5, 8}, {10}};
	// 1  2  0
	// 4  5  8
	// 10 0  0
	// 0  0  0

	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 3; j++)
		{
			hold = mat4[i][j];
			if (hold >= 10)
			{
				printf(" ");
			}
			else
			{
				printf("  ");
			}
			printf("%d", hold);
		}
		printf("\n");
	}
	printf("-------------\n");

	//   1  2  0
	//   4  5  8
	//  10  0  0
	//   0  0  0

	double mat5[3][2] = {{}, {5.2, 1.0}, {3.3}};

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 2; j++)
		{
			holdDouble = mat5[i][j];
			if (holdDouble >= 10)
			{
				printf(" ");
			}
			else
			{
				printf("  ");
			}
			// format specification for double and float
			printf("%.2lf", holdDouble);
		}
		printf("\n");
	}
	printf("-------------\n");
	// 0.00  0.00
	// 5.20  1.00
	// 3.30  0.00

	// Excessively values in the internal curly brackets
	int mat6[2][3] = {5, 2, 1, 6, 5};

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			hold = mat6[i][j];
			if (hold >= 10)
			{
				printf(" ");
			}
			else
			{
				printf("  ");
			}
			// format specification for double and float
			printf("%d", hold);
		}
		printf("\n");
	}
	printf("-------------\n");
	//   5  2  1
	//   6  5  0
}