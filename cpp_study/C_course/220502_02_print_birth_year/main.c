// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24147604#questions

#include <stdio.h>
#define CURR_YEAR 2022

void main()
{
    int age = 29;
    printf("Current year: %d - age: %d = Birth Year: %d\n", CURR_YEAR, age, CURR_YEAR - age);
}