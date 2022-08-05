
#include <stdlib.h>
#include <stdio.h>

int main()
{
 	int *values = malloc(40);
	values[2] = 45;
	int x = values[2];

	// we can expand the size of the heap allocated
	// using realloc
	
	values = realloc(values, 2000*sizeof(int));

	x = values[600];

	printf("The value in x is: %d\n", x);
}

// https://youtu.be/VOpjAHCee7c?t=196

