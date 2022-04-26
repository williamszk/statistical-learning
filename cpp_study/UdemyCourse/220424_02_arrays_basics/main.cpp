#include <iostream>

int main()
{
	
	int arr[5];
	arr[0] = 12;
	arr[1] = 15;
	arr[2] = 25;

	std::cout << "The sizeof of an array of 5 elements: " << sizeof(arr) << std::endl;
	// this should be 20, because it is 5*4 = 20 bytes

	std::cout << "The sizeof of a int: " << sizeof(arr[0]) << std::endl;

	// we can also use C functions
	printf("This comes from a C function: %ld\n", sizeof(arr[1]));


	// initialize an array
	int arr2[] = {2,4,6,8,10,12,14};

	// What is the size of the array?
	int arrLen = sizeof(arr2)/sizeof(arr2[0]);
	std::cout << "The size of the array is: " << arrLen << std::endl;

	// create an array and assign values but let
	// some slots not be assigned and print the whole array
	int arr3[10] = {2,3,4,1,2};

	int i;

	arrLen = sizeof(arr3)/sizeof(arr3[0]);

	printf("\nPrint the array: \n");	
	for (i = 0; i < arrLen; i++)
	{
		printf("%d ", arr3[i]);
	}

	std::cout << std::endl;

	// in C++ we have a foreach loop
	std::cout << "\nPrint the array again: " << std::endl;
	for (int x:arr3)
	{
		std::cout << x << " ";
	}
	std::cout << std::endl;

	
	return 0;
}

