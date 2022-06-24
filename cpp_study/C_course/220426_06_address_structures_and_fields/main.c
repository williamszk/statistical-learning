// We want to observe the address of a struct
// And it's fields

#include <stdio.h>

typedef struct person {
	char firstName[20];
	char lastName[20];
} Person;


void main()
{
	Person	bob = {
		.firstName = "Bob",
		.lastName = "Hendrix"
	};

	printf("First Name: %s\n", bob.firstName);

	printf("Address of structure: %p\n", &bob);

	printf("Address of field firstName of structure: %p\n", &(bob.firstName));

	printf("Address of field lastName of structure: %p\n", &(bob.lastName));

}


