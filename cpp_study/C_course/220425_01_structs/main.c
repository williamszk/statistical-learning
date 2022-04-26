// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24168562#questions

#include <stdio.h>

struct point
{
    int x;
    int y;
};

void main()
{
    struct point coordPoint;
    printf("Write x-coordinate: ");
    scanf("%d", &coordPoint.x);

    printf("Write y-coordinate: ");
    scanf("%d", &coordPoint.y);

    printf("The point is: (%d, %d)\n", coordPoint.x, coordPoint.y);
}