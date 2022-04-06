// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24168510#overview

#include <stdio.h>

void main()
{
	int *x;
	int holdInt;
	int i, j, k;
	int arr[] = {1, 2, 3, 4};

	for (i = 0; i < 4; i++)
	{
		x = &arr[i];
		printf("%p\n", x); // how to print pointers
	}
	printf("-------------\n");
	for (i = 0; i < 4; i++)
	{
		x = &arr[i];
		printf("%d\n", *x);
	}
	printf("-------------\n");

	double mat[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

	double *y;
	double holdDouble;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			y = &mat[i][j];
			holdDouble = mat[i][j];
			printf("%p\t%.1lf\n", y, holdDouble);
		}
	}
	printf("---------------\n");

	float mat2[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
	float *pntFloat;
	float holdFloat;
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			pntFloat = &mat2[i][j];
			holdFloat = mat2[i][j];
			printf("%p\t%.1f\n", pntFloat, holdFloat);
		}
	}
	printf("---------------\n");

	int cube[2][2][2] = {{{1, 2}, {3, 4}}, {{5, 6}, {7, 8}}};
	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 2; j++)
		{
			for (k = 0; k < 2; k++)
			{
				x = &cube[i][j][k];
				holdInt = cube[i][j][k];
				printf("%p\t%d\n", x, holdInt);
			}
		}
	}
	printf("---------------\n");
}