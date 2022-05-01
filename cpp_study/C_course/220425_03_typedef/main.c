// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24168564#questions

#include <stdio.h>

typedef int grade;

typedef struct date {
    int day;
    int month;
    int year;
} Date;

void printDate(Date dt)
{
    // can we consider this a method?
    printf("Your birthday is: %d-%d-%d.\n", dt.month, dt.day, dt.year);
}

Date inputDate()
{
    Date dt;
    printf("Input day: ");
    scanf("%d", &dt.day);

    printf("Input month: ");
    scanf("%d", &dt.month);

    printf("Input year: ");
    scanf("%d", &dt.year);

    return dt;
}

void main()
{

    grade math = 9;

    Date myBirthDay;

    myBirthDay = inputDate();

    printDate(myBirthDay);
}
