// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/29288928#questions 

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


int equalPoints(Point p1, Point p2)
{
	if (p1.x == p2.x && p1.y == p2.y)
		return 1;
	else
		return 0;
}

int equalByAge(Employee emp1, Employee emp2)
{
	if (emp1.age == emp2.age)
		return 1;
	else
		return 0;
}


void main()
{

	Point p1 = {2, 3}, p2 = {2, 3};

	printf("Is p1 equal to p2?    %d\n", equalPoints(p1, p2));

	Employee alice = {"Alice", 40.0, 1}, bob = {"Bob", 40, 2};

	printf("Is Alice equal to Bob by age?    %d\n", equalByAge(alice, bob));
}

