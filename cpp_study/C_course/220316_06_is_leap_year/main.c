// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24147896#overview

#include <stdio.h>

void main()
{
    // if it is divisable by 4

    // but if year is divisible by 100 it is not leap year

    // if year is divisible by 400 then it is leapyear

    int year;
    printf("Enter a year:\n");
    scanf("%d", &year);
    
    int isLeapYear = 0;

    if (year % 4 == 0)
    {
        if (year % 100 == 0)
        {
            // not leap year
            isLeapYear = 0;
        }
        else
        {
            if (year % 400)
            {
                // not leap year
                isLeapYear = 1;
            }
            else
            {
                // leap year
                isLeapYear = 0;
            }
        }
    }
    else
    {
        // not leapyear
        isLeapYear = 0;
    }

    if (isLeapYear == 1)
    {
        printf("%d is leap year.", year);
    }
    else
    {
        printf("%d is not leap year.", year);
    }
}