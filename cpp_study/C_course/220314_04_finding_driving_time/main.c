// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24147672#overview

#include <stdio.h>

float howLongTrip(float dist, float speed)
{
    return dist/speed;
}

int main()
{
    float dist = 100;
    float speed = 34;
    float duration = howLongTrip(dist, speed);
    printf("dist = %.2f km\n", dist);
    printf("speed = %.2f km/h\n", speed);
    printf("duration = %.2f h\n", duration);

}