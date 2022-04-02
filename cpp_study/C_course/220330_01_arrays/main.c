// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203680#overview

// declarion of arrays

#include <stdio.h>

void main()
{
	int i;

	int grades[5];

	for (i = 0; i < 5; i++)
	{
		printf("%d\n", grades[i]);
	}
	// all elements are initialized as 0
	printf("end of loop\n");

	// just to see the size of the number
	printf("%lu\n", sizeof(6)); // 4 bytes, 4 bytes, 32 bits
	long num1 = 10;
	printf("%lu\n", sizeof(num1)); // 8 bytes, 64 bits

	long num2 = 1000000000000;
	printf("%lu\n", sizeof(num2)); // 8 bytes, 64 bits

	// declaration of array
	double salaries[10];

	char myArray[100];

	// initialize an array
	// "initialize" = "declare" + "assign"

	// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203686#overview
	printf("Start of loop\n");
	int arr[3] = {5, 7, 10};

	for (i = 0; i < 3; i++)
	{
		printf("%d\n", arr[i]);
	}

	float bArr[3] = {1.2, 5.3, 2.6};
	printf("Start of loop\n");
	for (i = 0; i < 3; i++)
	{
		printf("%f\n", bArr[i]);
	}

	char name[4] = {'M', 'i', 'k', 'e'};
	for (i = 0; i < 4; i++)
	{
		printf("%c", name[i]);
	}
	printf("\n");

	char mychar = 'M';
	printf("Size of char: %lu\n", sizeof(mychar)); // 1 char takes 1 byte, 8 bits
	// In C the char is 1 byte and is an ASCII character

	int myArr1[5] = {0}; // this will initialize all elements to 0

	// create an array with 10 elements, but the first two must be 1 and 2
	int myArr2[10] = {1,2};
	printf("Start loop\n");
	for (i = 0; i < 10; i++)
	{
		printf("%d\n", myArr2[i]);
	}
}
