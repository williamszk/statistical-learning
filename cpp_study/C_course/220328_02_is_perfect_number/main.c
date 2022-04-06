// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/31499126#overview

#include <stdio.h>

int isPerfectNumber(int num)
{
	int counter = 1;
	int sumDivisor = 0;

	while (counter != num)
	{
		if (num % counter == 0)
		{
			sumDivisor += counter;
		}

		counter++;
	}

	if (sumDivisor == num) return 1;
	else return 0;
}

void main()
{
	int num;
	printf("Write a number: ");
	scanf("%d", &num);

	int isPerOutput = isPerfectNumber(num);

	if (isPerOutput == 1) printf("%d is perfect number.", num);
	else printf("%d is not perfect number.", num);
	
}