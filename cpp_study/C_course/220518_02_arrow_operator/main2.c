// // https://www.geeksforgeeks.org/arrow-operator-in-c-c-with-examples/
// C program to show Arrow operator
// used in structure

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Creating the union
union student {
	char name[80];
	int age;
	float percentage;
};

// Creating the union object
union student* emp = NULL;

// Driver code
int main()
{
	// Assigning memory to struct variable emp
	emp = (union student*)
		malloc(sizeof(union student));

	// Assigning value to age variable
	// of emp using arrow operator
	emp->age = 18;

	// DIsplaying the assigned value to the variable
	printf("emp->age = %d\n", emp->age);

    strcpy(emp->name, "Dennis Ritchie");
    printf("emp->name = %s\n", emp->name);
    printf("emp->age = %d\n", emp->age); // meaning less value
    // printf("emp->age = %s\n", emp->age); // this will give problem to the terminal
    
}
