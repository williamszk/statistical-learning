// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25741522#questions

#include <stdio.h>
#include <stdlib.h>

union student {
    int ID;
    double average;
};

struct student2 {
    int ID;
    double average;
};

typedef union student3 {
    int ID;
    double average;
} Student;

int main()
{
    union student mystudent1;

    printf("%d\n", sizeof(mystudent1));

    struct student2 mystudent2;

    printf("%lu\n", sizeof(mystudent2));

    union student *ptrStudent1;

    printf("sizeof(ptrStudent1) = %d\n", sizeof(ptrStudent1));

    int aNum;

    printf("sizeof(aNum) = %d\n", sizeof(aNum)); // 4

    int *ptrNum;

    printf("sizeof(ptrNum) = %d\n", sizeof(ptrNum)); // 8, pointers in my machine seem to be of 64 bits
    // the size of the pointer depends on the CPU's architecture, my CPU is 64bits

    mystudent1.ID = 5;

    printf("mystudent1.ID = %d\n", mystudent1.ID); 

    ptrStudent1 = &mystudent1;

    // notation how to change the content of a union using pointer
    ptrStudent1->ID = 10;
    printf("mystudent1.ID = %d\n", mystudent1.ID); 

    Student mystudent3;

    mystudent3.average = 98.22;

    printf("mystudent3.average = %.2f\n", mystudent3.average); 

    // build an arrey of unions
    Student arrStu[3] = {
        10, 30, 40
    };



    return 0;
}


