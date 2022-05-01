// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/29272334#questions

#include <stdio.h>
#include <string.h>


typedef struct employee {
	char name[20];
	float age;
	int id;
} Employee;

typedef struct grades {
	int grades[3];
	float times[3];
} Grades;


void main()
{
	Employee emp1;
	Employee emp2 = {"Jake", 24.5, 123};

	Employee emp3 = {
		.name = "Bob",	
		.age = 33.2,
		.id = 321
	};

	// we can copy the values of one struct to another struct
	emp1 = emp2;
	
	printf("Name: %s, Age: %.2f, Id: %d\n", emp1.name, emp1.age, emp1.id);

	// How to copy all items from an array of structs?
	// And how to copy by value a struct that have an array
	// as one of its fields?
	
	// emp2.name = "Robert";
	// this is not allowed
	
	printf("&emp1.name: %p, &emp2.name: %p\n", &emp1.name, &emp2.name);
	// they have different addresses for the name
	// even the array is copied separately

	Grades gr1 = {
		.grades = {2,3,4},
		.times = {1.2,2.2,3.1}, 
	};

	Grades gr2;
	
	// copy by value to another struct
	gr2 = gr1;

	printf("&gr1.grades[0]: %p\t &gr2.grades[0]: %p\n", &gr1.grades[0], &gr2.grades[0]);
	// the data lives in different places
	// So even when we have a struct of arrays we will pass them by value
	// to the new struct.	

	// With simple arrays we would need to copy element by element using a for loop
	// but with structs it is simpler, we can just write = to copy by value all elements
	// of the array

	// How do we change the name of the employee
	// which is an array of char?
	strcpy(emp1.name, "Robert");	

	printf("emp1 - Name: %s, Age: %.2f, Id: %d\n", emp1.name, emp1.age, emp1.id);
	printf("emp2 - Name: %s, Age: %.2f, Id: %d\n", emp2.name, emp2.age, emp2.id);
	// We can see here that we changed the name of emp1
	// But emp2 kept the same name
}


