// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24168562#questions

#include <stdio.h>

struct date
{
    uint32_t day;
    uint32_t month;
    uint32_t year;
};

void main()
{

    struct date birthDay;

    printf("What is the day of your birthday? ");
    scanf("%d", &birthDay.day);

    printf("What is the month of your birthday? ");
    scanf("%d", &birthDay.month);

    printf("What is the year of your birthday? ");
    scanf("%d", &birthDay.year);

    printf("Your birthday is: %d/%d/%d (d/m/y)\n", birthDay.day, birthDay.month, birthDay.year);
}