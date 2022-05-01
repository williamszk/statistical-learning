// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/29285754#questions

#include <stdio.h>

typedef struct Point {
	int x;
	int y;
} Point;



void printPoint(Point p)
{
	printf("Point x:%d, y:%d\n", p.x, p.y);
}


Point getPointFromUser()
{
	Point point;
	printf("Write the x-coordinate: ");
	scanf("%d", &point.x);

	printf("Write the y-coordinate: ");
	scanf("%d", &point.y);

	return point;
}


void main()
{
	Point point = getPointFromUser();

	printPoint(point);

	// modify the point
	
	point.x += 1;
	point.y += 3;

	printPoint(point);


}

