// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24147886#overview
#include <stdio.h>

void main()
{
    long seconds = 999999;
    long remainSeconds, hours, minutes;
    long SECONDS_TO_HOURS = 3600;
    long SECONDS_TO_MINUTES = 60;
    printf("Write the quantity of seconds:\n");
    scanf("%d", &seconds);

    hours = seconds / SECONDS_TO_HOURS;
    // printf("seconds: %d\n", seconds);
    remainSeconds = seconds % SECONDS_TO_HOURS;

    minutes = remainSeconds / SECONDS_TO_MINUTES;
    
    remainSeconds %= SECONDS_TO_MINUTES;

    if (hours < 10)
    {
        printf("0%d:", hours);
    }
    else
    {
        printf("%d:", hours);
    }

    if (minutes < 10)
    {
        printf("0%d:", minutes);
    }
    else
    {
        printf("%d:", minutes);
    }

    if (remainSeconds < 10)
    {
        printf("0%d\n", remainSeconds);
    }
    else
    {
        printf("%d\n", remainSeconds);
    }
}