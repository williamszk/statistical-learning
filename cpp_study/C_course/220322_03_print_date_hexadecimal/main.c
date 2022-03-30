// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30516416#overview

#include <stdio.h>

void main()
{
    int birthYear;
    int birthMonth;
    int birthDay;
    printf("Write your birthday year:\n");
    scanf("%d", &birthYear);

    printf("Write your birthday month:\n");
    scanf("%d", &birthMonth);

    printf("Write your birthday day:\n");
    scanf("%d", &birthDay);

    printf("Answer:\n");
    printf("Year = 0x%X\n", birthYear);
    printf("Month = 0x%X\n", birthMonth);
    printf("Day = 0x%X\n", birthDay);

}