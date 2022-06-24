// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/29288930#questions

#include <stdio.h>

typedef struct point
{
    int x;
    int y;
} Point;

Point addPoints(Point p1, Point p2)
{
    Point resultPoint;
    resultPoint.x = p1.x + p2.x;
    resultPoint.y = p1.y + p2.y;

    return resultPoint;
}

void incrementPoint(Point *ptr)
{
    (*ptr).x++;
    (*ptr).y++;
}

void main()
{
    Point myPnt = {
        .x = 1,
        .y = -2,
    };

    printf("x: %d, y: %d\n", myPnt.x, myPnt.y);

    incrementPoint(&myPnt);

    printf("x: %d, y: %d\n", myPnt.x, myPnt.y);

    Point myPnt2 = {
        .x = 10,
        .y = 20,
    };

    printf("x: %d, y: %d\n", myPnt2.x, myPnt2.y);

    Point myPnt3 = addPoints(myPnt, myPnt2);
    
    printf("x: %d, y: %d\n", myPnt3.x, myPnt3.y);
}