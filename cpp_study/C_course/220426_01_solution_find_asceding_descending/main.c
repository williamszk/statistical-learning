// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/29730938#questions


#include <stdio.h>


int digitsSorted(int num)
{
	int units = num % 10;
	int tens = (num / 10) % 10;
	int sortedSoFar;

	if (num < 100)
		if (tens < units)
			return 1;
		else // unit < tens
			return -1;

	sortedSoFar = digitsSorted(num / 10);

	if (sortedSoFar == 0)
		return 0;

	if (sortedSoFar == 1 && tens < units)
		return 1;
	if (sortedSoFar == -1 && tens > units)
		return -1;

	return 0;

}

void main()
{

    int num1 = 124; // should return 1
    printf("num1: %d\n", digitsSorted(num1));  

	int num2 = 12340; // this should return 0
	printf("num2: %d\n", digitsSorted(num2));

	int num3 = 9643; // this should return -1
	printf("num2: %d\n", digitsSorted(num3));

}



