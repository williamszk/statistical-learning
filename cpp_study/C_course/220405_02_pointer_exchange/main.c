// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203730#overview

#include <stdio.h>

void main()
{
    int num1 = 5, num2 = 7;
    int *ptrA, *ptrB;

    printf("-----------------------------------\n");
    printf("num1 = %d,\t\t num2 = %d \n", num1, num2);
    printf("ptrA = %p, \t ptrB = %p \n", ptrA, ptrB);
    printf("*ptrA = %d, \t\t *ptrB = %d \n", *ptrA, *ptrB);
    printf("&num1 = %p, \t &num2 = %p \n", &num1, &num2);

    ptrA = &num1;
    ptrB = &num2;

    printf("-----------------------------------\n");
    printf("num1 = %d,\t\t num2 = %d \n", num1, num2);
    printf("ptrA = %p, \t ptrB = %p \n", ptrA, ptrB);
    printf("*ptrA = %d, \t\t *ptrB = %d \n", *ptrA, *ptrB);
    printf("&num1 = %p, \t &num2 = %p \n", &num1, &num2);

    printf("-----------------------------------\n");
    *ptrA += 1;
    *ptrB += 3;
    printf("*ptrA += 1;\n");
    printf("*ptrB += 3;\n");
    printf("\n");

    printf("num1 = %d,\t\t num2 = %d \n", num1, num2);
    printf("ptrA = %p, \t ptrB = %p \n", ptrA, ptrB);
    printf("*ptrA = %d, \t\t *ptrB = %d \n", *ptrA, *ptrB);
    printf("&num1 = %p, \t &num2 = %p \n", &num1, &num2);

    ptrA = ptrB;
    ptrB = ptrA;

    printf("-----------------------------------\n");
    printf("num1 = %d,\t\t num2 = %d \n", num1, num2); // 7, 10
    printf("ptrA = %p, \t ptrB = %p \n", ptrA, ptrB); // 0x84, 0x84
    printf("*ptrA = %d, \t\t *ptrB = %d \n", *ptrA, *ptrB); // 10, 10
    printf("&num1 = %p, \t &num2 = %p \n", &num1, &num2); // 0x80, 0x84

    num1 = *ptrB; // num1 <- 10
    num2 = num1 - 3; // num2 <- 7

    printf("-----------------------------------\n");
    printf("num1 = %d,\t\t num2 = %d \n", num1, num2); // 10, 7
    printf("ptrA = %p, \t ptrB = %p \n", ptrA, ptrB); // 0x84, 0x84
    printf("*ptrA = %d, \t\t *ptrB = %d \n", *ptrA, *ptrB); // 7, 7
    printf("&num1 = %p, \t &num2 = %p \n", &num1, &num2); // 0x80, 0x84

}