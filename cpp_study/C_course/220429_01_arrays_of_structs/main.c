// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/29269102?start=15#questions

#include <stdio.h>
#define ARR_SIZE 5


typedef struct Point{
	int x;
	int y;
} Point;


void main()
{
	Point pointsArray[ARR_SIZE];

	printf("Insert x value for first element of the array.\n");
	pointsArray[0].x = 10;
	
	printf("Insert y value for first element of the array.\n");
	pointsArray[0].y = 30; 

	int i = 0;

	for (i = 0; i < ARR_SIZE; i++)
	{
		// printf("Point:\n\tx: %d\n\ty: %d\n\n", pointsArray[i].x, pointsArray[i].y);
		printf("Point #%d = (%d, %d)\n", i, pointsArray[i].x, pointsArray[i].y);
	}
} 


