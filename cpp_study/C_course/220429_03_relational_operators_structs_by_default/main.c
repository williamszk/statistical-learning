// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/29288920?start=15#questions

#include <stdio.h>

typedef struct point {
	int x;
	int y;
} Point;


typedef struct employee {
	char name[10];
	float age;
	int id;
} Employee;


void main()
{
	Point p1 = {3,5}, p2 = {2,6};

    // this is not legal
    // we can't compare structs
	// if (p1 > p2)
	// {
	// 	printf("p1 > p2");	
	// }

	Employee emp1 = {"Jake", 24.5, 123};
	Employee emp2 = {"John", 30, 342};

	// this operation is ilegal, we can't compare two structs
	// if (emp1 == emp2)
	// {
	// 	printf("emp1 == emp2");	
	// }
}

