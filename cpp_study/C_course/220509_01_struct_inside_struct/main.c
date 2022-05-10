// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/29285776#questions

#include <stdio.h>

typedef struct point
{
    int x;
    int y;
} Point;

typedef struct circle
{
    Point center;
    double radius;
} Circle;

int main()
{
    Point p1 = {
        .x = 1,
        .y = 2,
    };

    Circle c1 = {
        .center = p1,
        .radius = 3.3,
    };

    // we can access the fields of internal structs
    // like in nested objects
    printf("radius x: %d, y: %d\n", c1.center.x, c1.center.y);

    return 0;
}
