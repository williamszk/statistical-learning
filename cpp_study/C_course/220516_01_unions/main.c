// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25631116?start=0#questions
// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25631120#questions
// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25631124#questions

#include <stdio.h>
#include <string.h>

// info is the union name
union info
{
    char firstName[20];
    int age;
};

// minmax is the union name
union minmax
{
    int min;
    int max;
    double average;
};

struct pointSt
{
    int x;
    int y;
};

union pointUn
{
    int x;
    int y;
};

int main()
{
    // The union is a way to store different types of datatypes
    // we can store different types of data inside of it
    // each different key will store in the same region of memory

    // union variable
    union info myVar1;

    myVar1.age = 30;
    printf("myVar1.age = %d\n", myVar1.age);
    strcpy(myVar1.firstName, "Hello!");

    printf("myVar1.age = %d\n", myVar1.age);
    printf("myVar1.firstName = %s\n", myVar1.firstName);


    struct pointSt point01;
    union pointUn point02;

    // can we use typedef with union too?
    /**
     * 
     * 
     * 
     * 
     * 
     */
    point01.x = 5;
    point01.y = 7;

    printf("Struct point = (%d, %d)\n", point01.x, point01.y);

    point02.x = 3;
    point02.y = 5;

    printf("Struct point = (%d, %d)\n", point02.x, point02.y);

    return 0;
}