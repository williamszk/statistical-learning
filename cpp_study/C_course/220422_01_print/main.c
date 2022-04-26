// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20202700#questions

#include <stdio.h>

void main()
{
    char fullName[] = "William Suzuki";
    printf("Full name: %s\n", fullName);

    uint32_t age = 28;
    printf("Age: %d\n", age);

    char gender[] = "male";
    printf("Gender: %s\n", gender);

    // use just 1 printf
    printf("\n\n%s\n%d\n%s\n", fullName, age, gender);
}