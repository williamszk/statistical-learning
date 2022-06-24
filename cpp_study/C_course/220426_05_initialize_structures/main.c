// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/29269092#questions

#include <stdio.h>

typedef struct point {
	 int x;
	 int y;
} Point;


void main()
{
	// Declare a "Point" type without initialization
	Point p1;

	// Initialize a "Point" variable (members in order)
	Point p2 = {5, 7};

	// Declare and assign (using designed initializer)
	Point p3 = { .x = 3, .y = 4 };

	// Differently from Go, we need to add . in front
	// of the fields to initialize them
	
	// Declare and assign (out of order)
	Point p4 = {.y = 10, .x = 3};

	// Declare and partially assign 
	// (other members are initialized with 0)
	// what if the other member is a string? (array of chars)
	Point p5 = {.x = 1};
}

