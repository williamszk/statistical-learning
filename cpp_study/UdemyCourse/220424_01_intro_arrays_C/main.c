#include <stdio.h>

// some notes on the class:
// https://www.udemy.com/course/datastructurescncpp/learn/lecture/13612032#overview


void main()
{
	int i;
	int arr[10];

	printf("%ld\n", sizeof(arr[0])); // an integer takes 4 bytes

	int arr2[] = {2,4,6,8,10};

	int arrLen = sizeof(arr2)/sizeof(arr2[0]);

	for (i = 0; i < arrLen; i++)
	{
		printf("%d ", arr2[i]);
	} 
	printf("\n");
}

